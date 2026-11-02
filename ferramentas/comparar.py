#!/usr/bin/env python3
"""Monta a folha de comparação de um pet com os pets do Steal An Egg do mesmo degrau de raridade.

Uso (a partir da raiz do repositório):
    python ferramentas/comparar.py --pet "Kraken" --raridade legendary \
        --imagens print_frente.png print_34.png print_lado.png \
        [--lote outro1.png outro2.png] [--origem studio|blender] [--icone icone.png] [--efeitos] [--saida folha.png]

A folha tem três faixas, todas sobre o mesmo fundo neutro e na mesma altura:
  1. as vistas do pet (screenshot do Studio ou render);
  2. os 3 pets de comparação do Steal An Egg do degrau (Legendary = Secret/Eternal, Mythic = Divine)
     e, se houver, os outros pets do lote;
  3. todos em 128 px sobre fundo claro e escuro (teste do ícone de inventário).
Ela serve de prova para o revisor, que precisa abri-la (Read) antes de dar o veredito.
Ver "12 Modelos e pets/Pets lendarios e miticos/Regua Steal An Egg para os 21 pets.md".
"""

import argparse
from pathlib import Path
import sys

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SAE = ROOT / "recursos" / "Referencias de pets raros" / "Steal An Egg - pets recentes"
# Imagens-alvo finais (decisão do usuário, 31/10/2026): o pet tem que ficar extremamente parecido com elas.
ALVOS = ROOT / "recursos" / "Pets lendarios e miticos" / "Alvos finais"
# Primeiro os renders 3D do jogo (mais confiáveis), depois as ilustrações do site.
REFERENCIAS = {
    "legendary": ["pumpkin-golem", "graveyard-brute", "abomination-kong", "bloodbloom",
                  "grave-cerberus", "phantom-dragon", "pumpkin-brute"],
    "mythic": ["voidseer-pumpkin", "bone-emperor", "cursed-monarch-rainbow"],
}
DEGRAU = {"legendary": "Secret/Eternal", "mythic": "Divine"}
ALTURA = 360
OCUPACAO_ICONE = 0.88  # mesma ocupação do ícone padrão do render_pet.py, para comparar de igual para igual
FUNDO = (128, 132, 140)


def fonte(tam):
    for nome in ("DejaVuSans-Bold.ttf", "DejaVuSans.ttf", "arial.ttf"):
        try:
            return ImageFont.truetype(nome, tam)
        except OSError:
            continue
    return ImageFont.load_default()


def abrir(caminho):
    img = Image.open(caminho).convert("RGBA")
    caixa = img.getbbox()  # corta borda transparente
    return img.crop(caixa) if caixa else img


def na_altura(img, altura):
    escala = altura / img.height
    return img.resize((max(1, round(img.width * escala)), altura), Image.LANCZOS)


def faixa(titulo, itens, altura=ALTURA):
    """itens: lista de (rotulo, imagem RGBA)."""
    margem, rot = 16, 26
    pecas = [(r, na_altura(i, altura)) for r, i in itens]
    largura = margem + sum(p.width + margem for _, p in pecas)
    largura_titulo = margem * 2 + int(ImageDraw.Draw(Image.new("RGB", (1, 1))).textlength(titulo, font=fonte(20)))
    tela = Image.new("RGB", (max(largura, largura_titulo, 600), altura + rot * 2 + margem * 2), FUNDO)
    d = ImageDraw.Draw(tela)
    d.text((margem, 6), titulo, fill=(255, 255, 255), font=fonte(20))
    x = margem
    for rotulo, p in pecas:
        tela.paste(p, (x, rot + margem), p)
        d.text((x, rot + margem + altura + 4), rotulo, fill=(240, 240, 240), font=fonte(16))
        x += p.width + margem
    return tela


