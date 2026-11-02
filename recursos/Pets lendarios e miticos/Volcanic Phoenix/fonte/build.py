"""Volcanic Phoenix (Volcano, Legendary) — régua Steal An Egg, lote 1.

Gera o pet inteiro em Blender headless (pip install bpy, Blender 5.2):
malhas facetadas, rig de 24 ossos, 4 clipes em loop, textura assada 1024 e GLB.

Uso:  python build.py <pasta_saida>
Saída: VolcanicPhoenix.glb, VolcanicPhoenix.blend, tex/*.png
Convenção: 1 unidade = 1 stud, Z para cima, frente +Y, pivô no chão.
A direita do pet é +X (o pet olha para +Y); a asa esquerda (-X) tem a primária quebrada.
"""
import math
import os
import random
import sys

import bpy  # noqa: I001 (bpy registra bmesh e mathutils)
import bmesh
from mathutils import Matrix, Quaternion, Vector, noise

OUT = os.path.abspath(sys.argv[-1] if len(sys.argv) > 1 else "out")
os.makedirs(os.path.join(OUT, "tex"), exist_ok=True)
NAME = "VolcanicPhoenix"

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene


def srgb(h):
    h = h.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return tuple(((x + 0.055) / 1.055) ** 2.4 if x > 0.04045 else x / 12.92 for x in c) + (1.0,)


# ---------------------------------------------------------------- paleta da área Volcano
PAL = {
    "dark": "33293F",     # frestas e sombra entre placas
    "mid": "4A3D60",      # campo da obsidiana (corpo)
    "light": "62537E",    # topo das placas / borda das penas
    "ember0": "8A2010",   # brasa pintada (transição)
    "ember1": "FF4A18",
    "glow": "FF7A1E",
    "glow_hi": "FFC040",
    "gold": "C9962E",
    "gold_hi": "FFC828",  # acento dourado de raridade (filete das garras)
    "basalt": "57505E",
    "pupil": "1C1424",
}

# ---------------------------------------------------------------- utilidades de malha
PIECES = []  # (obj, grupo final)


def new_obj(name, bm, group, mat):
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(name, me)
    scene.collection.objects.link(ob)
    ob["mat"] = mat
    PIECES.append((ob, group))
    return ob


def set_attr(ob, fn):
    """Atributo 'fac' por vértice (0..1) usado pelos materiais (degradê ao longo da pena)."""
    me = ob.data
    at = me.attributes.new("fac", "FLOAT", "POINT")
    for i, v in enumerate(me.vertices):
        at.data[i].value = fn(i, v.co)


def weights(ob, fn):
    """fn(co) -> {osso: peso}."""
    groups = {}
    for v in ob.data.vertices:
        for b, w in fn(v.co).items():
            if w <= 0.001:
                continue
            g = groups.get(b) or ob.vertex_groups.new(name=b)
            groups[b] = g
            g.add([v.index], w, "REPLACE")


def rigid(bone):
    return lambda co: {bone: 1.0}


def smooth(a, b, x):
    t = max(0.0, min(1.0, (x - a) / (b - a)))
    return t * t * (3 - 2 * t)


def blob(name, center, radii, subdiv=3, rough=0.035, seed=0, group="body", mat="stone0",
         rot=(0, 0, 0), squash=None, smooth_shade=False):
    bm = bmesh.new()
    bmesh.ops.create_icosphere(bm, subdivisions=subdiv, radius=1.0)
    R = Matrix.Rotation(rot[0], 3, "X") @ Matrix.Rotation(rot[1], 3, "Y") @ Matrix.Rotation(rot[2], 3, "Z")
    for v in bm.verts:
        n = v.co.normalized()
        d = 1 + rough * noise.noise(n * 2.7 + Vector((seed, seed * 1.3, 0)))
        p = Vector((n.x * radii[0], n.y * radii[1], n.z * radii[2])) * d
        if squash:
            p = squash(p)
        v.co = R @ p + Vector(center)
    for f in bm.faces:
        f.smooth = smooth_shade  # rodada 4: volumes grandes lisos, sem aspecto amassado
    return new_obj(name, bm, group, mat)


def blade(name, M, L, W, T, seg=7, bend=0.0, curl=0.0, t0=0.0, t1=1.0, group="body", mat="feather",
          tipround=0.7, base_w=0.45, broken=None):
    """Pena-lâmina sólida com nervura em V. Espaço local: comprimento +X, largura ±Y, espessura +Z.
    M: Matrix 4x4 que leva o local ao mundo. t0..t1 corta um trecho (para separar a ponta em Glow).
    'fac' guarda t ao longo da pena."""
    bm = bmesh.new()
    rows = []
    ts = [t0 + (t1 - t0) * i / seg for i in range(seg + 1)]
    if broken:
        ts = [t for t in ts if t <= broken] + [broken]
    for t in ts:
        w = W * (base_w + (1 - base_w) * math.sin(min(1.0, t / 0.35) * math.pi / 2)) * (1 - t) ** tipround
        if t >= 0.999:
            w = 0.0
        x = L * t
        z = bend * L * t * t
        y = curl * L * t * t
        th = T * (1 - 0.6 * t)
        pts = [(x, y - w, z), (x, y, z + th * 0.9), (x, y + w, z),
               (x, y + w * 0.6, z - th * 0.35), (x, y, z - th * 0.2), (x, y - w * 0.6, z - th * 0.35)]
        if broken and t == broken:  # quebra irregular
            pts = [(x - 0.05 * L, y - w, z), (x, y, z + th * 0.9), (x - 0.12 * L, y + w, z),
                   (x - 0.1 * L, y + w * 0.6, z - th * 0.35), (x - 0.02 * L, y, z - th * 0.2),
                   (x - 0.06 * L, y - w * 0.6, z - th * 0.35)]
        rows.append([bm.verts.new(M @ Vector(p)) for p in pts])
    for a, b in zip(rows, rows[1:]):
        for k in range(6):
            bm.faces.new((a[k], a[(k + 1) % 6], b[(k + 1) % 6], b[k]))
    bm.faces.new(list(reversed(rows[0])))
    bm.faces.new(rows[-1])
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-5)
    ob = new_obj(name, bm, group, mat)
    # fac = t (posição ao longo da pena) recuperado pela coordenada local x
    Minv = M.inverted()
    set_attr(ob, lambda i, co: max(0.0, min(1.0, (Minv @ co).x / L)))
    return ob


def vein(name, M, L, T, t1, bend, fn, curl=0.0):
    """Rodada 8: veio de lava fino sobre a nervura da pena (malha Glow), continuando os veios do corpo."""
    a = math.atan2(0.54 * T * 0.9, L)
    M2 = M @ Matrix.Translation((0, 0, T * 0.86)) @ Matrix.Rotation(a, 4, "Y")
    blade(name, M2, L * t1, 0.045, 0.03, seg=4, bend=bend, curl=curl * t1, group=("glowV", fn), mat="glow", base_w=1.0,
          tipround=0.5)


def frame(origin, xdir, zhint):
    """Matriz local->mundo com X = xdir e Z ~ zhint."""
    x = Vector(xdir).normalized()
    y = Vector(zhint).cross(x).normalized()
    z = x.cross(y)
    M = Matrix((x, y, z)).transposed().to_4x4()
    M.translation = Vector(origin)
    return M


# ---------------------------------------------------------------- esqueleto (posições de repouso)
# Rodada 2 (revisor do lote): tronco e cabeça ~1,5× mais largos, asas menores e em camadas.
BODY_C = Vector((0, 0.0, 2.95))
RX, RY, RZ = 1.95, 1.38, 1.62  # rodada 9: tronco de Legendary, bem mais largo que as asas
KEEL_C, KEEL_R = BODY_C + Vector((0, 0.82, 0.0)), (1.25, 1.1, 1.25)
HEAD0 = Vector((0, 0.68, 4.12))  # centro da cabeça da v1; os detalhes do rosto são escalados a partir dele
# rodada 10: cabeça de ~1/3 da altura (centro de atenção, como a cara acesa dos SAE), redonda e baixa,
# assentada sobre o tronco (pescoço quase escondido)
HEAD_C = Vector((0, 0.95, 5.38))
HS = 1.85
SHOULDER = Vector((1.65, -0.22, 3.9))
ELBOW = SHOULDER + Vector((0.7, -0.17, 0.5))
HAND = ELBOW + Vector((0.6, -0.15, 0.43))
WS = 1.3  # rodada 14: asas grandes de fênix; escala das penas das asas (rodada 11: asas maiores que o corpo)
TAIL_ROOT = Vector((0, -1.15, 2.65))
N_TAIL = 7
TAIL_ANG = [-0.78, -0.52, -0.26, 0.0, 0.26, 0.52, 0.78]  # rodada 17: leque mais fechado, não vaza pelo lado  # rodada 16: leque atrás do corpo  # rodada 12: leque mais aberto
TAIL_LEN = [3.3, 3.9, 4.3, 4.6, 4.3, 3.9, 3.3]  # rodada 12: cauda longa de fênix (+35%)


