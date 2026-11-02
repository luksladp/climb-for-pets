---
area: modelos
tipo: registro-de-entrega
resumo: Entrega do Lava Titan v3 (Legendary, Volcano, lote 1) na régua Steal An Egg, rodada 17 — cabeça de gorila refeita nas rodadas 10 a 17, GLB com 4 malhas (maior 8 765 tris), rig de 17 ossos, clipes Idle/Walk/Happy/Slam, 5 flipbooks, 6 emissores + 1 luz, renders do Blender e ícone 128 px; de onde veio e como refazer.
termos: lava titan v3 entrega lote 1 volcano glb rig clipes idle walk happy slam tris flipbook render blender icone 128 regua steal an egg
---
# Lava Titan v3 — entrega (lote 1 Volcano)

**Data:** 31/10/2026 · **Raridade:** Legendary · **Gait:** ground · **Régua:** [[Regua Steal An Egg para os 21 pets]] (degrau Alto: Graveyard Brute, Abomination Kong, Pumpkin Golem).

## Arquivos (nesta pasta)

| Arquivo | O que é |
| --- | --- |
| `LavaTitan.glb` | modelo final: 3 malhas com rig, skin e 4 clipes |
| `LavaTitan_paleta.png` | única textura (512×32, cores em faixas), usada pelas 3 malhas |
| `renders/frente.png`, `tres_quartos.png`, `lado.png` | sem efeitos, 1024², fundo transparente |
| `renders/*_fx.png` | as mesmas vistas com efeitos ligados (magma em brilho cheio, 1 quadro de cada flipbook no ponto do emissor, luz da cratera) |
| `renders/icone_128.png` | ícone de inventário, fundo transparente, contorno escuro + borda quente (`fonte/icone.py`) |
| `vfx/*.html` e `vfx/LavaTitan_*_4x4.png` / `_2x2.png` | efeitos em HTML e as folhas de flipbook geradas |
| `emissores.md` | lista de emissores, pontos de origem e orçamento |
| `fonte/build_v3.py`, `fonte/render_v3.py` | geram o GLB e os renders (bpy 5.2) |
| `fonte/build_v2_origem.py`, `render_v2_origem.py` | ponto de partida (lava-titan-v2), trazido para o repositório nesta entrega |

## Números do GLB

| Malha | Tris | Material | No Roblox |
| --- | --- | --- | --- |
| `LavaTitan_Rock` | 8 765 | `LavaTitan_Rock` (paleta, fosco) | MeshPart + SurfaceAppearance com a paleta (grafite `3F3C46`/`2F2D35`/`1E1C22`, focinho `524E59`, dentes `D6CFC4`) |
| `LavaTitan_Magma` | 7 374 | `LavaTitan_Magma` (paleta + emissão) | MeshPart Neon laranja-lava `FF7A1A` (veias, fendas do crânio, cratera, contorno dos olhos); interior da boca na mesma cor |
| `LavaTitan_Eyes` | 232 | `LavaTitan_Eyes` (paleta + emissão forte) | MeshPart Neon própria: olho `FFB030` com brilho `FFE6A0` |
| `LavaTitan_Crystal` | 252 | `LavaTitan_Crystal` (paleta) | cristais de obsidiana grafite `18171C` com facetas `403D47`, sem ponta acesa (rodada 10) |

- Maior malha: **8 765 tris** (limite 20 000). Textura 512×32 (16 faixas) (limite 1024²). Pivô no chão (nenhum vértice abaixo de z = 0), 1 unidade = 1 stud.
- Tamanho base: largura 6,58 · profundidade 4,90 · altura 5,79 (topo da cabeça; cristais 5,45). No jogo ×1,6.
- **Rig:** 17 ossos (`root`, `hips`, `spine`, `chest`, `head`, e por lado `upperarm`, `forearm`, `hand`, `thigh`, `shin`, `foot`). Placas de rocha presas a um osso só (não deformam); núcleo de magma com pesos suaves.
- **Clipes** (30 fps, no lugar, primeiro quadro = último): `Idle` 3,5 s (respira, ombros sobem) · `Walk` 2,0 s (knuckle-walk, braço com a perna oposta) · `Happy` 2,5 s (soca o peito 3× e ergue os punhos) · `Slam` 2,2 s (ergue os punhos, bate no chão em 0,5 s, onde disparam os efeitos). Conferido reimportando o GLB (rodada 1): 3 malhas, 17 ossos, 4 animações.

## Rodadas 10 a 17 (31/10/2026, olhos e boca refeitos)

