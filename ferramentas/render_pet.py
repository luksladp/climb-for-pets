#!/usr/bin/env python3
"""Kit único de render dos pets: mesmas câmeras, luz, fundo e ícone para todos os pets, a partir do GLB.

Uso (a partir da raiz do repositório; precisa de `pip install bpy pillow numpy`):
    python ferramentas/render_pet.py --glb "recursos/Pets lendarios e miticos/Lava Titan/LavaTitan.glb" \
        --saida /tmp/titan [--modo rapido|final] [--vistas frente,tres_quartos,lado] [--sem-icone] \
        [--frente +x|-x|+y|-y] [--clip Idle --quadro 1]

Saída na pasta --saida: frente.png, tres_quartos.png, lado.png (fundo transparente, recorte justo),
icone_128.png (enquadramento padrão do lote) e render.json (tempos e medidas).

- Modo `rapido` (padrão): 512 px, 16 amostras com denoise. Para variantes e rodadas intermediárias.
- Modo `final`: 1024 px, 64 amostras com denoise. Para a variante escolhida e a folha final.
- A frente do pet é achada sozinha pelos olhos (material ou malha com "eye"/"olho" no nome);
  use --frente se o pet não tiver olhos.
- Pose: 1º quadro do clipe Idle (a pose que o jogador vê); sem Idle, a pose de descanso.
- Ícone padrão (regra da nota "Processo rapido de rodada"): vista 3/4 de frente, pet inteiro ocupando 88% do
  lado maior do quadro de 128 px, centrado, fundo transparente, luz de recorte no render e nenhum halo
  ou contorno pintado depois.
- Os efeitos (VFX) não entram aqui: cada pet ainda gera as vistas com efeitos pelo próprio script.
"""

import argparse
import json
import math
import os
import sys
import time
from pathlib import Path

import numpy as np

MODOS = {"rapido": (512, 16), "final": (1024, 64)}
# (graus a partir da frente, para a direita do pet; elevação em graus)
VISTAS = {"frente": (0, 12), "tres_quartos": (40, 12), "lado": (90, 5), "icone": (30, 12)}
ICONE_LADO, ICONE_OCUPACAO = 128, 0.88
EIXOS = {"+x": (1, 0), "-x": (-1, 0), "+y": (0, 1), "-y": (0, -1)}


def args():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--glb", required=True, type=Path)
    p.add_argument("--saida", required=True, type=Path)
    p.add_argument("--modo", choices=sorted(MODOS), default="rapido")
    p.add_argument("--vistas", default="frente,tres_quartos,lado")
    p.add_argument("--sem-icone", action="store_true")
    p.add_argument("--frente", choices=sorted(EIXOS), help="Direção para onde o pet olha (padrão: pelos olhos)")
    p.add_argument("--clip", default="Idle")
    p.add_argument("--quadro", type=int, default=1)
    return p.parse_args()


def preparar_cena(glb, clip, quadro):
    import bpy
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(glb))
    sc = bpy.context.scene
    for arm in [o for o in sc.objects if o.type == "ARMATURE"]:
        ad = arm.animation_data or arm.animation_data_create()
        for t in list(ad.nla_tracks):
            t.mute = True
        acao = bpy.data.actions.get(clip)
        ad.action = acao
        if acao is not None:
            try:
                ad.action_slot = acao.slots[0]
            except Exception:
                pass
    sc.frame_set(quadro)
    return sc


def vertices_mundo(sc):
    """Vértices deformados (pose atual) de todas as malhas visíveis, em coordenadas do mundo."""
    import bpy
    dg = bpy.context.evaluated_depsgraph_get()
    blocos, olhos = [], []
    for o in sc.objects:
        if o.type != "MESH" or o.hide_render:
            continue
        oe = o.evaluated_get(dg)
        me = oe.to_mesh()
        n = len(me.vertices)
        if n:
            co = np.empty(n * 3, dtype=np.float32)
            me.vertices.foreach_get("co", co)
            co = co.reshape(-1, 3)
            m = np.array(oe.matrix_world)
            co = co @ m[:3, :3].T + m[:3, 3]
            blocos.append(co)
            nomes_mat = [s.material.name.lower() for s in o.material_slots if s.material]
            if "eye" in o.name.lower() or "olho" in o.name.lower():
                olhos.append(co)
            elif any("eye" in nm or "olho" in nm for nm in nomes_mat):
                idx = [i for i, s in enumerate(o.material_slots)
                       if s.material and ("eye" in s.material.name.lower() or "olho" in s.material.name.lower())]
                vs = set()
                for poly in me.polygons:
                    if poly.material_index in idx:
                        vs.update(poly.vertices)
                if vs:
                    olhos.append(co[sorted(vs)])
        oe.to_mesh_clear()
    return np.concatenate(blocos), (np.concatenate(olhos) if olhos else None)


def achar_frente(pts, olhos, forcado):
    if forcado:
        return np.array(EIXOS[forcado], dtype=float)
    if olhos is None:
        sys.exit("Sem olhos para achar a frente do pet: use --frente +x|-x|+y|-y")
    centro = (pts.min(0) + pts.max(0)) / 2
    d = olhos.mean(0)[:2] - centro[:2]
    eixo = np.array([1.0, 0.0]) if abs(d[0]) >= abs(d[1]) else np.array([0.0, 1.0])
    return eixo * np.sign(d @ eixo)