def hp(v):
    """Posição de um detalhe do rosto da v1 levada para a cabeça nova."""
    return HEAD_C + (Vector(v) - HEAD0) * HS


def hr(r):
    return tuple(x * HS for x in r)


def tail_dir(i):
    a = TAIL_ANG[i]
    d = Vector((math.sin(a), -math.cos(a), 0))
    d.z = -0.38 + 0.32 * abs(a)  # rodada 12: leque mais alto, as pontas aparecem dos lados do corpo de frente
    return d.normalized()


def mirror(v, s):
    return Vector((v.x * s, v.y, v.z))


def front_y(z, a=0.0):
    """Superfície da frente do tronco (aprox.) na altura z e ângulo a."""
    k = math.sqrt(max(0.05, 1 - ((z - BODY_C.z) / RZ) ** 2))
    y = BODY_C.y + math.cos(a) * RY * 1.12 * k + 0.04
    kk = 1 - ((z - KEEL_C.z) / KEEL_R[2]) ** 2  # a quilha projeta o peito à frente
    if kk > 0:
        y = max(y, KEEL_C.y + math.cos(a * 1.6) * KEEL_R[1] * math.sqrt(kk) * 1.05)
    return Vector((math.sin(a) * RX * k, y, z))


# ---------------------------------------------------------------- corpo
# rodada 7: o corpo é uma camada de lava (malha Glow) coberta por placas de pedra facetadas soltas; as frestas
# entre as placas são as juntas laranja (mesmo material do Lava Titan e do Molten Dragon). As placas são geradas
# em plate_cover() depois das pernas, sobre os elipsoides registrados em UNDER.
UNDER = []  # (centro, raios, grupo das placas, espaçamento, semente)


def under(name, c, r, pgroup, ggroup, sp, seed):
    blob(name, c, r, subdiv=2, rough=0.0, seed=seed, group=ggroup, mat="glow", smooth_shade=True)
    UNDER.append((Vector(c), Vector(r), pgroup, sp, seed))


under("torso", BODY_C, (RX, RY, RZ), "body", "glow_body", 0.8, 1)
under("keel", KEEL_C, KEEL_R, "body", "glow_body", 1.1, 2)  # rodada 14: placas grandes no peito, menores nas bordas
under("rump", Vector((0, -0.95, 2.5)), (1.05, 0.95, 0.8), "body", "glow_body", 0.6, 3)
under("neck", Vector((0, 0.5, 4.45)), (0.62, 0.62, 0.85), "neck", "glow_Neck", 0.52, 4)
HR = Vector((1.36, 1.32, 1.22))  # rodada 10: raios da cabeça (~2,5 de altura, ~1/3 do pet)
FS = 1.13  # escala do rosto (olhos, sobrancelhas, bico) acompanhando a cabeça


# rodada 13: máscara lisa só na cara (olhos, sobrancelhas e bico); o resto da cabeça é placa sobre lava, como o corpo
MC, MR = HEAD_C + Vector((0, 0.3, -0.04)), Vector((1.2, 1.28, 1.14))


def head_surf(x, z, push=0.0):
    """Ponto na frente da máscara da cara em x, z relativos ao centro da cabeça, e a normal ali."""
    z = z + HEAD_C.z - MC.z
    y = MR.y * math.sqrt(max(0.02, 1 - (x / MR.x) ** 2 - (z / MR.z) ** 2))
    off = Vector((x, y, z))
    n = Vector((off.x / MR.x ** 2, off.y / MR.y ** 2, off.z / MR.z ** 2)).normalized()
    return MC + off + n * push, n
# rodada 8: cabeça em máscara de pedra própria, facetada e sem seixos (só exclui as placas do pescoço)
under("head", HEAD_C, HR, "head", "glow_head", 0.72, 5)  # rodada 14: poucas facetas grandes na cabeça
blob("face", MC, MR, subdiv=3, rough=0.03, seed=5, group="head", mat="stone1")
UNDER.append((MC, MR, None, 0, 5))

# rodada 10: bico de fênix em cunha facetada (lê como bico, não como nariz), largo na base e em gancho, num tom
# de pedra mais claro que a cara; a mandíbula de baixo desce e a boca acesa aparece só entre as duas bordas,
# em V (boca recortada do lote, como a do Lava Titan)
BEAK_C, _bn = head_surf(0.0, -0.26 * FS, -0.08)
BS = 1.24  # rodada 17: bico um pouco maior de frente  # rodada 13: bico menor, longe dos cantos dos olhos


def hull(name, pts, group, mat, M=None):
    bm = bmesh.new()
    vs = [bm.verts.new(BEAK_C + ((M @ Vector(q)) if M else Vector(q)) * BS) for q in pts]
    bmesh.ops.convex_hull(bm, input=vs)
    for f in bm.faces:
        f.smooth = False
    return new_obj(name, bm, group, mat)


def sym(pts):
    out = []
    for x, y, z in pts:
        out.append((x, y, z))
        if x:
            out.append((-x, y, z))
    return out


# rodada 11: perfil curvo (culmen em arco até o gancho), não caixa reta
hull("beak_up", sym([(0.4, -0.1, 0.1), (0.34, -0.1, -0.15), (0.0, -0.12, 0.32), (0.0, 0.22, 0.26),
                     (0.0, 0.46, 0.16), (0.16, 0.3, 0.08), (0.0, 0.64, 0.0), (0.0, 0.72, -0.16),
                     (0.0, 0.66, -0.38), (0.06, 0.6, -0.24), (0.2, 0.34, -0.16)]), "head", "beak")
OPEN = Matrix.Translation((0, 0, -0.17)) @ Matrix.Rotation(-0.3, 4, "X") @ Matrix.Translation((0, 0, 0.17))
hull("beak_lo", sym([(0.3, -0.1, -0.2), (0.28, -0.1, -0.46), (0.0, -0.1, -0.54), (0.0, 0.48, -0.3),
                     (0.06, 0.44, -0.24), (0.18, 0.28, -0.21), (0.0, 0.32, -0.48)]), "head", "beak", OPEN)
# interior aceso: só aparece na fresta entre as mandíbulas
hull("mouth", sym([(0.26, -0.12, -0.17), (0.24, -0.12, -0.3), (0.17, 0.26, -0.19), (0.13, 0.24, -0.3),
                   (0.0, 0.44, -0.23), (0.0, 0.36, -0.31)]), "glow_head", "glow")  # rodada 17: fresta menor