O luks achou o corpo bom e os olhos e a boca estranhos. Nas rodadas 10 a 17 a cabeça foi refeita do zero; o corpo (núcleo, mosaico de placas, colunas, cristais, cratera, mãos e pés) continua igual, porque o gerador do corpo volta ao mesmo ponto depois da cabeça e do mosaico. Cada rodada teve um revisor independente novo, que viu só a folha e a régua. Prints: render do Blender (não é o jogo).

| Rodada | O que mudou | PIOR do revisor |
| --- | --- | --- |
| 10 | Cabeça de gorila: crânio em cúpula, sobrancelha em V, olhos angulares acesos, focinho claro com narinas, boca em vinco com presas; pontas dos cristais apagadas e base 40% mais grossa; topo das placas em 3 tons e fissura fina escura em parte das placas grandes | 1, 6 (rosto natural, mas pequeno no ícone) |
| 11 | Cabeça 19% maior e mais alta, olhos 1,45× mais altos, boca entreaberta acesa, dentes cor de osso | 1, 6 |
| 12 | Cabeça 40% maior que na 10, boca aberta em "U" com lábio de pedra e dentes | 1, 5 (pedra lilás) |
| 13 | Pedra e cristais em grafite (sem lilás); olhos em amêndoa abaulada com ponto de brilho; focinho, bochechas e queixo numa peça só | 1 |
| 14 | Cabeça mais alta, "U" mais fundo, dentes de baixo maiores. Teste de placas grandes no corpo: ficou bagunçado e foi desfeito | 1 |
| 15 | Veias em toda fresta estreita (rede contínua), nós dos dedos maiores e claros, crânio partido em 4 placas com fendas de lava, grafite mais escuro (pedido da conferência do lote) | 1 |
| 16 | Focinho no tom do corpo, narinas menores e afundadas, presas em pé presas na mandíbula, perfil da cabeça mais contínuo | 1 |
| 17 | Cabeça mais alta e à frente (aparece de lado), focinho mais saliente, dentes do meio brancos, menos lascas de lava soltas nos vãos | 1, 4 |

Os revisores das rodadas 13 a 17 leram o rosto como "gorila bravo cartoon, natural e expressivo"; o da 14 disse que é a melhor parte do pet. O PIOR que sobrou (critério 1) é do corpo: placas do mesmo tamanho, pernas escondidas atrás dos punhos e perfil de lado confuso. Mudar isso mexe no corpo que o luks aprovou, e a decisão ficou com ele. Folhas de cada rodada em `folhas/LavaTitan_comparacao[_fx]_rodadaNN.png`. Brilho medido sem efeitos na rodada 17: 7,0 % (frente), 5,7 % (3/4), 3,7 % (lado).

## Rodada 8 (31/10/2026)

Na rodada 7, os critérios 1, 4 e 6 ficaram PIOR. Corpo mantido.

- **Cabeça integrada:** mais baixa e recuada (centro y 1,25, z 3,88), pescoço largo fundido no tronco; a mandíbula desce e recua até o peito, sem o bloco de boca projetado.
- **Boca recortada na pedra:** abertura entre o lábio e a mandíbula, interior recuado em lava na mesma cor das fissuras (`FF7A1A`), com dentes de pedra grossos e de tamanhos diferentes.
- **Olhos** um pouco maiores, mais fundos e mais brilhantes (emissão dos olhos acima da das fissuras), curvando para a lateral para ler a 3/4 e de lado.
- **Ícone** enquadrado mais perto da cabeça, com mais contraste (`fonte/icone.py`).

## Rodada 7 (31/10/2026)

Na rodada 6, só os critérios 1 e 4 ficaram PIOR. O lote fixou um meio-termo para os olhos dos 3 pets. Corpo mantido.

- **Cabeça:** a laje chata do topo virou crânio de rochas arredondado; **sobrancelha saliente** em crista que faz sombra; cabeça mais à frente dos ombros (y 1,50).
- **Olhos:** cerca de 25 % menores que na rodada 6, **afundados** numa cavidade escura sob a sobrancelha, laranja-amarelo saturado `FFB030` com núcleo pouco mais claro `FFC860`.
- **Boca:** mandíbula aberta de verdade, larga e abaixada; interior recuado em lava `A83C10`, mais fraco que os olhos; sem dentes em zigue-zague; o vão aparece também de lado.
- **Peito:** a estrela e o filete dourado saíram; o peito tem só as veias comuns.
- **Pontas dos cristais** na mesma cor das fissuras; **aura do chão** em laranja (`FF5A14`), não dourada.

