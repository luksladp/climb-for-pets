#!/usr/bin/env python3
"""Uma rodada de um pet num comando só: build das variantes em paralelo, render padrão, checagem e folha.

Uso (a partir de jogos/; precisa de `pip install bpy pillow numpy scipy scikit-image`):
    python .framework/rodada.py --pet "Lava Titan" --rodada 18 [--variantes A B C] [--modo rapido|final] \
        [--pior 1,2] [--efeitos] [--sem-build]
    python .framework/rodada.py --pet "Lava Titan" --rodada 18 --aplicar B     # guarda a variante escolhida

O que faz, para cada variante (VARIANTE=A, B... no ambiente do build; sem --variantes, uma só, "base"):
  1. roda os comandos de build do `rodada.json` do pet, cada variante na sua pasta de trabalho;
  2. renderiza com o kit único (`render_pet.py`): frente, 3/4, lado e ícone padrão;
  3. roda a checagem (`checar.py`) contra a rodada anterior (o GLB e as vistas guardados na pasta do pet);
  4. monta a folha: com uma variante, a folha de comparação normal (`comparar.py`); com várias, a folha de
     variantes, uma linha por variante, ao lado do SAE do degrau e dos outros pets do lote no mesmo render;
  5. escreve `resumo.md` com tempos, checagem e caminhos.
Com --efeitos (ou --modo final) também gera as vistas com efeitos pelo script do pet e a folha com efeitos.

--aplicar copia a variante escolhida para a pasta do pet (GLB, vistas, ícone e os arquivos de "copiar"), e ela
passa a ser a "rodada anterior" da próxima. Quem escolhe é o revisor, na folha de variantes.

O `rodada.json` fica em `Recursos/Pets lendarios e miticos/<Pet>/` e diz como montar o pet:
    {"raridade": "legendary", "lote": ["Volcanic Phoenix", "Molten Dragon"], "glb": "LavaTitan.glb",
     "build": [["python3", "{fonte}/build_v3.py", "--out", "{saida}"]],
     "efeitos": [[...]], "efeitos_vistas": "{saida}/fx/{vista}_fx.png", "copiar": ["LavaTitan_paleta.png"]}
Cada variante ganha a própria cópia de `fonte/` (e um atalho para `vfx/`) dentro da pasta de trabalho; os
comandos rodam dentro dessa cópia, com OUT={saida} e VARIANTE no ambiente. {fonte} aponta para a cópia.
Ver "12 Modelos e pets/Pets lendarios e miticos/Processo rapido de rodada.md".
"""

import argparse
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

FW = Path(__file__).resolve().parent
ROOT = FW.parent
PETS = ROOT / "Recursos" / "Pets lendarios e miticos"
TRABALHO = ROOT / ".rodadas"
VISTAS = ("frente", "tres_quartos", "lado")
PY = sys.executable