# rodada 10: olhos grandes do lote (amêndoa acesa FFB030 com núcleo FFD070, órbita escura funda e sobrancelha de
# pedra inclinada), bem separados do bico e ~1,45× maiores: o rosto vira o centro de atenção
EYE_C = []
for s in (1, -1):
    c, n = head_surf(0.53 * FS * s, 0.14 * FS, -0.05)  # rodada 11: mais de frente (não sobra de lado)
    EYE_C.append(c)
    yaw = math.atan2(abs(n.x), n.y) * 1.0  # rodada 15: olho de frente, longe da borda da cabeça a 3/4
    pitch = math.atan2(n.z, math.hypot(n.x, n.y))
    RM = (Matrix.Rotation(-yaw * s, 3, "Z") @ Matrix.Rotation(pitch, 3, "X")
          @ Matrix.Rotation(-0.3 * s, 3, "Y"))  # canto interno mais baixo

    def almond(p, w=0.44 * FS):
        k = 1 - 0.7 * (p.x / w) ** 2
        return Vector((p.x, p.y, p.z * max(0.2, k)))

    blob(f"socket{s}", c - n * 0.07, (0.52 * FS, 0.14, 0.36 * FS), subdiv=2, rough=0.03, seed=40 + s, group="head",
         mat="socket", squash=lambda p: RM @ p)
    blob(f"eye{s}", c + n * 0.035, (0.44 * FS, 0.06, 0.25 * FS), subdiv=2, rough=0.0, group="eyes", mat="eye",
         squash=lambda p: RM @ almond(p))
    # rodada 12: olho do lote (como o do Lava Titan): amêndoa facetada acesa, sem pupila, núcleo mais claro
    blob(f"eyecore{s}", c + n * 0.09 + Vector((-0.04 * s, 0, -0.02)), (0.2 * FS, 0.025, 0.1 * FS), subdiv=2,
         rough=0.0, group="eyecore", mat="eye", squash=lambda p: RM @ almond(p))
    # sobrancelha de pedra: bloco facetado inclinado para dentro e para baixo, sobre a borda de cima do olho
    RB = (Matrix.Rotation(-yaw * s, 3, "Z") @ Matrix.Rotation(pitch, 3, "X")
          @ Matrix.Rotation(-0.42 * s, 3, "Y"))
    blob(f"brow{s}", c + n * 0.05 + Vector((-0.02 * s, 0, 0.27 * FS)), (0.56 * FS, 0.22, 0.12 * FS), subdiv=1, rough=0.05,
         seed=44 + s, group="head", mat="stone2", squash=lambda p: RB @ p)

# crista: 5 penas-lâmina para trás com pontas em brasa (ponta em Glow)
for k in range(7):  # rodada 16: crista de fênix maior, 7 penas
    a = (k - 3) * 0.22
    d = Vector((math.sin(a) * 0.5, -0.75, 0.55 + 0.1 * (3 - abs(k - 3))))
    M = frame(hp((0.09 * (k - 3) * 0.6, 0.55, 4.6)), d, (0, 0.4, 1))
    L = (0.9 - 0.09 * abs(k - 3)) * 2.6
    blade(f"crest{k}", M, L, 0.26, 0.14, seg=5, bend=0.3, t1=0.62, group="head", mat="wing")
    blade(f"crestG{k}", M, L, 0.26, 0.14, seg=4, bend=0.3, t0=0.6, group="head", mat="brasa")

# rodada 15: sem gola de espetos; o pescoço é placa sobre lava, ligado ao peito

# âncora do pulso do peito (FX_Core e a luz)
core_c = front_y(3.15) + Vector((0, -0.06, 0))  # rodada 7: assentado entre as placas
# rodada 9: sem estrela no peito; a lava aparece só pela rede de fendas entre as placas

# ---------------------------------------------------------------- asas (menores, penas em camadas com volume)
WING_PRIM = [(1.25, 1.35), (1.05, 1.5), (0.82, 1.6), (0.58, 1.66), (0.33, 1.62), (0.08, 1.52), (-0.18, 1.38)]
for s in (1, -1):
    sh, el, ha = mirror(SHOULDER, s), mirror(ELBOW, s), mirror(HAND, s)
    side = "R" if s > 0 else "L"
    W1, W2 = f"Wing1.{side}", f"Wing2.{side}"

    def wfn(co, W1=W1, W2=W2, el=el, sh=sh):
        x = abs(co.x)
        t = smooth(abs(el.x) - 0.25, abs(el.x) + 0.25, x)
        b = smooth(abs(sh.x) - 0.2, abs(sh.x) + 0.2, x)
        return {"Body": 1 - b, W1: b * (1 - t), W2: b * t}

    # ombro e braço emplumados (blobs facetados)
    # rodada 10: ombro e braço com volume (a asa não vira lâmina de lado)
    blob(f"shoulder{side}", sh, (0.82, 0.7, 0.76), subdiv=1, rough=0.08, seed=20 + s, group=wfn, mat="stone0")
    blob(f"arm{side}", (sh + el) / 2, (0.62, 0.4, 0.42), subdiv=2, rough=0.08, seed=22 + s, group=wfn,
         rot=(0, -s * 0.62, 0))
    blob(f"fore{side}", (el + ha) / 2, (0.52, 0.34, 0.36), subdiv=2, rough=0.08, seed=24 + s, group=wfn,
         rot=(0, -s * 0.62, 0))
    # filete de ouro na raiz da asa
    M = frame(sh + Vector((0, 0.3, 0.1)), el - sh, (0, 1, 0))
    blade(f"wgold{side}", M, (el - sh).length * 0.8, 0.05, 0.05, seg=3, group=wfn, mat="gold", base_w=1.0,
          tipround=0.2)

    plane_n = Vector((0, 1, 0.12)).normalized()
    # primárias: 7, em leque; cada uma levemente à frente da anterior (sobreposição em camadas); ponta em Glow
    for k, (ang, L) in enumerate(WING_PRIM):
        d = Vector((math.cos(ang) * s, -0.22, math.sin(ang)))
        org = ha + mirror(Vector((-0.1 * k, 0.035 * k, -0.05 * k)), s)
        M = frame(org, d, plane_n)
        brk = 0.55 if (s < 0 and k == 2) else None
        Lk = L * 1.22 * WS
        blade(f"prim{side}{k}", M, Lk, 0.44, 0.36, seg=7, bend=0.1, t1=0.74, tipround=0.45, group=W2,
              mat="wing", broken=brk)
        vein(f"primV{side}{k}", M, Lk, 0.36, 0.5 if brk else 0.72, 0.1, rigid(W2))
        if brk is None:
            blade(f"primG{side}{k}", M, Lk, 0.44, 0.36, seg=4, bend=0.1, t0=0.72, tipround=0.45,
                  group=W2, mat="ember")
    # secundárias: 6 ao longo do antebraço/braço, apontam para baixo-fora
    for k in range(6):
        u = k / 5
        org = ha.lerp(sh, 0.15 + 0.75 * u) + Vector((0, 0.03 * k, 0))
        ang = -0.35 - 0.75 * u
        d = Vector((math.cos(ang) * s * 0.75, -0.25, math.sin(ang)))
        L = (1.15 - 0.3 * u) * WS
        M = frame(org + Vector((0, -0.05, 0)), d, plane_n)
        blade(f"sec{side}{k}", M, L, 0.3, 0.3, seg=6, bend=0.08, t1=0.82, group=wfn, mat="wing")
        vein(f"secV{side}{k}", M, L, 0.3, 0.8, 0.08, wfn)
        blade(f"secG{side}{k}", M, L, 0.3, 0.3, seg=3, bend=0.08, t0=0.8, group=W2, mat="ember")
    # coberteiras: 4 fileiras por cima do braço, cada uma mais à frente (camadas com volume)
    for row in range(3):
        n = 6 - row
        for k in range(n):
            u = (k + 0.5) / n
            org = sh.lerp(ha, 0.04 + 0.92 * u) + Vector((0, 0.12 + 0.06 * (3 - row), -0.06 - 0.16 * row))
            ang = -0.9 - 0.2 * row + 0.5 * u
            d = Vector((math.cos(ang) * s * 0.55, -0.1, math.sin(ang)))
            L = (0.5 + 0.14 * row) * WS
            M = frame(org, d, plane_n)
            blade(f"cov{side}{row}_{k}", M, L, 0.26, 0.19, seg=4, bend=0.08, group=wfn, mat="wing")

