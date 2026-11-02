---
area: projeto
tipo: estado
resumo: Estado do Climb for Pets no repositório e lista do que ainda está fora dele (zip e pasta do projeto) e precisa ser trazido para valer como referência.
termos: climb for pets +1 estado processo rapido rodada referencias migracao pasta do projeto zip pets lendarios miticos remake
---
# Climb for Pets

Registrado em 30/10/2026. Regra: só vale como referência o que está neste repositório, na `main` (ver `CLAUDE.md` na raiz).

## O que já está no repositório

- **Na `main`:** os padrões gerais do vault, `12 Modelos e pets/Modelo 3D a partir de imagem.md` e
  `13 Animacao efeitos e som/VFX do HTML para o Roblox.md`.
- **Em pull requests abertos** (ainda não contam para outras conversas até serem mesclados):
  - #5 — referências de raridade, mutações e ovos (Steal An Egg) e pets de Halloween do Adopt Me;
  - #6 — fichas de remake dos 21 pets Lendários e Míticos das áreas 4–10, com alvo 2D e render atual reduzidos;
  - #7 — gerador do Gingerbread Golem v2 no Blender.

## O que ainda está fora e precisa entrar

A nota de índice do PR #6 cita estas fontes que existem só no projeto do Claude:

| Fonte fora do repositório | Para onde trazer |
| --- | --- |
| `00_INSTRUCOES_DO_PROJETO.md` (direção de arte, olhos, contraste, proibições) | regras como nota em `12 Modelos e pets/Pets lendarios e miticos/` |
| `01_ESTADO_ATUAL.md` (situação do jogo: áreas, ovos, pets no `Config`) | resumo nesta nota |
| Alvos 2D originais 1024² (`referencias-pets-lendarios-miticos/alvos-2d/`) | `Recursos/Pets lendarios e miticos/` (hoje só há cópias de 640 px) |
| Renders originais (`renders-3d/`) e conceitos (`pets-v2/`) | mesma pasta de `Recursos` |
| Modelos Royal Skywhale v2–v4 (`.glb`) citados em `Sky Whale.md` | `Recursos/Skywhale/` |
| Código e `Config` do jogo | pasta própria na raiz (ex. `climb-for-pets/`), como os outros jogos |

Enquanto isso não entra, as conversas do projeto devem tratar essas fontes como ausentes e avisar o que falta,
em vez de usá-las. A frase "para gerar ou comparar, use os originais da pasta do projeto" do PR #6 deixa de valer
quando os originais forem trazidos para cá.

## Decisões

- 31/10/2026: os 21 pets Lendários e Míticos seguem a [[Regua Steal An Egg para os 21 pets]], em 7 lotes por área, aprovados pelo usuário lote a lote.
- 31/10/2026: as rodadas dos pets seguem o [[Processo rapido de rodada]] (aprovado pelo usuário): rodar até aprovar com regra de platô, kit único de render e ícone, checagem automática, variantes em paralelo e banca de 3 revisores.

- 31/10/2026: as 22 imagens finais em `Recursos/Pets lendarios e miticos/Alvos finais/` são a meta de aparência; cada pet tem que ficar extremamente parecido com a sua (critério 7 da régua).

## Próxima ação

Mesclar os PRs #5, #6 e #7 (decisão do usuário) e trazer os arquivos da tabela acima numa entrega própria.