def carregar_comparar():
    spec = importlib.util.spec_from_file_location("comparar", FW / "comparar.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def preencher(cmd, **kw):
    return [str(c).format(**kw) for c in cmd]


def rodar(cmd, cwd, env, log):
    t = time.time()
    with open(log, "a") as f:
        f.write("$ " + " ".join(cmd) + "\n")
        f.flush()
        r = subprocess.run(cmd, cwd=cwd, env=env, stdout=f, stderr=subprocess.STDOUT)
    if r.returncode:
        raise RuntimeError(f"falhou ({r.returncode}): {' '.join(cmd)} — veja {log}")
    return time.time() - t


def render(glb, saida, modo, log):
    return rodar([PY, str(FW / "render_pet.py"), "--glb", str(glb), "--saida", str(saida), "--modo", modo],
                 ROOT, os.environ.copy(), log)


def vistas_do_lote(nome, modo):
    """3/4 do outro pet do lote no mesmo render: usa <Pet>/vistas/ se existir, senão renderiza o GLB guardado."""
    pasta = PETS / nome
    if (pasta / "vistas" / "tres_quartos.png").is_file():
        return pasta / "vistas" / "tres_quartos.png"
    cfg = json.loads((pasta / "rodada.json").read_text())
    glb = pasta / cfg["glb"]
    cache = TRABALHO / "_lote" / nome / f"{int(glb.stat().st_mtime)}_{glb.stat().st_size}"
    if not (cache / "tres_quartos.png").is_file():
        cache.mkdir(parents=True, exist_ok=True)
        render(glb, cache, modo, cache / "render.log")
    return cache / "tres_quartos.png"


def folha_variantes(cmp, pet, raridade, variantes, lote, saida):
    faixas = []
    alvo = cmp.achar_alvo(pet)
    if alvo:  # critério 7: cada variante (3/4) ao lado da imagem-alvo final
        faixas.append(cmp.faixa_alvo(pet, alvo, [(f"variante {n}", cmp.abrir(p / "tres_quartos.png"))
                                                for n, p in variantes], 420))
    icones = []
    for nome, pasta in variantes:
        itens = [(f"{nome} — vista {i + 1}", cmp.abrir(pasta / f"{v}.png")) for i, v in enumerate(VISTAS)]
        faixas.append(cmp.faixa(f"{pet} — variante {nome} — render do Blender (não é o jogo) — sem efeitos", itens, 300))
        icones.append((nome, cmp.Image.open(pasta / "icone_128.png").convert("RGBA")))
    refs = []
    for n in cmp.REFERENCIAS[raridade][:3]:
        refs.append((f"SAE {n}", cmp.abrir(sorted(cmp.SAE.glob(n + ".*"))[0])))
    lote_it = [(p.stem, cmp.abrir(p)) for p in lote]
    faixas.append(cmp.faixa(f"Comparação: Steal An Egg {cmp.DEGRAU[raridade]} + outros pets do lote", refs + lote_it))
    faixas.append(cmp.faixa_icones(icones + refs + lote_it))
    cmp.empilhar(faixas).save(saida)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--pet", required=True)
    p.add_argument("--rodada", required=True, type=int)
    p.add_argument("--variantes", nargs="*", default=[])
    p.add_argument("--modo", choices=("rapido", "final"), default="rapido")
    p.add_argument("--pior", default="", help="Critérios PIOR da rodada anterior (ex.: 1,6)")
    p.add_argument("--efeitos", action="store_true", help="Também gera as vistas e a folha com efeitos")
    p.add_argument("--sem-build", action="store_true", help="Não monta: usa o GLB guardado do pet (para testar o kit)")
    p.add_argument("--aplicar", metavar="VARIANTE", help="Guarda a variante escolhida na pasta do pet")
    a = p.parse_args()

    pasta = PETS / a.pet
    cfg = json.loads((pasta / "rodada.json").read_text())
    tag = a.pet.replace(" ", "")
    trab = TRABALHO / a.pet / f"rodada{a.rodada}"
    variantes = a.variantes or ["base"]

    if a.aplicar:
        origem = trab / a.aplicar
        if not origem.is_dir():
            sys.exit(f"Variante não encontrada: {origem}")
        shutil.copy2(origem / Path(cfg["glb"]).name, pasta / cfg["glb"])
        (pasta / "vistas").mkdir(exist_ok=True)
        for f in (origem / "vistas").glob("*.png"):
            if f.name != "icone_render.png":
                shutil.copy2(f, pasta / "vistas" / f.name)
        for rel in cfg.get("copiar", []):
            src = origem / rel
            if src.is_dir():
                shutil.copytree(src, pasta / rel, dirs_exist_ok=True)
            elif src.is_file():
                shutil.copy2(src, pasta / rel)
        print(f"Variante {a.aplicar} guardada em {pasta} (GLB, vistas, ícone e {len(cfg.get('copiar', []))} itens de 'copiar').")
        return

    t0 = time.time()
    trab.mkdir(parents=True, exist_ok=True)
    tempos = {}

    # rodada anterior: o que está guardado na pasta do pet
    anterior_glb = pasta / cfg["glb"]
    anterior_vistas = pasta / "vistas"
    if not (anterior_vistas / "frente.png").is_file():
        anterior_vistas = trab / "anterior"
        anterior_vistas.mkdir(exist_ok=True)
        tempos["render da rodada anterior"] = render(anterior_glb, anterior_vistas, "rapido", trab / "anterior.log")

    def build(var):
        saida = trab / var
        if saida.exists():
            shutil.rmtree(saida)
        (saida / "fx").mkdir(parents=True)
        # cópia própria dos scripts para cada variante: um build não pisa nos arquivos do outro
        shutil.copytree(pasta / "fonte", saida / "fonte", ignore=shutil.ignore_patterns("__pycache__"))
        if (pasta / "vfx").is_dir():
            (saida / "vfx").symlink_to(pasta / "vfx", target_is_directory=True)
        log = saida / "build.log"
        if a.sem_build:
            shutil.copy2(anterior_glb, saida / Path(cfg["glb"]).name)
            return 0.0
        env = os.environ.copy()
        env.update(OUT=str(saida), VARIANTE=var)
        t = 0.0
        for cmd in cfg["build"]:
            t += rodar(preencher(cmd, fonte=saida / "fonte", saida=saida), saida / "fonte", env, log)
        return t

    t = time.time()
    with ThreadPoolExecutor(max_workers=min(len(variantes), 3)) as ex:
        res = dict(zip(variantes, ex.map(build, variantes)))
    tempos["build (variantes em paralelo)"] = time.time() - t

    resultados = {}
    for var in variantes:
        saida = trab / var
        glb = saida / Path(cfg["glb"]).name
        if not glb.is_file():
            achados = sorted(saida.glob("*.glb"))
            if not achados:
                sys.exit(f"O build da variante {var} não gerou GLB em {saida}")
            glb = achados[0]
            shutil.copy2(glb, saida / Path(cfg["glb"]).name)
            glb = saida / Path(cfg["glb"]).name
        tempos[f"render {var}"] = render(glb, saida / "vistas", a.modo, saida / "render.log")
        if a.efeitos or a.modo == "final":
            if cfg.get("efeitos"):
                env = os.environ.copy()
                env.update(OUT=str(saida), VARIANTE=var)
                t = time.time()
                for cmd in cfg["efeitos"]:
                    rodar(preencher(cmd, fonte=saida / "fonte", saida=saida, glb=glb, vfx=pasta / "vfx"),
                          saida / "fonte", env, saida / "efeitos.log")
                tempos[f"efeitos {var}"] = time.time() - t
        cmd = [PY, str(FW / "checar.py"), "--pet", a.pet, "--raridade", cfg["raridade"], "--glb", str(glb),
               "--vistas", str(saida / "vistas"), "--anterior-glb", str(anterior_glb),
               "--anterior-vistas", str(anterior_vistas), "--json", str(saida / "checagem.json")]
        if a.pior:
            cmd += ["--pior", a.pior]
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        (saida / "checagem.md").write_text(r.stdout + r.stderr)
        resultados[var] = {"bloqueada": r.returncode != 0, "checagem": r.stdout}

    t = time.time()
    lote = []
    (trab / "lote").mkdir(exist_ok=True)
    for n in cfg.get("lote", []):
        destino = trab / "lote" / (n.replace(" ", "") + ".png")
        shutil.copy2(vistas_do_lote(n, "rapido"), destino)
        lote.append(destino)
    tempos["vistas do lote"] = time.time() - t

    cmp = carregar_comparar()
    (pasta / "folhas").mkdir(exist_ok=True)
    folhas = []
    if len(variantes) == 1:
        v = trab / variantes[0] / "vistas"
        saida = pasta / "folhas" / f"{tag}_comparacao_rodada{a.rodada}.png"
        base = [PY, str(FW / "comparar.py"), "--pet", a.pet, "--raridade", cfg["raridade"],
                "--origem", "blender", "--icone", str(v / "icone_128.png"), "--lote", *map(str, lote)]
        subprocess.run(base + ["--imagens", *[str(v / f"{x}.png") for x in VISTAS], "--saida", str(saida)],
                       cwd=ROOT, check=True)
        folhas.append(saida)
        padrao = cfg.get("efeitos_vistas")
        if padrao and (a.efeitos or a.modo == "final"):
            fx = [Path(padrao.format(saida=trab / variantes[0], vista=x)) for x in VISTAS]
            if all(f.is_file() for f in fx):
                saida_fx = pasta / "folhas" / f"{tag}_comparacao_fx_rodada{a.rodada}.png"
                subprocess.run(base + ["--efeitos", "--imagens", *map(str, fx), "--saida", str(saida_fx)],
                               cwd=ROOT, check=True)
                folhas.append(saida_fx)
    else:
        saida = pasta / "folhas" / f"{tag}_variantes_rodada{a.rodada}.png"
        folha_variantes(cmp, a.pet, cfg["raridade"], [(v, trab / v / "vistas") for v in variantes], lote, saida)
        folhas.append(saida)

    tempos["total"] = time.time() - t0
    linhas = [f"# {a.pet} — rodada {a.rodada} ({a.modo})", "",
              "Folhas: " + ", ".join(f"`{f.relative_to(ROOT)}`" for f in folhas), "",
              "| Etapa | Segundos |", "| --- | --- |"]
    linhas += [f"| {k} | {v:.0f} |" for k, v in tempos.items()]
    for var, r in resultados.items():
        linhas += ["", f"## Variante {var}: {'BLOQUEADA' if r['bloqueada'] else 'pode ir ao revisor'}", "", r["checagem"]]
    (trab / "resumo.md").write_text("\n".join(linhas))
    print("\n".join(linhas))
    print(f"\nResumo em {trab / 'resumo.md'}")


if __name__ == "__main__":
    main()