# ---------------------------------------------------------------- cauda: 5 penas longas + 2 plumas de chama
for i in range(N_TAIL):
    d = tail_dir(i)
    L = TAIL_LEN[i]
    side_n = Vector((math.cos(TAIL_ANG[i]), math.sin(TAIL_ANG[i]), 0))  # face larga de lado: lê de perfil e a 3/4
    # rodada 14: face larga meio para cima, meio de lado: o leque se lê de frente, a 3/4 e de lado
    M = frame(TAIL_ROOT + Vector((0.1 * TAIL_ANG[i], 0, 0)), d, (side_n * 0.6 + Vector((0, 0, 1))).normalized())
    b1, b2 = f"Tail{i}_1", f"Tail{i}_2"

    def tfn(co, M=M, L=L, b1=b1, b2=b2):
        t = max(0.0, (M.inverted() @ co).x / L)
        a = smooth(0.0, 0.12, t)
        c = smooth(0.35, 0.6, t)
        return {"Body": 1 - a, b1: a * (1 - c), b2: a * c}

    flame = False  # rodada 17: sem plumas chapadas; todas as penas de pedra com veio e ponta âmbar
    if flame:  # pluma de chama solta, toda em Glow, ondulada
        blade(f"tailF{i}", M, L * 1.05, 0.5, 0.12, seg=8, bend=0.1 * (1 if i < 3 else -1), curl=0.22,
              group=tfn, mat="brasa", base_w=0.4)  # rodada 16: pluma em brasa fosca, sem risco amarelo
    else:
        blade(f"tail{i}", M, L, 0.8, 0.22, seg=8, curl=0.2, t1=0.74, group=tfn, mat="wing", base_w=0.5)
        vein(f"tailV{i}", M, L, 0.22, 0.72, 0.0, tfn, curl=0.2)
        blade(f"tailG{i}", M, L, 0.8, 0.22, seg=5, curl=0.2, t0=0.72, group=tfn, mat="brasa",
              base_w=0.5)
# leque de penas curtas cobrindo a raiz da cauda
for k in range(6):
    a = (k - 2.5) * 0.3
    d = Vector((math.sin(a) * 0.6, -0.8, -0.35)).normalized()
    M = frame(TAIL_ROOT + Vector((0.14 * (k - 2.5), 0.25, 0.22)), d, Vector((0, 0, 1)))
    blade(f"tailcov{k}", M, 0.85, 0.26, 0.12, seg=4, bend=0.1, group="body", mat="wing")

# ---------------------------------------------------------------- pernas: coxa emplumada, tarso de basalto, 4 garras de ouro
HIP_X, ANKLE = 0.85, Vector((0.85, 0.3, 1.22))  # rodada 14: garras maiores, pés no chão
for s in (1, -1):
    side = "R" if s > 0 else "L"
    LB = f"Leg.{side}"
    hip = Vector((HIP_X * s, 0.15, 1.8))
    under(f"thigh{side}", hip, (0.88, 0.88, 0.82), "body", "glow_body", 0.52, 30 + s)
    for k in range(6):  # penas da calça
        a = (k - 2.5) * 0.45
        M = frame(hip + Vector((math.sin(a) * 0.4 + 0.05 * s, math.cos(a) * 0.4, -0.2)),
                  Vector((0, 0, -1)) + Vector((math.sin(a), math.cos(a), 0)) * 0.3,
                  Vector((math.sin(a), math.cos(a), 0)))
        blade(f"pant{side}{k}", M, 0.55, 0.22, 0.12, seg=3, group=LB, mat="wing")
    ankle = mirror(ANKLE, s)
    # rodada 17: perna com forma (não coluna): joelho, tarso afinando com escamas de pedra na frente, tornozelo
    blob(f"knee{side}", Vector((ankle.x, ankle.y - 0.12, 1.3)), (0.46, 0.5, 0.34), subdiv=1, rough=0.06,
         seed=70 + s, group=LB, mat="stone1")
    blob(f"tarsus{side}", Vector((ankle.x, ankle.y - 0.04, 0.86)), (0.4, 0.44, 0.52), subdiv=2, rough=0.05,
         seed=72 + s, group=LB, mat="stone0", rot=(-0.22, 0, 0))
    blob(f"ankleJ{side}", Vector((ankle.x, ankle.y + 0.02, 0.46)), (0.4, 0.42, 0.22), subdiv=1, rough=0.06,
         seed=74 + s, group=LB, mat="stone1")
    for j, z in enumerate((0.64, 0.86, 1.08)):  # escamas na frente do tarso (placas da ave)
        blob(f"scute{side}{j}", Vector((ankle.x, ankle.y + 0.34 - 0.06 * j, z)), (0.34 - 0.02 * j, 0.12, 0.13),
             subdiv=1, rough=0.05, seed=76 + j + s, group=LB, mat="stone2", rot=(-0.22, 0, 0))
    blob(f"foot{side}", Vector((ankle.x, ankle.y, 0.32)), (0.5, 0.55, 0.24), subdiv=1, rough=0.05, group=LB, mat="basalt")
    # rodada 15: dedos de pedra (3 à frente, 1 atrás) com garra curta e escura na ponta
    for k, a in enumerate((-0.5, 0.0, 0.5, math.pi)):
        d = Vector((math.sin(a), math.cos(a), -0.12)).normalized()
        Lt = 0.62 if k < 3 else 0.4
        tc = ankle + Vector((0, 0, -0.62)) + d * (0.3 + Lt * 0.5)
        tc.z = 0.2
        blob(f"toe{side}{k}", tc, (0.2, Lt * 0.62, 0.18), subdiv=1, rough=0.05, seed=60 + k, group=LB,
             mat="basalt", rot=(0, 0, -a))
        tip = Vector((tc.x, tc.y, 0.0)) + Vector((d.x, d.y, 0)) * Lt * 0.5 + Vector((0, 0, 0.38))
        M = frame(tip, Vector((d.x, d.y, -0.25)), Vector((0, 0, 1)))
        blade(f"claw{side}{k}", M, 0.48, 0.24, 0.22, seg=3, bend=-0.7, group=LB, mat="gold_claw", base_w=1.0,
              tipround=1.0)


# ---------------------------------------------------------------- rodada 7: placas de pedra facetadas
def inside(p, c, r, k=1.0):
    d = p - c
    return (d.x / r.x) ** 2 + (d.y / r.y) ** 2 + (d.z / r.z) ** 2 < k * k


def slab(bm, p, nrm, rad, th, rnd):
    """Placa de pedra: polígono irregular de 5–7 lados, lateral reta e topo chanfrado (facetado)."""
    nrm = (nrm + Vector((rnd.uniform(-1, 1), rnd.uniform(-1, 1), rnd.uniform(-1, 1))) * 0.14).normalized()
    t1 = nrm.orthogonal().normalized()
    t1.rotate(Matrix.Rotation(rnd.uniform(0, math.tau), 3, nrm))
    t2 = nrm.cross(t1)
    k = rnd.choice((4, 5, 5, 6))  # rodada 12: placas angulares, menos lados (traço do Lava Titan)
    ang = sorted(math.tau * (i + rnd.uniform(-0.25, 0.25)) / k for i in range(k))
    rs = [rad * rnd.uniform(0.82, 1.12) for _ in ang]
    sx = rnd.uniform(0.85, 1.2)
    ring = lambda h, f: [bm.verts.new(p + nrm * h + (t1 * math.cos(a) * sx + t2 * math.sin(a) / sx) * r * f)
                         for a, r in zip(ang, rs)]
    lo, mid, top = ring(-0.16, 0.9), ring(th * 0.7, 1.0), ring(th, 0.82)
    for a, b in ((lo, mid), (mid, top)):
        for i in range(k):
            bm.faces.new((a[i], a[(i + 1) % k], b[(i + 1) % k], b[i]))
    bm.faces.new(top)


