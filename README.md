# Climb for Pets

Projeto separado do repositório de referências (`luksladp/ROBLOX_JOGOS`), que guarda só referências.

- `notas/`: estado do projeto e o lote 1 (Volcano).
- `modelos/`: notas dos 21 pets Lendários e Míticos (fichas, régua Steal An Egg, prompts, processo de rodada).
- `recursos/`: imagens, GLBs e entregas dos pets.
- `ferramentas/`: scripts de produção de pets (rodada, checagem, render, comparação, banca).

Origem: movido do ROBLOX_JOGOS em 02/11/2026. Os wikilinks `[[...]]` apontam para notas que ficaram no repositório de referências; os caminhos dos scripts podem precisar de ajuste.

## Ajustes depois da mudança (02/11/2026)
- Os scripts de `ferramentas/` agora usam a raiz deste repositório e `recursos/` (minúsculo). Rodar `python ferramentas/rodada.py ...` a partir da raiz. Só conferi que compilam; não rodei.
- `comparar.py` e `checar.py` precisam das imagens de referência do Steal An Egg, que ficam no repositório de referências (`luksladp/ROBLOX_JOGOS`, `jogos/Recursos/Referencias de pets raros/`). Copie essa pasta para `recursos/Referencias de pets raros/` antes de usar.
- Os `[[wikilinks]]` das notas apontam para notas do ROBLOX_JOGOS (escala, pivôs, régua do Steal An Egg etc.); abra-as lá.