def faixa_icones(itens):
    margem, lado = 12, 128
    tela = Image.new("RGB", (margem + len(itens) * (lado + margem), 2 * lado + 3 * margem + 30), FUNDO)
    d = ImageDraw.Draw(tela)
    d.text((margem, 4), "Ícone 128 px — fundo claro / escuro", fill=(255, 255, 255), font=fonte(18))
    alvo = round(lado * OCUPACAO_ICONE)
    for n, (_, img) in enumerate(itens):
        if img.size == (lado, lado) and img.getpixel((0, 0))[3] == 0:
            icone = img  # ícone padrão do render_pet.py: já vem enquadrado, entra como está
        else:
            icone = ImageOps.contain(img.crop(img.getbbox() or (0, 0, *img.size)), (alvo, alvo), Image.LANCZOS)
        for linha, cor in enumerate(((235, 235, 235), (30, 32, 38))):
            x, y = margem + n * (lado + margem), 30 + margem + linha * (lado + margem)
            quadro = Image.new("RGB", (lado, lado), cor)
            quadro.paste(icone, ((lado - icone.width) // 2, (lado - icone.height) // 2), icone)
            tela.paste(quadro, (x, y))
    return tela


def empilhar(faixas):
    largura = max(f.width for f in faixas)
    folha = Image.new("RGB", (largura, sum(f.height for f in faixas)), FUNDO)
    y = 0
    for f in faixas:
        folha.paste(f, (0, y))
        y += f.height
    return folha


def achar_alvo(pet):
    """Imagem-alvo final do pet (ex.: "03_Molten_Dragon.webp" para "Molten Dragon"), ou None."""
    chave = pet.lower().replace(" ", "_")
    achados = [c for c in sorted(ALVOS.glob("*.*")) if c.stem.lower().split("_", 1)[-1] == chave]
    return achados[0] if achados else None


def faixa_alvo(pet, alvo_path, resultados, altura=560):
    """Alvo final e resultado(s) grandes, lado a lado, para julgar o critério 7."""
    itens = [(f"ALVO: {alvo_path.name}", abrir(alvo_path))] + list(resultados)
    return faixa(f"ALVO x RESULTADO — {pet}: tem que ficar extremamente parecido (critério 7)", itens, altura)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--pet", required=True, help="Nome do pet")
    p.add_argument("--raridade", required=True, choices=sorted(REFERENCIAS), help="legendary ou mythic")
    p.add_argument("--imagens", nargs="+", required=True, type=Path, help="Vistas do pet (frente, 3/4, lado...)")
    p.add_argument("--lote", nargs="*", default=[], type=Path, help="Uma imagem de cada outro pet do lote")
    p.add_argument("--refs", nargs="*", help="Trocar os pets de comparação (nomes dos arquivos, sem extensão)")
    p.add_argument("--origem", choices=("studio", "blender"), default="studio",
                   help="De onde vêm as vistas do pet: screenshot do Roblox Studio ou render do Blender")
    p.add_argument("--icone", type=Path, help="Ícone de inventário do pet para a faixa de 128 px (padrão: a primeira vista)")
    p.add_argument("--efeitos", action="store_true", help="Marca no título que as vistas estão com os efeitos ligados")
    p.add_argument("--alvo", type=Path, help="Imagem-alvo final (padrão: a de Alvos finais com o nome do pet)")
    p.add_argument("--saida", type=Path)
    a = p.parse_args()

    faltando = [str(c) for c in [*a.imagens, *a.lote, *([a.icone] if a.icone else [])] if not c.is_file()]
    if faltando:
        sys.exit("Imagem não encontrada: " + ", ".join(faltando))
    nomes = a.refs or REFERENCIAS[a.raridade][:3]
    refs = []
    for nome in nomes:
        achados = sorted(SAE.glob(nome + ".*"))
        if not achados:
            sys.exit(f"Referência do Steal An Egg não encontrada no repositório: {nome}")
        refs.append((f"SAE {nome}", abrir(achados[0])))

    pet = [(f"{a.pet} — vista {n + 1}", abrir(c)) for n, c in enumerate(a.imagens)]
    lote = [(c.stem, abrir(c)) for c in a.lote]
    origem = "screenshot do Roblox Studio" if a.origem == "studio" else "render do Blender (não é o jogo)"
    alvo_path = a.alvo or achar_alvo(a.pet)
    topo = []
    if alvo_path and alvo_path.is_file():
        n = min(1, len(pet) - 1)  # a vista de 3/4, como nas imagens-alvo
        topo = [faixa_alvo(a.pet, alvo_path, [(f"resultado: {pet[n][0]}", pet[n][1])])]
    else:
        print(f"AVISO: sem imagem-alvo para '{a.pet}' em {ALVOS}; a folha sai sem a faixa do critério 7", file=sys.stderr)
    folha = empilhar(topo + [
        faixa(f"{a.pet} ({a.raridade.title()}) — {origem}" + (" — com efeitos" if a.efeitos else " — sem efeitos"), pet),
        faixa(f"Comparação: Steal An Egg {DEGRAU[a.raridade]}" + (" + outros pets do lote" if lote else ""),
              refs + lote),
        faixa_icones([(a.pet, Image.open(a.icone).convert("RGBA")) if a.icone else pet[0], *refs, *lote]),
    ])
    saida = a.saida or a.imagens[0].with_name(f"{a.pet.replace(' ', '')}_comparacao.png")
    folha.save(saida)
    print(f"{saida}  ({folha.width}x{folha.height}; referências: {', '.join(nomes)})")


if __name__ == "__main__":
    main()
