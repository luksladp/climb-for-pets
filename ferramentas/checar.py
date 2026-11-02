#!/usr/bin/env python3
"""Checagem automática de um pet antes do revisor: mede em segundos o que dá para medir.

Uso (a partir de jogos/; precisa de `pip install numpy pillow scipy`):
    python .framework/checar.py --pet "Lava Titan" --raridade legendary --glb <pet.glb> --vistas <pasta> \
        [--anterior-glb <rodada_anterior.glb>] [--anterior-vistas <pasta>] [--pior 1,6] [--json saida.json]

--vistas é a pasta do render_pet.py (frente.png, tres_quartos.png, lado.png, icone_128.png).
--pior são os critérios da régua que deram PIOR na rodada anterior. Com eles, a checagem exige que a forma
tenha mudado (regra do usuário de 31/10/2026) e, se o critério 1 deu PIOR, que o pet tenha as famílias de cor
e material do SAE do degrau.

Cada linha sai como OK, AVISO ou BLOQUEIA. Com algum BLOQUEIA o código de saída é 1 e a rodada não vai ao
revisor. A checagem é um filtro: passar nela não aprova nada, quem aprova é o revisor.
Ver "12 Modelos e pets/Pets lendarios e miticos/Processo rapido de rodada.md".
"""

import argparse
import json
import struct
import sys
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SAE = ROOT / "Recursos" / "Referencias de pets raros" / "Steal An Egg - pets recentes"
SAE_DEGRAU = {
    "legendary": ["pumpkin-golem", "graveyard-brute", "abomination-kong", "bloodbloom",
                  "grave-cerberus", "phantom-dragon", "pumpkin-brute"],
    "mythic": ["voidseer-pumpkin", "bone-emperor", "cursed-monarch-rainbow"],
}
MAX_TRIS, MAX_TEX = 20000, 1024
ICONE_OCUPACAO = (0.84, 0.92)          # padrão do lote: 88% do lado maior
FORMA_MIN = 0.003                       # deslocamento médio mínimo (fração da altura) para contar como forma nova
SILHUETA_MAX_IOU = 0.99                 # silhueta igual acima disso
FUNDO_ESCURO = np.array([30, 32, 38]) / 255
LUMA = np.array([0.2126, 0.7152, 0.0722])

# ---------------------------------------------------------------- GLB


def ler_glb(caminho):
    b = Path(caminho).read_bytes()
    if b[:4] != b"glTF":
        sys.exit(f"Não é um GLB: {caminho}")
    n = struct.unpack("<I", b[12:16])[0]
    j = json.loads(b[20:20 + n])
    bin_ = b""
    off = 20 + n
    if off < len(b):
        m = struct.unpack("<I", b[off:off + 4])[0]
        bin_ = b[off + 8:off + 8 + m]
    return j, bin_


TIPOS = {5120: np.int8, 5121: np.uint8, 5122: np.int16, 5123: np.uint16, 5125: np.uint32, 5126: np.float32}
COMP = {"SCALAR": 1, "VEC2": 2, "VEC3": 3, "VEC4": 4, "MAT4": 16}


def acessor(j, bin_, i):
    a = j["accessors"][i]
    bv = j["bufferViews"][a["bufferView"]]
    tipo, comp = np.dtype(TIPOS[a["componentType"]]), COMP[a["type"]]
    ini = bv.get("byteOffset", 0) + a.get("byteOffset", 0)
    passo = bv.get("byteStride", tipo.itemsize * comp)
    if passo == tipo.itemsize * comp:
        return np.frombuffer(bin_, tipo, a["count"] * comp, ini).reshape(a["count"], comp)
    linhas = [np.frombuffer(bin_, tipo, comp, ini + k * passo) for k in range(a["count"])]
    return np.stack(linhas)


def matriz_no(no):
    if "matrix" in no:
        return np.array(no["matrix"], dtype=float).reshape(4, 4).T
    t = np.array(no.get("translation", [0, 0, 0]), dtype=float)
    x, y, z, w = no.get("rotation", [0, 0, 0, 1])
    r = np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
                  [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
                  [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])
    s = np.array(no.get("scale", [1, 1, 1]), dtype=float)
    m = np.eye(4)
    m[:3, :3] = r * s
    m[:3, 3] = t
    return m