def plate_cover():
    """Rodada 13: placas recortadas em células de Voronoi sobre a camada de lava, com fresta fina e constante
    entre vizinhas (mesmo método das placas do Lava Titan): a lava vira uma rede de veios finos no corpo todo."""
    rnd = random.Random(7)
    keep_out = [(BEAK_C + Vector((0, 0.1, -0.1)), 0.3)]
    seeds = []
    for ci, (c, r, pg, sp, seed) in enumerate(UNDER):
        if pg is None:
            continue
        a, b, cc = r
        area = 4 * math.pi * (((a * b) ** 1.6 + (a * cc) ** 1.6 + (b * cc) ** 1.6) / 3) ** (1 / 1.6)
        N = int(area / (sp * sp) * 1.1)
        for i in range(N):
            z = 1 - 2 * (i + 0.5) / N
            q = math.sqrt(1 - z * z)
            phi = i * math.pi * (3 - math.sqrt(5)) + seed
            u = Vector((q * math.cos(phi), q * math.sin(phi), z))
            p = c + Vector((u.x * r.x, u.y * r.y, u.z * r.z))
            # rodada 14: semente deslocada ao acaso (placas irregulares, não favo)
            jit = Vector((rnd.uniform(-1, 1), rnd.uniform(-1, 1), rnd.uniform(-1, 1))) * sp * 0.32
            w = (p + jit - c)
            w = Vector((w.x / r.x, w.y / r.y, w.z / r.z)).normalized()
            u = w
            p = c + Vector((u.x * r.x, u.y * r.y, u.z * r.z))
            if any(inside(p, c2, r2, 0.97 if pg2 is None else 0.86) for j, (c2, r2, pg2, *_) in enumerate(UNDER) if j != ci):  # rodada 15: placas cobrem as junções
                continue
            if any((p - kc).length < kr for kc, kr in keep_out):
                continue
            nrm = Vector((u.x / r.x, u.y / r.y, u.z / r.z)).normalized()
            if pg == "head" and nrm.z > -0.3 and inside(p + nrm * 0.3, MC, MR):
                continue  # a cara fica na máscara lisa
            seeds.append((p, nrm, sp * rnd.uniform(0.78, 1.22), pg))
    GAP = 0.05
    groups = {}
    for i, (p, n, d, pg) in enumerate(seeds):
        t1 = n.orthogonal().normalized()
        t2 = n.cross(t1)
        Fm = Matrix((t1, t2, n)).transposed()
        Ft = Fm.transposed()
        poly = [Vector((math.cos(a), math.sin(a))) * d * 0.85 for a in [k * math.tau / 8 + 0.2 for k in range(8)]]
        for j, (q0, _, dj, _) in enumerate(seeds):
            if j == i or (q0 - p).length > (d + dj) * 1.2:
                continue
            q = Ft @ (q0 - p)
            if abs(q.z) > 0.6 * q.length + 0.05:
                continue
            uu = Vector((q.x, q.y))
            L = uu.length
            if L < 1e-5:
                continue
            cut = (L * L + (d * d - dj * dj) * 0.25) / (2 * L) - GAP / 2
            out = []
            for k in range(len(poly)):
                P, Q = poly[k], poly[(k + 1) % len(poly)]
                fp, fq = P.dot(uu / L) - cut, Q.dot(uu / L) - cut
                if fp <= 0:
                    out.append(P)
                if (fp < 0) != (fq < 0) and abs(fp - fq) > 1e-9:
                    out.append(P.lerp(Q, fp / (fp - fq)))
            poly = out
            if len(poly) < 3:
                break
        if len(poly) < 3:
            continue
        cen = sum(poly, Vector((0, 0))) / len(poly)
        h = d * rnd.uniform(0.22, 0.3) * (0.6 if pg == "head" else 1.0)  # rodada 14: cabeça facetada, placas baixas
        pts = []
        for v in poly:
            pts.append(Vector((v.x, v.y, -0.16)))
            pts.append(Vector((v.x, v.y, h * 0.55 + rnd.uniform(-0.02, 0.02))))
            w = v.lerp(cen, 0.2)
            pts.append(Vector((w.x, w.y, h * rnd.uniform(0.85, 1.0))))
        pts.append(Vector((cen.x, cen.y, h * 1.08)))
        bm = groups.setdefault((pg, rnd.randrange(3)), bmesh.new())
        tilt = Matrix.Rotation(rnd.uniform(-0.09, 0.09), 3, "X") @ Matrix.Rotation(rnd.uniform(-0.09, 0.09), 3, "Y")
        vs = [bm.verts.new(p + Fm @ (tilt @ v)) for v in pts]
        bmesh.ops.convex_hull(bm, input=vs)
    for (pg, m), bm in groups.items():
        for f in bm.faces:
            f.smooth = False
        new_obj(f"plates_{pg}_{m}", bm, pg, f"stone{m}")


plate_cover()




# ---------------------------------------------------------------- materiais procedurais (para assar)


def node_mat(name, build):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    for n in list(nt.nodes):
        nt.nodes.remove(n)
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
    nt.links.new(bsdf.outputs[0], out.inputs[0])
    build(nt, bsdf)
    return m


def ramp(nt, fac_socket, stops):
    r = nt.nodes.new("ShaderNodeValToRGB")
    cr = r.color_ramp
    for i, (p, c) in enumerate(stops):
        el = cr.elements[i] if i < 2 else cr.elements.new(p)
        el.position = p
        el.color = srgb(c)
    nt.links.new(fac_socket, r.inputs[0])
    return r


def lava_veins(nt, base_socket, bsdf, everywhere=False, scale=0.95, vein=0.026):
    """Padrão do lote Volcano: obsidiana fosca + rede de veias finas laranja-lava em todo o corpo.
    Voronoi distância-até-borda em coordenada de objeto, distorcido por ruído, densidade média.
    As veias vão para a cor e para a emissão (assada como EmissiveMap)."""
    tc = nt.nodes.new("ShaderNodeTexCoord")
    nz = nt.nodes.new("ShaderNodeTexNoise")
    nz.inputs["Scale"].default_value = 5.0
    mix = nt.nodes.new("ShaderNodeVectorMath")
    mix.operation = "MULTIPLY_ADD"
    mix.inputs[1].default_value = (0.12, 0.12, 0.12)
    nt.links.new(nz.outputs["Color"], mix.inputs[0])
    nt.links.new(tc.outputs["Object"], mix.inputs[2])
    vor = nt.nodes.new("ShaderNodeTexVoronoi")
    vor.feature = "DISTANCE_TO_EDGE"
    vor.inputs["Scale"].default_value = scale
    nt.links.new(mix.outputs[0], vor.inputs["Vector"])
    # máscara da veia: 1 no centro da fissura, 0 a partir de VEIN
    VEIN = vein  # calibre médio (mesma largura absoluta da rodada 3), placas maiores
    mr = nt.nodes.new("ShaderNodeMapRange")
    mr.inputs["From Min"].default_value = 0.0
    mr.inputs["From Max"].default_value = VEIN
    mr.inputs["To Min"].default_value = 1.0
    mr.inputs["To Max"].default_value = 0.0
    nt.links.new(vor.outputs["Distance"], mr.inputs["Value"])
    # veias só nos veios principais: frente (peito, garganta, rosto) e trechos escolhidos por um ruído largo;
    # costas e laterais ficam em pedra fosca sem brilho
    sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    nt.links.new(tc.outputs["Object"], sep.inputs[0])
    # rodada 6: as veias saem do coração de lava no peito e ficam esparsas nas bordas
    dist = nt.nodes.new("ShaderNodeVectorMath")
    dist.operation = "DISTANCE"
    dist.inputs[1].default_value = tuple(core_c)
    nt.links.new(tc.outputs["Object"], dist.inputs[0])
    fr = nt.nodes.new("ShaderNodeMapRange")
    fr.inputs["From Min"].default_value = 0.8
    fr.inputs["From Max"].default_value = 2.3
    fr.inputs["To Min"].default_value = 1.0
    fr.inputs["To Max"].default_value = 0.0
    nt.links.new(dist.outputs["Value"], fr.inputs["Value"])
    big = nt.nodes.new("ShaderNodeTexNoise")
    big.inputs["Scale"].default_value = 0.9
    nt.links.new(tc.outputs["Object"], big.inputs["Vector"])
    gt = nt.nodes.new("ShaderNodeMapRange")
    gt.inputs["From Min"].default_value = 0.58
    gt.inputs["From Max"].default_value = 0.63
    nt.links.new(big.outputs["Fac"], gt.inputs["Value"])
    reg = nt.nodes.new("ShaderNodeMath")
    reg.operation = "MAXIMUM"
    nt.links.new(fr.outputs["Result"], reg.inputs[0])
    nt.links.new(gt.outputs["Result"], reg.inputs[1])
    face = nt.nodes.new("ShaderNodeMapRange")  # rodada 4: nenhuma veia no rosto/cabeça
    face.inputs["From Min"].default_value = 6.4  # rodada 6: cabeça com as mesmas veias do corpo
    face.inputs["From Max"].default_value = 6.5
    face.inputs["To Min"].default_value = 1.0
    face.inputs["To Max"].default_value = 0.0
    nt.links.new(sep.outputs["Z"], face.inputs["Value"])
    reg2 = nt.nodes.new("ShaderNodeMath")
    reg2.operation = "MULTIPLY"
    nt.links.new(reg.outputs[0], reg2.inputs[0])
    nt.links.new(face.outputs["Result"], reg2.inputs[1])
    vm = nt.nodes.new("ShaderNodeMath")
    vm.operation = "MULTIPLY"
    nt.links.new(mr.outputs["Result"], vm.inputs[0])
    nt.links.new(reg2.outputs[0], vm.inputs[1])
    if not everywhere:  # rodada 15: nas penas a rede de veios vale em toda a pena (como a membrana do Dragon)
        mr = vm
    lava = ramp(nt, vor.outputs["Distance"], [(0.0, PAL["glow_hi"]), (VEIN * 0.45, PAL["glow"]),
                                              (VEIN, PAL["ember0"])])
    mx = nt.nodes.new("ShaderNodeMix")
    mx.data_type = "RGBA"
    nt.links.new(mr.outputs[0], mx.inputs["Factor"])
    nt.links.new(base_socket, mx.inputs["A"])
    nt.links.new(lava.outputs[0], mx.inputs["B"])
    nt.links.new(mx.outputs["Result"], bsdf.inputs["Base Color"])
    em = nt.nodes.new("ShaderNodeMix")
    em.data_type = "RGBA"
    em.inputs["A"].default_value = (0, 0, 0, 1)
    nt.links.new(mr.outputs[0], em.inputs["Factor"])
    nt.links.new(lava.outputs[0], em.inputs["B"])
    nt.links.new(em.outputs["Result"], bsdf.inputs["Emission Color"])
    bsdf.inputs["Emission Strength"].default_value = 1.0
    bsdf.inputs["Roughness"].default_value = 0.68  # fosco: sem reflexo branco
    bsdf.inputs["Metallic"].default_value = 0.0
    return tc


