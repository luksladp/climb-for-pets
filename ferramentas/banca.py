#!/usr/bin/env python3
"""Junta os vereditos da banca de 3 revisores num veredito só, por maioria em cada critério.

Uso (a partir da raiz do repositório):
    python ferramentas/banca.py --vereditos r1.md r2.md r3.md [--travar 2,3,5 --anterior consolidado_anterior.md] \
        [--saida consolidado.md]

Cada arquivo é a resposta de um revisor, com a tabela da régua:
    | 1 Nível do degrau | IGUAL | pumpkin-golem | o que se vê na folha |
Para cada critério vale o veredito da maioria (2 de 3). Sem maioria (três vereditos diferentes), vale PIOR.
INCONCLUSIVO de qualquer revisor pede folha nova para aquele critério.

--travar: critérios que ficam como estavam no consolidado anterior, porque a parte deles não mudou (a checagem
mostrou que a forma, as vistas ou o ícone são os mesmos). Use só quando o `checar.py` confirmar que nada daquela
parte mudou; o revisor continua julgando todos os critérios, mas o voto dele nesses não muda o resultado.
APROVADO só se nenhum critério consolidado for PIOR.
Ver "12 Modelos e pets/Pets lendarios e miticos/Processo rapido de rodada.md".
"""

import argparse
import re
from collections import Counter
from pathlib import Path

VALORES = ("MELHOR", "IGUAL", "PIOR", "INCONCLUSIVO")
LINHA = re.compile(r"^\|\s*([1-7])\b[^|]*\|\s*\**\s*(MELHOR|IGUAL|PIOR|INCONCLUSIVO)\s*\**\s*\|(.*)$", re.I)


def ler(caminho):
    out = {}
    for linha in Path(caminho).read_text().splitlines():
        m = LINHA.match(linha.strip())
        if m and int(m.group(1)) not in out:
            resto = [c.strip() for c in m.group(3).split("|")]
            out[int(m.group(1))] = (m.group(2).upper(), resto[0] if resto else "", resto[1] if len(resto) > 1 else "")
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--vereditos", nargs=3, required=True, type=Path)
    p.add_argument("--travar", default="")
    p.add_argument("--anterior", type=Path)
    p.add_argument("--saida", type=Path)
    a = p.parse_args()
    tabelas = [ler(v) for v in a.vereditos]
    for v, t in zip(a.vereditos, tabelas):
        faltam = sorted(set(range(1, 8)) - set(t))
        if faltam:
            raise SystemExit(f"{v}: faltam os critérios {faltam} na tabela")
    travar = {int(x) for x in a.travar.replace(" ", "").split(",") if x}
    anterior = ler(a.anterior) if (travar and a.anterior) else {}
    if travar and not anterior:
        raise SystemExit("--travar precisa de --anterior com o consolidado da rodada anterior")
    nomes = {1: "Nível do degrau", 2: "Coerência com o lote", 3: "Escada de raridade",
             4: "Brilho só onde importa", 5: "Paleta da área", 6: "Ícone 128 px", 7: "Fiel à imagem-alvo"}
    linhas = ["| Critério | Consolidado | Votos | Comparado com | O que se vê na folha |", "| --- | --- | --- | --- | --- |"]
    resultado = {}
    for c in range(1, 8):
        votos = [t[c][0] for t in tabelas]
        if c in travar:
            final, nota = anterior[c][0], "travado (parte não mudou)"
        elif "INCONCLUSIVO" in votos:
            final, nota = "INCONCLUSIVO", "refazer a folha"
        else:
            topo, n = Counter(votos).most_common(1)[0]
            final, nota = (topo, "maioria") if n >= 2 else ("PIOR", "sem maioria: vale PIOR")
        resultado[c] = final
        apoio = next((t[c] for t in tabelas if t[c][0] == final), tabelas[0][c])
        linhas.append(f"| {c} {nomes[c]} | {final} | {' / '.join(votos)} ({nota}) | {apoio[1]} | {apoio[2]} |")
    piores = [c for c, v in resultado.items() if v == "PIOR"]
    inconc = [c for c, v in resultado.items() if v == "INCONCLUSIVO"]
    if inconc:
        veredito = f"INCONCLUSIVO — refazer a folha (critérios {', '.join(map(str, inconc))})"
    elif piores:
        veredito = f"REPROVADO ({len(piores)} PIOR: {', '.join(map(str, piores))})"
    else:
        veredito = "APROVADO (nenhum critério PIOR)"
    texto = "\n".join([f"**Banca de 3 revisores: {veredito}**", ""] + linhas) + "\n"
    if a.saida:
        a.saida.write_text(texto)
    print(texto)


if __name__ == "__main__":
    main()