def luzes(sc, frente):
    """Luz igual para todos os pets: só sóis (não dependem do tamanho do pet), mais ambiente neutro."""
    import bpy
    from mathutils import Vector
    mundo = bpy.data.worlds.new("mundo")
    sc.world = mundo
    mundo.use_nodes = True
    bg = mundo.node_tree.nodes["Background"]
    bg.inputs["Color"].default_value = (0.42, 0.44, 0.48, 1)
    bg.inputs["Strength"].default_value = 0.9
    f = Vector((frente[0], frente[1], 0))
    direita = f.cross(Vector((0, 0, 1)))

    def sol(nome, de_onde, energia, cor, angulo=0.2):
        ld = bpy.data.lights.new(nome, "SUN")
        ld.energy, ld.color, ld.angle = energia, cor, angulo
        ob = bpy.data.objects.new(nome, ld)
        sc.collection.objects.link(ob)
        ob.rotation_euler = (-de_onde.normalized()).to_track_quat("-Z", "Y").to_euler()

    sol("chave", f * 0.8 + direita * 0.6 + Vector((0, 0, 1.1)), 3.2, (1.0, 0.97, 0.92))
    sol("preenchimento", f * 0.7 - direita * 0.9 + Vector((0, 0, 0.4)), 0.9, (0.85, 0.88, 1.0), 0.5)
    sol("recorte_quente", -f * 1.0 - direita * 0.5 + Vector((0, 0, 0.6)), 2.4, (1.0, 0.62, 0.32), 0.3)
    sol("recorte_frio", -f * 0.6 + direita * 0.8 + Vector((0, 0, 1.2)), 1.6, (0.9, 0.92, 1.0), 0.3)


def camera(sc):
    import bpy
    cd = bpy.data.cameras.new("cam")
    cd.type = "ORTHO"
    cam = bpy.data.objects.new("cam", cd)
    sc.collection.objects.link(cam)
    sc.camera = cam
    return cam


def mirar(cam, pts, frente, graus, elevacao, folga=1.04):
    """Câmera ortográfica justa: projeta os vértices no plano da câmera e enquadra o pet inteiro."""
    from mathutils import Vector
    a = math.radians(graus)
    f = np.array([frente[0], frente[1], 0.0])
    direita = np.cross(f, [0, 0, 1])
    h = f * math.cos(a) + direita * math.sin(a)
    e = math.radians(elevacao)
    d = h * math.cos(e) + np.array([0, 0, math.sin(e)])          # da câmera para fora, a partir do pet
    d /= np.linalg.norm(d)
    rot = Vector(-d).to_track_quat("-Z", "Y")
    m = np.array(rot.to_matrix())
    eixo_x, eixo_y = m[:, 0], m[:, 1]
    px, py = pts @ eixo_x, pts @ eixo_y
    cx, cy = (px.min() + px.max()) / 2, (py.min() + py.max()) / 2
    centro = pts.mean(0)
    centro = centro + eixo_x * (cx - centro @ eixo_x) + eixo_y * (cy - centro @ eixo_y)
    raio = float(np.linalg.norm(pts.max(0) - pts.min(0)))
    cam.location = Vector(centro + d * raio * 3)
    cam.rotation_euler = rot.to_euler()
    cam.data.ortho_scale = max(px.max() - px.min(), py.max() - py.min()) * folga
    cam.data.clip_end = raio * 10


def icone(src, dst):
    from PIL import Image
    im = Image.open(src).convert("RGBA")
    im = im.crop(im.getbbox())
    alvo = round(ICONE_LADO * ICONE_OCUPACAO)
    escala = alvo / max(im.size)
    im = im.resize((max(1, round(im.width * escala)), max(1, round(im.height * escala))), Image.LANCZOS)
    out = Image.new("RGBA", (ICONE_LADO, ICONE_LADO), (0, 0, 0, 0))
    out.paste(im, ((ICONE_LADO - im.width) // 2, (ICONE_LADO - im.height) // 2), im)
    out.save(dst)


def main():
    a = args()
    import bpy
    t0 = time.time()
    a.saida.mkdir(parents=True, exist_ok=True)
    sc = preparar_cena(a.glb.resolve(), a.clip, a.quadro)
    pts, olhos = vertices_mundo(sc)
    frente = achar_frente(pts, olhos, a.frente)
    luzes(sc, frente)
    cam = camera(sc)
    res, amostras = MODOS[a.modo]
    sc.render.engine = "CYCLES"
    sc.cycles.device = "CPU"
    sc.cycles.samples = amostras
    sc.cycles.use_denoising = True
    sc.render.film_transparent = True
    sc.view_settings.view_transform = "Standard"
    sc.render.resolution_x = sc.render.resolution_y = res
    tempos = {"preparar": round(time.time() - t0, 1)}
    vistas = [v for v in a.vistas.split(",") if v]
    if not a.sem_icone:
        vistas.append("icone")
    for v in vistas:
        t = time.time()
        graus, elev = VISTAS[v]
        mirar(cam, pts, frente, graus, elev)
        caminho = a.saida / (("icone_render" if v == "icone" else v) + ".png")
        sc.render.filepath = str(caminho)
        bpy.ops.render.render(write_still=True)
        if v == "icone":
            icone(caminho, a.saida / "icone_128.png")
        tempos[v] = round(time.time() - t, 1)
    altura = float(pts[:, 2].max() - pts[:, 2].min())
    info = {"glb": str(a.glb), "modo": a.modo, "resolucao": res, "amostras": amostras,
            "frente": [float(x) for x in frente], "altura": round(altura, 3), "segundos": tempos,
            "total": round(time.time() - t0, 1)}
    (a.saida / "render.json").write_text(json.dumps(info, ensure_ascii=False, indent=2))
    print(json.dumps(info, ensure_ascii=False))


if __name__ == "__main__":
    main()