def obsidian(nt, bsdf):
    tc = nt.nodes.new("ShaderNodeTexCoord")
    nz = nt.nodes.new("ShaderNodeTexNoise")
    nz.inputs["Scale"].default_value = 3.5
    nt.links.new(tc.outputs["Object"], nz.inputs["Vector"])
    base = ramp(nt, nz.outputs["Fac"], [(0.25, PAL["dark"]), (0.5, PAL["mid"]), (0.8, PAL["light"])])  # sem manchas
    lava_veins(nt, base.outputs[0], bsdf)


def feather(nt, bsdf, ember_core=False):
    at = nt.nodes.new("ShaderNodeAttribute")
    at.attribute_name = "fac"
    # base obsidiana, ponta em gradiente vermelho → laranja (a ponta final é a peça Glow)
    stops = [(0.0, "48454D"), (0.5, "55515B"), (0.85, "625E68")]  # rodada 16: pena no cinza do corpo  # rodada 13: pena de pedra, sem degradê marrom
    r = ramp(nt, at.outputs["Fac"], stops)
    if ember_core == "veins":  # rodada 15: pena de pedra escura com rede de rachaduras de lava
        r2 = ramp(nt, at.outputs["Fac"], [(0.0, "3A373E"), (0.6, "47434C"), (1.0, "534F59")])
        lava_veins(nt, r2.outputs[0], bsdf, everywhere=True, scale=1.5, vein=0.07)
        return
    if ember_core:  # pena de asa/cauda: lâmina limpa, sem rachadura; só a ponta acende (peça Glow)
        nt.links.new(r.outputs[0], bsdf.inputs["Base Color"])
        bsdf.inputs["Roughness"].default_value = 0.6
        bsdf.inputs["Emission Color"].default_value = (0, 0, 0, 1)
        return
    lava_veins(nt, r.outputs[0], bsdf)


def stone(c0, c1):
    """Pedra das placas (rodada 7): fosca, sem veias; leve variação de tom dentro da placa."""
    def b(nt, bsdf):
        tc = nt.nodes.new("ShaderNodeTexCoord")
        nz = nt.nodes.new("ShaderNodeTexNoise")
        nz.inputs["Scale"].default_value = 2.4
        nt.links.new(tc.outputs["Object"], nz.inputs["Vector"])
        r = ramp(nt, nz.outputs["Fac"], [(0.3, c0), (0.7, c1)])
        # rodada 17: cada placa com valor próprio: bordas/quinas mais claras (pointiness), fundo das fendas escuro (AO)
        geo = nt.nodes.new("ShaderNodeNewGeometry")
        edge = ramp(nt, geo.outputs["Pointiness"], [(0.5, "000000"), (0.58, "FFFFFF")])
        lit = nt.nodes.new("ShaderNodeMix")
        lit.data_type = "RGBA"
        lit.blend_type = "SCREEN"
        lit.inputs["Factor"].default_value = 1.0
        nt.links.new(r.outputs[0], lit.inputs[6])
        sc = nt.nodes.new("ShaderNodeMix")
        sc.data_type = "RGBA"
        nt.links.new(edge.outputs[0], sc.inputs["Factor"])
        sc.inputs[6].default_value = (0, 0, 0, 1)
        sc.inputs[7].default_value = (0.1, 0.095, 0.11, 1)
        nt.links.new(sc.outputs[2], lit.inputs[7])
        ao = nt.nodes.new("ShaderNodeAmbientOcclusion")
        ao.inputs["Distance"].default_value = 0.35
        aor = ramp(nt, ao.outputs["AO"], [(0.25, "8C8C8C"), (0.8, "FFFFFF")])
        dk = nt.nodes.new("ShaderNodeMix")
        dk.data_type = "RGBA"
        dk.blend_type = "MULTIPLY"
        dk.inputs["Factor"].default_value = 1.0
        nt.links.new(lit.outputs[2], dk.inputs[6])
        nt.links.new(aor.outputs[0], dk.inputs[7])
        nt.links.new(dk.outputs[2], bsdf.inputs["Base Color"])
        bsdf.inputs["Roughness"].default_value = 0.78
        bsdf.inputs["Metallic"].default_value = 0.0
        bsdf.inputs["Emission Color"].default_value = (0, 0, 0, 1)
    return b


def brasa(nt, bsdf):
    """Rodada 9: ponta da crista em laranja-brasa (sem amarelo-dourado), acesa pelo EmissiveMap."""
    bsdf.inputs["Base Color"].default_value = srgb("D46F1A")  # rodada 17: o mesmo âmbar das fissuras (uma cor só)
    bsdf.inputs["Roughness"].default_value = 0.6
    bsdf.inputs["Metallic"].default_value = 0.0
    bsdf.inputs["Emission Color"].default_value = srgb("7A3608")


def flat(color, rough, metal):
    def b(nt, bsdf):
        bsdf.inputs["Base Color"].default_value = srgb(color)
        bsdf.inputs["Roughness"].default_value = rough
        bsdf.inputs["Metallic"].default_value = metal
        bsdf.inputs["Emission Color"].default_value = (0, 0, 0, 1)
    return b


MATS = {
    "obsidian": node_mat("obsidian", obsidian),
    "feather": node_mat("feather", feather),
    "wing": node_mat("wing", lambda nt, b: feather(nt, b, True)),
    "wingv": node_mat("wingv", lambda nt, b: feather(nt, b, "veins")),
    # rodada 9: pedra puxada para o cinza-ardósia do Lava Titan
    "stone0": node_mat("stone0", stone("55525A", "67636C")),  # rodada 14: grafite médio, como o cinza do Lava Titan
    "stone1": node_mat("stone1", stone("5E5A63", "726D77")),
    "stone2": node_mat("stone2", stone("6C6872", "827D88")),
    "brasa": node_mat("brasa", brasa),
    "ember": node_mat("ember", flat("5A5660", 0.75, 0.0)),  # rodada 16: ponta de pedra: ponta de pedra; o laranja fica nos veios
    "gold": node_mat("gold", flat(PAL["gold"], 0.62, 0.6)),  # dourado fosco
    "beak": node_mat("beak", flat("B3ADB8", 0.6, 0.0)),  # rodada 16: pedra clara (cor de dente do Lava Titan), contrasta com a cara  # rodada 12: bico laranja-brasa fosco (família das pontas das penas)
    "socket": node_mat("socket", flat("140F1C", 0.8, 0.0)),  # órbita escura e funda
    "gold_claw": node_mat("gold_claw", flat("2A2236", 0.6, 0.0)),  # rodada 8: garras escuras
    "basalt": node_mat("basalt", flat(PAL["basalt"], 0.8, 0.0)),
    "pupil": node_mat("pupil", flat(PAL["pupil"], 0.4, 0.0)),
}