def malhas(j, bin_):
    """Por malha: triângulos e vértices no espaço do modelo (malha com pele: pose de ligação, como no glTF)."""
    pais = {}
    for i, no in enumerate(j.get("nodes", [])):
        for f in no.get("children", []):
            pais[f] = i

    def mundo(i):
        m = matriz_no(j["nodes"][i])
        while i in pais:
            i = pais[i]
            m = matriz_no(j["nodes"][i]) @ m
        return m

    out = {}
    for i, no in enumerate(j.get("nodes", [])):
        if "mesh" not in no:
            continue
        me = j["meshes"][no["mesh"]]
        nome = me.get("name") or no.get("name") or f"malha{no['mesh']}"
        m = np.eye(4) if "skin" in no else mundo(i)
        tris, pts = 0, []
        for pr in me["primitives"]:
            pos = acessor(j, bin_, pr["attributes"]["POSITION"]).astype(float)
            pts.append(pos @ m[:3, :3].T + m[:3, 3])
            n = j["accessors"][pr["indices"]]["count"] if "indices" in pr else len(pos)
            tris += n // 3
        d = out.setdefault(nome, {"tris": 0, "pts": []})
        d["tris"] += tris
        d["pts"].extend(pts)
    for d in out.values():
        d["pts"] = np.concatenate(d["pts"])
    return out


def texturas(j, bin_):
    tam = []
    for i, im in enumerate(j.get("images", [])):
        if "bufferView" not in im:
            continue
        bv = j["bufferViews"][im["bufferView"]]
        dados = bin_[bv.get("byteOffset", 0):bv.get("byteOffset", 0) + bv["byteLength"]]
        try:
            from io import BytesIO
            w, h = Image.open(BytesIO(dados)).size
            tam.append((im.get("name") or f"imagem{i}", w, h))
        except Exception:
            pass
    return tam

# ---------------------------------------------------------------- imagens


def abrir(caminho, lado=400):
    im = Image.open(caminho).convert("RGBA")
    caixa = im.getbbox()
    if caixa:
        im = im.crop(caixa)
    im.thumbnail((lado, lado))
    return np.asarray(im).astype(float) / 255