## Rodada 6 (31/10/2026, olhos e boca no padrão revisado do lote)

O revisor apontou olhos pequenos e estreitos nos 3 pets; o padrão do lote foi revisado. Corpo mantido.

- **Olhos:** amêndoa inclinada para dentro com o dobro da altura, inteira abaixo da testa; de fora para dentro: órbita escura (contorno), halo laranja, íris `FFC040` e núcleo `FFF0C0`. São a área mais clara do rosto.
- **Boca escavada**, mais estreita que o rosto: fundo escuro recuado, brasa baixa `7A2E14` só na cor (sem Neon, diferente das fissuras) e dentes irregulares de pedra em cima e embaixo.
- **Cabeça entalhada:** um pouco maior (escala 1,90) e mais à frente dos ombros (y 1,32), testa saliente, maçãs do rosto, laterais fechadas e mandíbula própria saliente.
- **Cristais** afinando em facetas (largura 0,80 a 42 % e 0,42 a 80 % da altura), com brilho nas facetas e ponta em brasa menor; deixam de parecer lápis.
- **Ícone** quase de frente (vista 0,30 / 0,95), enquadrado um pouco mais alto para a cabeça ficar maior.

## Rodada 5 (31/10/2026, só a cabeça)

Na rodada 4, só os critérios 1 e 4 ficaram PIOR, ambos pelo rosto. Corpo mantido.

- **Cabeça de pedra** maior (escala 1,80), mais baixa (centro z 3,98) e integrada ao tronco por um pescoço largo; crânio, nuca e laterais de rocha cobrem o núcleo (de lado não aparece bola); os dois chifres finos saíram.
- **Testa pesada:** laje de rocha que avança por cima dos olhos.
- **Olhos no padrão do lote:** fenda em V inclinada para dentro ("bravo calmo"), toda emissiva `FFC040` com núcleo mais claro `FFE6A0`, sem pupila nem anel, numa órbita escura sob a testa.
- **Boca:** fenda larga e reta entre o lábio de pedra e a mandíbula quadrada, brilho laranja-lava `FF7A1A`, dobrando para os lados para ser legível de frente, a 3/4 e de lado.

## Rodada 4 (31/10/2026, pedido do luks + terceira reprovação)

O luks gostou do corpo e achou **olhos e boca estranhos**; o corpo ficou como estava.

- **Olhos sem esclera:** contorno escuro, halo laranja `FF7A1A`, íris `FFC040` e núcleo branco-quente pequeno `FFF6DC`, maiores (raio 0,14), à frente da aba, visíveis nas 3 vistas. Viraram uma malha própria (`LavaTitan_Eyes`) para ser uma MeshPart Neon separada no Roblox.
- **Boca natural:** fenda fechada e levemente curva na frente da mandíbula, com brilho baixo de lava; o rosto não tem mais magma aparecendo entre as pedras (antes lia como dentes estranhos).
- **Cabeça** um pouco maior (escala 1,66) e mais alta (centro z 4,32).
- **Anel dourado** do peito mais fino e fosco (`B08A45`, rugosidade 0,85).
- **Blocos com chanfro** mais largo e borda clara `6A6180`; topo médio, laterais escuras.
- **Cristais** com ponta em brasa laranja.
- **Aura no chão** maior e mais forte; a câmera de frente subiu um pouco para o anel aparecer.
- Brilho medido sem efeitos: 5,9 % (frente), 5,5 % (3/4), 4,1 % (lado).

## Rodada 3 (31/10/2026, segunda reprovação do revisor)

A rodada 2 melhorou (paleta IGUAL ao lote), mas ficou PIOR em rosto, anatomia, superfície, efeitos e ícone. Mudanças:

- **Rosto:** cabeça maior (escala 1,30 → 1,58) e mais à frente, com pescoço curto visível; olhos maiores, à frente da aba, em **branco-amarelo `FFF2C2`**, separados do laranja das veias.
- **Anatomia:** braços bem para fora (cotovelo x 2,30), fora da silhueta das pernas em vista frontal, com punhos grandes; ombros e peito projetados à frente (tronco inclinado).
- **Superfície:** fenda 0,03 (calibre médio do lote) e **veias só nos veios principais** (peito, garganta, ombros, cotovelos, pulsos, joelhos); o resto do núcleo exposto vira basalto fosco.
- **Acento:** filete dourado fosco `C9973A` em volta da estrela do peito (acento Legendary).
- **Efeitos:** a fumaça cinza saiu; entram **brasas e chama baixa na cratera** e uma **aura de brasas no chão**. O pulso do peito saiu (a estrela já é Neon). Com efeitos, a emissão do magma é 1,6 (antes 2,5), e as veias continuam laranja.
- **Ícone:** contorno escuro de 2 px e borda quente, legível sobre fundo claro e escuro.