# ---------------------------------------------------------------- armature
arm_data = bpy.data.armatures.new(NAME + "_Rig")
rig = bpy.data.objects.new(NAME + "_Rig", arm_data)
scene.collection.objects.link(rig)
bpy.context.view_layer.objects.active = rig
bpy.ops.object.mode_set(mode="EDIT")
EB = arm_data.edit_bones


def bone(name, h, t, parent=None, roll_up=(0, 0, 1)):
    b = EB.new(name)
    b.head, b.tail = Vector(h), Vector(t)
    b.align_roll(Vector(roll_up))
    if parent:
        b.parent = EB[parent]
    return b


bone("Root", (0, 0, 0), (0, 0.6, 0), roll_up=(0, 0, 1))
bone("Body", (0, 0, 2.3), (0, 0.15, 3.65), "Root", roll_up=(0, 1, 0))
bone("Neck", (0, 0.4, 3.95), (0, 0.7, 4.45), "Body", roll_up=(0, 1, 0))
bone("Head", (0, 0.7, 4.45), (0, 1.1, 5.6), "Neck", roll_up=(0, 1, 0))
for s, side in ((1, "R"), (-1, "L")):
    bone(f"Wing1.{side}", mirror(SHOULDER, s), mirror(ELBOW, s), "Body", roll_up=(0, 1, 0))
    bone(f"Wing2.{side}", mirror(ELBOW, s), mirror(HAND, s), f"Wing1.{side}", roll_up=(0, 1, 0))
    bone(f"Leg.{side}", (HIP_X * s, 0.15, 1.8), mirror(ANKLE, s), "Body", roll_up=(0, 1, 0))
for i in range(N_TAIL):
    d = tail_dir(i)
    L = TAIL_LEN[i]
    o = TAIL_ROOT + Vector((0.1 * TAIL_ANG[i], 0, 0))
    bone(f"Tail{i}_1", o, o + d * L * 0.48, "Body")
    bone(f"Tail{i}_2", o + d * L * 0.48, o + d * L, f"Tail{i}_1")
bpy.ops.object.mode_set(mode="OBJECT")

# ---------------------------------------------------------------- pesos e junção por malha final
FINAL = {"Body": [], "Glow": [], "Eyes": [], "EyeCore": []}
for ob, group in PIECES:
    target = "Body"
    fn = None
    if isinstance(group, tuple):
        group, fn = group
    if isinstance(group, str) and group.startswith("glow"):
        target = "Glow"
        g = group.split("_", 1)[1] if "_" in group else "Body"
        if group.startswith("glowW_"):
            side = group[-1]
            g = f"Wing2.{side}"
        if group == "glowT":
            g = None
        fn = fn or ({"body": rigid("Body"), "head": rigid("Head")}.get(g) or rigid(g))
    elif group == "eyecore":
        target, fn = "EyeCore", rigid("Head")
    elif group == "eyes":
        target, fn = "Eyes", rigid("Head")
    elif callable(group):
        fn = group
    else:
        fn = {"body": rigid("Body"), "head": rigid("Head"), "neck": rigid("Neck")}.get(group) or rigid(group)
    weights(ob, fn)
    m = MATS.get(ob["mat"])
    if target == "Body":
        ob.data.materials.append(m or MATS["obsidian"])
    FINAL[target].append(ob)


def join(objs, name):
    bpy.ops.object.select_all(action="DESELECT")
    for o in objs:
        o.select_set(True)
    bpy.context.view_layer.objects.active = objs[0]
    bpy.ops.object.join()
    ob = bpy.context.active_object
    ob.name = ob.data.name = name
    return ob


body = join(FINAL["Body"], NAME + "_Body")
glow = join(FINAL["Glow"], NAME + "_Glow")
eyes = join(FINAL["Eyes"], NAME + "_Eyes")
eyecore = join(FINAL["EyeCore"], NAME + "_EyeCore")

# ---------------------------------------------------------------- UV + bake (Color, Roughness, Metalness) 1024
bpy.ops.object.select_all(action="DESELECT")
bpy.context.view_layer.objects.active = body
body.select_set(True)
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.select_all(action="SELECT")
bpy.ops.uv.smart_project(angle_limit=math.radians(50), island_margin=0.004)
bpy.ops.object.mode_set(mode="OBJECT")

scene.render.engine = "CYCLES"
scene.cycles.device = "CPU"
scene.cycles.samples = 4
SIZE = 1024


def bake_pass(label, socket_fn):
    img = bpy.data.images.new(f"{NAME}_{label}", SIZE, SIZE, alpha=False)
    if label not in ("Color", "Emissive"):
        img.colorspace_settings.name = "Non-Color"
    saved = []
    for m in body.data.materials:
        nt = m.node_tree
        bsdf = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
        out = next(n for n in nt.nodes if n.type == "OUTPUT_MATERIAL")
        em = nt.nodes.new("ShaderNodeEmission")
        src = bsdf.inputs[socket_fn]
        if src.links:
            nt.links.new(src.links[0].from_socket, em.inputs[0])
        else:
            v = src.default_value
            em.inputs[0].default_value = tuple(v) if hasattr(v, "__len__") else (v, v, v, 1)
        old = out.inputs[0].links[0].from_socket
        nt.links.new(em.outputs[0], out.inputs[0])
        tn = nt.nodes.new("ShaderNodeTexImage")
        tn.image = img
        nt.nodes.active = tn
        saved.append((nt, old, out, em, tn))
    bpy.ops.object.bake(type="EMIT", margin=6)
    path = os.path.join(OUT, "tex", f"{NAME}_{label}.png")
    img.filepath_raw = path
    img.file_format = "PNG"
    img.save()
    for nt, old, out, em, tn in saved:
        nt.links.new(old, out.inputs[0])
        nt.nodes.remove(em)
        nt.nodes.remove(tn)
    return img


img_c = bake_pass("Color", "Base Color")
img_r = bake_pass("Roughness", "Roughness")
img_m = bake_pass("Metalness", "Metallic")
img_e = bake_pass("Emissive", "Emission Color")

# material final único do corpo (o que vai no GLB / SurfaceAppearance)
final = bpy.data.materials.new(NAME + "_Body")
final.use_nodes = True
nt = final.node_tree
bsdf = nt.nodes["Principled BSDF"]
for img, sock in ((img_c, "Base Color"), (img_r, "Roughness"), (img_m, "Metallic"), (img_e, "Emission Color")):
    tn = nt.nodes.new("ShaderNodeTexImage")
    tn.image = img
    nt.links.new(tn.outputs[0], bsdf.inputs[sock])
bsdf.inputs["Emission Strength"].default_value = 2.2
body.data.materials.clear()
body.data.materials.append(final)


def emissive(name, color, strength):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = srgb(color)
    b.inputs["Emission Color"].default_value = srgb(color)
    b.inputs["Emission Strength"].default_value = strength
    return m


glow.data.materials.append(emissive(NAME + "_Glow", "FF9A28", 0.75))  # rodada 7: uma só cor de brilho
eyes.data.materials.append(emissive(NAME + "_Eyes", "FFB030", 2.4))
eyecore.data.materials.append(emissive(NAME + "_EyeCore", "FFD070", 2.8))

for ob in (body, glow, eyes, eyecore):
    ob.parent = rig
    mod = ob.modifiers.new("Armature", "ARMATURE")
    mod.object = rig

# ---------------------------------------------------------------- animação (30 fps, loops fechados)
scene.render.fps = 30
PB = rig.pose.bones
REST = {b.name: b.bone.matrix_local.to_3x3() for b in PB}


def rot(bname, axis, ang):
    """Rotação em torno de um eixo do espaço do rig (rest), convertida para o local do osso."""
    R = REST[bname]
    q = (R.inverted() @ Matrix.Rotation(ang, 3, Vector(axis)) @ R).to_quaternion()
    return q