def familias(a, minimo=0.06):
    """Famílias de cor e material visíveis: faixas de matiz de 30° com pelo menos 6% da área do pet,
    mais 1 para o conjunto neutro (cinza, preto, branco). Sombra e luz do mesmo material não contam duas vezes."""
    m = a[..., 3] > 0.5
    rgb = a[..., :3][m]
    mx, mn = rgb.max(1), rgb.min(1)
    s = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
    r, g, b = rgb.T
    d = np.maximum(mx - mn, 1e-6)
    h = np.where(mx == r, ((g - b) / d) % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) * 60
    chave = np.where(s < 0.2, -1, (h // 30).astype(int))
    u, c = np.unique(chave, return_counts=True)
    f = c / c.sum()
    return int((f >= minimo).sum())


def visivel_no_escuro(a):
    m = a[..., 3] > 0.5
    lum = a[..., :3][m] @ LUMA
    return float((lum > FUNDO_ESCURO @ LUMA + 0.12).mean())


def silhueta(caminho, lado=256):
    im = Image.open(caminho).convert("RGBA")
    caixa = im.getbbox()
    im = im.crop(caixa) if caixa else im
    q = Image.new("L", (lado, lado), 0)
    a = im.getchannel("A")
    a.thumbnail((lado, lado))
    q.paste(a, ((lado - a.width) // 2, lado - a.height))
    return np.asarray(q) > 127


def halo(alfa):
    """Fração de pixels semitransparentes a mais de 1 px da parte opaca (halo ou contorno pintado)."""
    from scipy.ndimage import binary_dilation
    opaco = alfa > 200
    perto = binary_dilation(opaco, iterations=1)
    fora = (alfa > 20) & ~perto
    return float(fora.sum() / max(opaco.sum(), 1))

# ---------------------------------------------------------------- checagem


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--pet", required=True)
    p.add_argument("--raridade", required=True, choices=sorted(SAE_DEGRAU))
    p.add_argument("--glb", required=True, type=Path)
    p.add_argument("--vistas", required=True, type=Path)
    p.add_argument("--anterior-glb", type=Path)
    p.add_argument("--anterior-vistas", type=Path)
    p.add_argument("--pior", default="", help="Critérios PIOR da rodada anterior, ex.: 1,6")
    p.add_argument("--json", type=Path)
    a = p.parse_args()
    pior = {int(x) for x in a.pior.replace(" ", "").split(",") if x}
    linhas = []

    def linha(estado, item, valor, regra):
        linhas.append({"estado": estado, "item": item, "valor": valor, "regra": regra})

    j, bin_ = ler_glb(a.glb)
    ms = malhas(j, bin_)
    todos = np.concatenate([d["pts"] for d in ms.values()])
    altura = float(np.ptp(todos[:, 1])) or 1.0          # glTF: Y para cima

    # 1. limites do jogo
    maior = max(ms.items(), key=lambda kv: kv[1]["tris"])
    linha("OK" if maior[1]["tris"] <= MAX_TRIS else "BLOQUEIA", "Triângulos por malha",
          f"maior: {maior[0]} {maior[1]['tris']}", f"até {MAX_TRIS}")
    tex = texturas(j, bin_)
    grande = [t for t in tex if max(t[1], t[2]) > MAX_TEX]
    linha("OK" if not grande else "BLOQUEIA", "Texturas",
          ", ".join(f"{n} {w}x{h}" for n, w, h in tex) or "nenhuma", f"até {MAX_TEX}²")
    clipes = [x.get("name", "") for x in j.get("animations", [])]
    tem = lambda *ns: any(c.lower() in ns for c in clipes)
    ok_clip = tem("idle") and tem("walk", "fly", "swim") and tem("happy") and len(clipes) >= 4
    linha("OK" if ok_clip else "BLOQUEIA", "Clipes", ", ".join(clipes) or "nenhum",
          "Idle, Walk/Fly/Swim, Happy e 1 especial")

    # 2. ícone padrão
    icone = a.vistas / "icone_128.png"
    if icone.is_file():
        ic = Image.open(icone).convert("RGBA")
        alfa = np.asarray(ic)[..., 3]
        cantos = [alfa[0, 0], alfa[0, -1], alfa[-1, 0], alfa[-1, -1]]
        ys, xs = np.nonzero(alfa > 20)
        ocup = max(np.ptp(xs) + 1, np.ptp(ys) + 1) / max(ic.size)
        margem = min(xs.min(), ys.min(), ic.width - 1 - xs.max(), ic.height - 1 - ys.max())
        ok = ic.size == (128, 128) and max(cantos) == 0 and ICONE_OCUPACAO[0] <= ocup <= ICONE_OCUPACAO[1] and margem >= 2
        linha("OK" if ok else "BLOQUEIA", "Ícone: tamanho, fundo e ocupação",
              f"{ic.width}x{ic.height}, cantos {'transparentes' if max(cantos) == 0 else 'opacos'}, "
              f"ocupa {ocup:.0%}, margem {margem} px",
              "128x128, fundo transparente, 84–92% do lado maior, sem tocar a borda")
        hl = halo(alfa)
        linha("OK" if hl < 0.03 else "BLOQUEIA", "Ícone sem halo nem contorno pintado", f"{hl:.1%} da área",
              "menos de 3% de pixels semitransparentes fora da silhueta")
        esc = visivel_no_escuro(np.asarray(ic).astype(float) / 255)
        refs = [visivel_no_escuro(abrir(next(SAE.glob(n + ".*")))) for n in SAE_DEGRAU[a.raridade]]
        linha("OK" if esc >= min(refs) else "AVISO", "Ícone visível no fundo escuro", f"{esc:.0%} do pet",
              f"SAE do degrau: {min(refs):.0%} a {max(refs):.0%}")
    else:
        linha("BLOQUEIA", "Ícone", "icone_128.png não encontrado", "o render_pet.py gera o ícone padrão")

    # 3. famílias de cor e material (critério 1, "um material só")
    frente = a.vistas / "frente.png"
    if frente.is_file():
        fam = familias(abrir(frente))
        refs = sorted(familias(abrir(next(SAE.glob(n + ".*")))) for n in SAE_DEGRAU[a.raridade])
        mediana = refs[len(refs) // 2]
        estado = "OK" if fam >= mediana else ("BLOQUEIA" if 1 in pior else "AVISO")
        linha(estado, "Famílias de cor e material (vista de frente)", str(fam),
              f"mediana do SAE do degrau: {mediana} (de {refs[0]} a {refs[-1]}); bloqueia se o critério 1 deu PIOR")

    # 4. a forma mudou? (regra: todo PIOR muda a forma)
    if a.anterior_glb:
        from scipy.spatial import cKDTree
        ja, ba = ler_glb(a.anterior_glb)
        ant = malhas(ja, ba)
        rng = np.random.default_rng(0)
        mudancas = []
        for nome, d in ms.items():
            if nome not in ant:
                mudancas.append(f"{nome} (nova)")
                continue
            p0, p1 = ant[nome]["pts"], d["pts"]
            amostra = p1[rng.choice(len(p1), min(len(p1), 8000), replace=False)]
            dist = cKDTree(p0).query(amostra)[0].mean() / altura
            amostra0 = p0[rng.choice(len(p0), min(len(p0), 8000), replace=False)]
            dist = max(dist, cKDTree(p1).query(amostra0)[0].mean() / altura)
            if dist >= FORMA_MIN:
                mudancas.append(f"{nome} {dist:.1%}")
        mudancas += [f"{n} (saiu)" for n in ant if n not in ms]
        ious = {}
        if a.anterior_vistas:
            for v in ("frente", "tres_quartos", "lado"):
                f0, f1 = a.anterior_vistas / f"{v}.png", a.vistas / f"{v}.png"
                if f0.is_file() and f1.is_file():
                    s0, s1 = silhueta(f0), silhueta(f1)
                    ious[v] = float((s0 & s1).sum() / max((s0 | s1).sum(), 1))
        silhueta_mudou = any(x < SILHUETA_MAX_IOU for x in ious.values())
        mudou = bool(mudancas) or silhueta_mudou
        estado = "OK" if mudou else ("BLOQUEIA" if pior else "AVISO")
        valor = ("malhas que mudaram: " + "; ".join(mudancas) if mudancas else "nenhuma malha mudou") + \
            ("; silhueta (IoU) " + ", ".join(f"{k} {x:.3f}" for k, x in ious.items()) if ious else "")
        linha(estado, "A forma mudou desde a rodada anterior", valor,
              f"deslocamento médio ≥ {FORMA_MIN:.1%} da altura em alguma malha, ou silhueta com IoU < {SILHUETA_MAX_IOU}; "
              "bloqueia se houve PIOR (trocar só cor, tom ou brilho não conta)")
    elif pior:
        linha("BLOQUEIA", "A forma mudou desde a rodada anterior", "sem --anterior-glb",
              "com PIOR na rodada anterior, a comparação com ela é obrigatória")

    bloqueios = [x for x in linhas if x["estado"] == "BLOQUEIA"]
    print(f"Checagem — {a.pet} ({a.raridade})\n")
    print("| Estado | Item | Medido | Regra |\n| --- | --- | --- | --- |")
    for x in linhas:
        print(f"| {x['estado']} | {x['item']} | {x['valor']} | {x['regra']} |")
    print("\nResultado:", "BLOQUEADA — corrigir antes do revisor" if bloqueios else "pode ir ao revisor")
    if a.json:
        a.json.write_text(json.dumps({"pet": a.pet, "linhas": linhas, "bloqueada": bool(bloqueios)},
                                     ensure_ascii=False, indent=2))
    sys.exit(1 if bloqueios else 0)


if __name__ == "__main__":
    main()