## Rodada 2 (31/10/2026, correções do revisor independente)

O revisor do lote reprovou a rodada 1 (PIOR em 1, 2, 4, 5 e 6). Mudanças, seguindo o padrão do lote (basalto violeta-escuro fosco, veias laranja finas, brilho ≤ ~20%, uma cor de brilho, olhos como ponto mais forte, luz de borda quente):

- **Anatomia de brutamonte:** cabeça subiu acima da linha dos ombros (pescoço curto), braços afastados do tronco, punhos e nós dos dedos maiores, quadris mais abertos com vão entre as pernas.
- **Veias finas:** fenda entre placas 0,05 → 0,03 e, onde o núcleo ficava exposto numa área aberta, ele vira basalto escuro; o magma só aparece nas fendas. Brilho medido nos renders sem efeitos: **8,1 % (frente), 8,2 % (3/4), 7,3 % (lado)** da silhueta.
- **Basalto violeta-escuro:** paleta `4F4862`, `3A3449`, `25212F`; cristais `1E1828` com realce `5E4A80`.
- **Uma cor de brilho:** laranja-lava `FF7A1A` nas veias, estrela e cratera; só os olhos são mais claros (`FFC03A`), maiores e bem à frente. Estrela do peito menor (raio 0,80 → 0,50), na cor das veias.
- **Com efeitos:** emissão do magma 5,0 → 2,5, pulso do peito menor e laranja, fumaça da cratera mais densa e escura.
- **Renders:** luz de borda quente por trás para o pet não sumir no fundo escuro.

## O que mudou do v2 para o v3 (régua Steal An Egg)

- **Mais largo e pesado** como os brutamontes do degrau: ombros, antebraços e punhos maiores (largura 4,47 → 5,35).
- **Rede de fendas contínua e forte:** placas maiores e mais grossas com fendas laranja `FF4A10` largas entre elas, em vez de riscos finos sobre rocha quase preta.
- **Rocha fosca em 3 tons**, brilho só no laranja (uma cor forte). (Cores da rodada 1; a rodada 2 trocou para basalto violeta-escuro, acima.)
- **Olhos** em V maiores e amarelos, **estrela do peito** maior (raio 0,64 → 0,80). Cristais pretos altos, coluna partida e placa caída mantidos.

## Origem dos prints

**Render do Blender (não é o jogo).** O Studio do usuário estava acessível, mas importar a malha sem upload de asset exigiria enviar centenas de KB de vértices pelo MCP; o upload é ação externa e não foi feito. Câmera ortográfica, sol + céu neutro, fundo transparente. Se o usuário autorizar o Import 3D, os prints do Studio substituem estes.

## Como refazer

```
pip install bpy==5.2.3
python fonte/build_v3.py --out /tmp/lt        # gera LavaTitan.glb, lava_titan_v3.blend e a paleta
python fonte/render_v3.py /tmp/lt/lava_titan_v3.blend renders 1024 48 frente,tres_quartos,lado,icone [--fx]
python .framework/flipbook.py "Recursos/Pets lendarios e miticos/Lava Titan/vfx/<efeito>.html" --grade 4 [--loop]
```
python fonte/icone.py renders/icone.png renders/icone_128.png   # contorno + borda quente

## Pendências para o lote

- Folha de comparação (`comparar.py`) e veredito do revisor independente: feitos na thread do lote.
- Prints no Studio, se o usuário autorizar o Import 3D.

## Conexoes
[[Lava Titan]] · [[Regua Steal An Egg para os 21 pets]] · [[Modelo 3D a partir de imagem]] · [[VFX do HTML para o Roblox]]

## Rodada 9 (só o ícone)

Refeito apenas `renders/icone_128.png`; modelo, prints e efeitos não mudaram.
- Fundo transparente, sem caixa; contorno escuro fino e luz de recorte quente leve.
- Câmera 3/4 de frente mais afastada (ortho 9.0): corpo inteiro no quadro, conteúdo de 100 px centrado (margem do corpo ~11%, do brilho ~7%); pontas dos cristais, punhos e pés sem tocar a borda.
- Os dois olhos e a boca visíveis.