def compose(bname, *rs):
    q = Quaternion()
    for axis, ang in rs:
        q = rot(bname, axis, ang) @ q
    return q


X, Y, Z = (1, 0, 0), (0, 1, 0), (0, 0, 1)
TAU = 2 * math.pi


def pose_common(t, flap, flap_amp, flap_base, bob, pitch, head_yaw, tail_amp, tail_speed, roll=0.0,
                fold=0.0, flare=0.0):
    P = {}
    P["Root"] = (Vector((0, 0, bob)), Quaternion())
    # o giro de barril é no osso Body (pivô no centro do corpo, não no chão)
    P["Body"] = (Vector((0, 0, 0.45 * math.sin(roll / 2) ** 2)), compose("Body", (X, -pitch), (Y, roll)))
    P["Neck"] = (None, compose("Neck", (X, pitch * 0.6 + 0.04 * math.sin(TAU * t)), (Z, head_yaw * 0.4)))
    P["Head"] = (None, compose("Head", (X, pitch * 0.4 - 0.05 * math.sin(TAU * t + 1)), (Z, head_yaw * 0.6)))
    for s, side in ((1, "R"), (-1, "L")):
        w = flap_base + flap_amp * flap
        # flap: gira em torno do eixo frente-trás (Y); fold: dobra para a frente e para baixo
        P[f"Wing1.{side}"] = (None, compose(f"Wing1.{side}", (Y, -s * w), (Z, s * (0.9 * fold - 0.15 * flare)),
                                            (X, 0.6 * fold)))
        P[f"Wing2.{side}"] = (None, compose(f"Wing2.{side}", (Y, -s * 0.45 * w), (Z, s * 0.8 * fold)))
        P[f"Leg.{side}"] = (None, compose(f"Leg.{side}", (X, -0.25 * pitch / 0.26 if pitch else 0.0)))
    for i in range(N_TAIL):
        ph = TAU * tail_speed * t - i * 0.5
        P[f"Tail{i}_1"] = (None, compose(f"Tail{i}_1", (X, tail_amp * math.sin(ph)),
                                         (Z, 0.08 * math.sin(ph + 1.3) + 0.25 * flare * TAIL_ANG[i])))
        P[f"Tail{i}_2"] = (None, compose(f"Tail{i}_2", (X, tail_amp * 1.5 * math.sin(ph - 0.9)),
                                         (Z, 0.12 * math.sin(ph + 0.4))))
    return P


def idle(t):  # 3,0 s: paira, 2 batidas lentas, cabeça vira, cauda ondula com atraso
    flap = math.sin(TAU * 2 * t)
    return pose_common(t, flap, 0.32, 0.0, 0.12 * math.sin(TAU * 2 * t - 0.6), 0.0,
                       0.35 * math.sin(TAU * t), 0.1, 1, 0.0)


def fly(t):  # 1,2 s: corpo inclinado 15°, 2 batidas fortes
    flap = math.sin(TAU * 2 * t)
    return pose_common(t, flap, 0.62, -0.1, 0.18 * math.sin(TAU * 2 * t - 0.8), math.radians(15),
                       0.0, 0.16, 2, 0.0)


def happy(t):  # 2,2 s: giro de barril + bico abre (grito)
    roll_t = smooth(0.15, 0.65, t)
    flap = math.sin(TAU * 3 * t)
    P = pose_common(t, flap, 0.45, 0.15, 0.35 * math.sin(math.pi * t) ** 2, 0.0, 0.0, 0.18, 2,
                    roll=TAU * roll_t)
    g = math.sin(math.pi * smooth(0.65, 0.95, t))
    P["Head"] = (None, compose("Head", (X, 0.45 * g)))
    P["Neck"] = (None, compose("Neck", (X, -0.25 * g)))
    return P


def flare(t):  # 2,0 s: fecha (0–0,4) → abre com estouro (0,4) → assenta
    close = smooth(0.0, 0.2, t) * (1 - smooth(0.2, 0.26, t))
    burst = smooth(0.2, 0.26, t) * (1 - smooth(0.4, 0.95, t))
    flap = 0.0
    base = -0.35 * close + 0.55 * burst
    P = pose_common(t, flap, 0.0, base, -0.15 * close + 0.25 * burst, -0.2 * close, 0.0,
                    0.1 + 0.15 * burst, 1, fold=close, flare=burst)
    P["Head"] = (None, compose("Head", (X, 0.5 * burst - 0.2 * close)))
    return P


CLIPS = [("Idle", 90, idle), ("Fly", 36, fly), ("Happy", 66, happy), ("Flare", 60, flare)]
rig.animation_data_create()
actions = []
for cname, nf, fn in CLIPS:
    act = bpy.data.actions.new(cname)
    act.use_fake_user = True
    rig.animation_data.action = act
    prevq = {}
    for f in list(range(0, nf, 2)) + [nf]:
        t = (f % nf) / nf if f < nf else 0.0  # último quadro = primeiro (loop sem salto)
        P = fn(t)
        for bn in [b.name for b in PB]:
            pb = PB[bn]
            loc, q = P.get(bn, (None, Quaternion()))
            if bn in prevq and prevq[bn].dot(q) < 0:
                q = -q
            prevq[bn] = q
            pb.rotation_mode = "QUATERNION"
            pb.rotation_quaternion = q
            pb.location = loc if loc is not None else Vector()
            pb.keyframe_insert("rotation_quaternion", frame=f)
            pb.keyframe_insert("location", frame=f)
    track = rig.animation_data.nla_tracks.new()
    track.name = cname
    track.strips.new(cname, 1, act)
    actions.append(act)
rig.animation_data.action = None
for b in PB:
    b.rotation_quaternion = Quaternion()
    b.location = Vector()

# ---------------------------------------------------------------- âncoras FX_* (empties presos a ossos)
FX = {
    "FX_Core": ("Body", core_c + Vector((0, 0.12, 0))),
    "FX_TailEmber": ("Body", TAIL_ROOT + Vector((0, -1.1, -0.6))),
    "FX_AuraWings": ("Body", Vector((0, -0.1, 3.0))),
    "FX_WingTip.R": ("Wing2.R", HAND + Vector((0.75, -0.25, 1.0))),
    "FX_WingTip.L": ("Wing2.L", mirror(HAND, -1) + Vector((-0.75, -0.25, 1.0))),
    "FX_Head": ("Head", hp((0, 1.2, 4.2))),
    "FX_Crest": ("Head", hp((0, 0.3, 4.95))),
    "FX_TailTip": ("Tail3_2", TAIL_ROOT + tail_dir(3) * TAIL_LEN[3] * 0.92),
}
for n, (bn, p) in FX.items():
    e = bpy.data.objects.new(n, None)
    e.empty_display_size = 0.15
    scene.collection.objects.link(e)
    e.parent = rig
    e.parent_type = "BONE"
    e.parent_bone = bn
    e.matrix_world = Matrix.Translation(p)

# ---------------------------------------------------------------- relatório e export
rep = []
for ob in (body, glow, eyes, eyecore):
    me = ob.data
    tris = sum(len(p.vertices) - 2 for p in me.polygons)
    rep.append(f"{ob.name}: {tris} tris, {len(me.vertices)} verts")
rep.append(f"ossos: {len(rig.data.bones)}")
rep.append("clipes: " + ", ".join(f"{a.name} {int(a.frame_range[1]-1)}q" for a in actions))
xs = [(body.matrix_world @ v.co) for v in body.data.vertices]
rep.append("bbox: x %.2f..%.2f y %.2f..%.2f z %.2f..%.2f" % (
    min(v.x for v in xs), max(v.x for v in xs), min(v.y for v in xs), max(v.y for v in xs),
    min(v.z for v in xs), max(v.z for v in xs)))
print("\n".join(rep))
open(os.path.join(OUT, "relatorio.txt"), "w").write("\n".join(rep) + "\n")

bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, NAME + ".blend"))
bpy.ops.object.select_all(action="SELECT")
bpy.ops.export_scene.gltf(filepath=os.path.join(OUT, NAME + ".glb"), export_format="GLB",
                          export_animation_mode="ACTIONS", export_force_sampling=True,
                          export_extras=False, export_yup=True, export_apply=False)
print("OK", OUT)
