---
area: modelos
tipo: ficha
resumo: Entrega da Volcanic Phoenix (Volcano, Legendary) do lote 1 da régua Steal An Egg — GLB com rig e 4 clipes, texturas, flipbooks de VFX, renders e como regenerar tudo em Blender headless.
termos: volcanic phoenix entrega lote 1 volcano legendary glb rig clipes idle fly happy flare renders icone blender regua steal an egg
---
# Volcanic Phoenix — entrega do lote 1 (Volcano)

Feita em 31/10/2026 seguindo [[Regua Steal An Egg para os 21 pets]] e a ficha [[Volcanic Phoenix]] (só nome, espécie, raridade, gait, clipes e pontos de efeito). Nada foi copiado de um pet do Steal An Egg; ele serve só de nível.

## O que tem aqui

| Arquivo | O que é |
| --- | --- |
| `VolcanicPhoenix.glb` | 4 malhas skinadas (`_Body`, `_Glow`, `_Eyes`, `_EyeCore`), rig de 24 ossos, clipes Idle, Fly, Happy e Flare, 6 âncoras `FX_*` |
| `tex/` | ColorMap, RoughnessMap e MetalnessMap 1024² do `_Body` para o `SurfaceAppearance`, mais o EmissiveMap das veias (vai no GLB; no Roblox as veias ficam pintadas na Color) |
| `vfx/` | 5 efeitos em HTML + folhas de flipbook 1024², `trail_flame.png` e `emissores.md` (lista e orçamento) |
| `renders/` | frente, 3/4 e lado sem e com efeitos, ícone 128 px (e 512), `clipes_quadros.jpg` (4 quadros de cada clipe) |
| `fonte/` | `build.py` (gera tudo), `render.py`, `fx_preview.py`, `anim_check.py` |

## Números

| Malha | Tris | Material no Roblox |
| --- | --- | --- |
| `VolcanicPhoenix_Body` | 14 686 | `SurfaceAppearance` (Color/Roughness/Metalness de `tex/`) |
| `VolcanicPhoenix_Glow` | 2 292 | Neon `FF9A28` (lava sob as placas, veios das asas, plumas de chama da cauda e boca) |
| `VolcanicPhoenix_Eyes` | 160 | Neon `FFB030` (olho) |
| `VolcanicPhoenix_EyeCore` | 160 | Neon `FFD070` (núcleo pouco mais claro) |

- Todas abaixo de 20 000 tris por malha. Brilho limitado às pontas (Glow), aos olhos e aos veios principais do peito e rosto (padrão do lote: ≤ ~20%).
- Escala base: 6,7 de envergadura × 5,7 de altura (pés a 0,40 do chão, topo da crista a 6,1; pivô no chão). No jogo ×1,6.
- Clipes a 30 fps, primeiro quadro = último (loop sem salto): Idle 3,0 s · Fly 1,2 s (corpo a 15°) · Happy 2,2 s (giro de barril no osso Body + grito) · Flare 2,0 s (fecha 0–0,4 s, estoura em 0,4 s).
- Ossos: Root, Body, Neck, Head, Wing1/Wing2 .L/.R, Leg.L/.R, 7 penas de cauda com 2 ossos cada.
- Padrão do lote Volcano: obsidiana violeta-escura fosca (`33293F`/`4A3D60`/`62537E`, roughness 0,68) com rede de veias finas laranja-lava em corpo, cabeça, asas e cauda; pontas das penas em degradê vermelho `8A2010` → laranja `FF4A18` → Glow `FF5A1E`; ouro velho `C9962E`; acento dourado de raridade `FFC828` nas garras. Olhos são o ponto de brilho mais forte; a gema do peito é menor que eles.
- Marca assimétrica: a asa esquerda tem uma primária quebrada pela metade.

## Rodada 2 (31/10/2026, após a reprovação do revisor do lote)

Tronco e cabeça ~1,5× mais largos (o corpo domina o quadro), asas menores com primárias, secundárias e 4 fileiras de coberteiras sobrepostas e com espessura; veias de lava finas e emissivas em todo o corpo; corpo fosco; uma só cor de brilho (laranja da área); olhos 25% maiores e acesos; gema do peito menor e o `CorePulse` menos intenso; luz de borda quente nos renders. Escala, ossos e clipes seguem os mesmos.

## Rodada 3 (31/10/2026, padrão do lote revisado)

Veias de calibre médio, células maiores, só nos veios principais (peito, garganta, rosto e alguns trechos), com costas e laterais em pedra fosca; emissão mais forte já sem efeitos. Asas e cauda em lâminas de pena maiores e limpas, sem rachadura, só com a ponta acesa. Corpo de ave de fogo: quilha projetada, pescoço visível, cabeça alongada, crista 1,5× mais alta, pernas mais grossas. Olhos com núcleo branco-amarelo quente, halo laranja e contorno escuro (sem dourado em volta); bico e garras em dourado fosco; pontas das penas menos intensas. Efeitos: chamas de verdade (`flame_4x4.png`) nas pontas das asas, na crista e na cauda; ver `vfx/emissores.md`.

## Rodada 4 (31/10/2026, corpo aprovado pelo usuário; rosto refeito)

O usuário gostou do corpo e achou olhos e boca estranhos. Olhos sem esclera: íris acesa `FFC040` com núcleo branco-quente pequeno, halo laranja e contorno escuro, assentados na superfície da cabeça (antes ficavam afundados) e ~1,5× maiores; sobrancelhas inclinadas para dar atitude, sem cobrir a íris. Bico de rapina curto e grosso com gancho, em dourado fosco liso (`B8862E`). Nenhuma veia no rosto. Volumes grandes (tronco, quilha, pescoço, cabeça, coxas) lisos, sem aspecto amassado; asas com espessura; tarsos e garras mais grossos; losango do peito menor; pontas das penas menos saturadas (`F0703A`). Efeitos: anel de brasas no chão (Beam com `ground_ring.png`) e chama da crista encostada na crista.

## Rodada 5 (31/10/2026, olho padrão do lote)

Olho padrão dos 3 pets: amêndoa de rapina inclinada (canto interno mais baixo), toda emissiva `FFC040` com núcleo mais claro `FFE8A0`, sem pupila e sem anel claro, afundada numa órbita de pedra escura `241C30` sob uma sobrancelha-placa fina. Bico maior, curvo e em gancho, com fenda escura de boca até o canto. Placas com veias laranja em volta do corpo todo (frente, flancos, costas e nuca); o rosto fica sem veias. Peito e ombros mais largos, tronco menos redondo, pescoço mais longo e definido, cabeça mais alta. Pontas das asas e cauda em laranja-lava `FF5A14`.

## Rodada 6 (31/10/2026)

Olhos com o dobro da altura da rodada 5, sem pálpebra cortando: núcleo `FFF0C0`, íris `FFC040`, halo laranja (Glow) e órbita escura; mais à frente na cabeça, os dois aparecem a 3/4 e no ícone. Bico curto de fênix no dourado fosco do lote (`C9962E`). Crista de chama ~30% mais alta, com metade da pena acesa. Cabeça com o mesmo material e veias do corpo, base sem manchas. Placas do peito maiores e em menor número; veias em células maiores que saem de um coração de lava grande no peito e ficam esparsas nas bordas. Pernas mais grossas. Ícone enquadrado mais perto da cabeça.

## Rodada 7 (31/10/2026, mesmo material do Lava Titan e do Molten Dragon)

Corpo, cabeça, nuca, costas e coxas agora são placas de pedra facetadas soltas (polígonos de 5 a 7 lados com topo chanfrado, três tons de obsidiana, tamanho e ângulo variados) sobre uma camada de lava contínua na malha Glow; as frestas entre as placas são as juntas laranja, e nenhuma área lisa aparece de lado. Uma só cor de brilho: juntas, coração e interior da boca em `FF9A28`, olhos `FFB030` com núcleo `FFD070`. As bordas das penas de asa, cauda e crista passaram para laranja escuro fosco (`B4441A`, sem emissão). Olho ~25% menor, sem aro e sem centro escuro, afundado numa órbita de pedra sob uma sobrancelha esculpida inclinada. Bico maior encaixado na cabeça, entreaberto com o interior em brasa. Ícone afastado para caber asas e crista com margem, com rim light quente dos dois lados para o fundo escuro. Tronco um pouco mais largo sob as asas, tarsos, pés e garras mais grossos.

## Rodada 8 (31/10/2026)

Cabeça em máscara de pedra própria, facetada e sem seixos. Placas do corpo do tamanho das do Lava Titan, com juntas finas, e sem manchas laranja largas em volta do coração. Asas em penas sobrepostas roxo escuro com ponta laranja fosca (`D9661E`, sem o vermelho) e veios de lava finos na nervura de cada primária e secundária, continuando os do corpo. Crista ~30% e cauda ~20% mais longas, com pontas e plumas em chama (`FF9A28`). Órbitas escuras e fundas (`140F1C`) com olhos amarelos em amêndoa maiores; bico de pedra roxa (`5C4E78`); garras escuras (`2A2236`), sem dourado. Anel de chão com 6,4 de largura e sem transparência, no nível do anel do Titan.

## Rodada 9 (31/10/2026, última do lote)

Mantidos a máscara da cabeça, os olhos e o bico da rodada 8. Tronco bem maior e mais largo em relação às asas (raios 1,95 × 1,38 × 1,62, quilha e anca maiores, ombros mais abertos), coxas, tarsos, pés e garras mais grossos. A estrela do peito e as manchas laranja saíram: a lava aparece só pela rede contínua de fendas finas entre as placas, no traço do Lava Titan. Pedra puxada para o cinza-ardósia do Titan (`37334A` a `5F5974`). Pontas da crista em laranja-brasa (`E0521A`, sem amarelo-dourado). Ícone a 35° de frente, mais perto, com rim light laranja forte dos dois lados acendendo o contorno do tronco. Efeitos: anel de chão com `Color FF7A1E` (laranja do Titan) e chamas das pontas maiores (Size 2,0 nas asas e na cauda, 1,6 na crista).

## Rodada 10 (31/10/2026, rosto refeito; corpo da rodada 9 mantido)

Pedido do usuário: o corpo ficou bom, olhos e boca são o ponto fraco. Cabeça redonda bem maior (raios 1,38 × 1,24 × 1,24, ~2,5 de altura, perto de 1/3 do pet sem a crista), assentada sobre o tronco com o pescoço quase escondido; crista ~15% menor para a cabeça ser o centro de atenção. Olhos do lote ~1,6× maiores (amêndoa acesa `FFB030` com núcleo `FFD070`, órbita `140F1C`), bem separados do bico, com sobrancelhas de pedra encaixadas na cabeça formando um V. Bico refeito como cunha facetada (antes lia como nariz): largo na base, em gancho, em pedra mais clara que a cara (`7A7299`); a mandíbula de baixo desce e a boca acesa (`FF9A28`) aparece só entre as duas bordas, em V de frente e em cunha de lado. Placas do peito um pouco maiores; ombro e braço das asas com mais volume; tarsos, pés e garras mais grossos. O ícone de 128 px agora sai do `render.py`: pet inteiro a 32° de frente, 8% de margem.

Revisor independente da rodada 10 (só a folha e a régua): REPROVADO com 3 PIOR (1 nível, 2 coerência, 4 brilho); o ícone (6) passou. Sobre o rosto: olhos legíveis, mas "discos de lâmpada" sem pupila e saltando da silhueta de lado; bico pequeno, escuro e reto, que some de frente; cabeça lisa destoando do corpo de placas; manchas laranja largas no tronco.

## Rodada 11 (31/10/2026)

Olhos com pupila escura redonda e anel claro em volta (olho de ave), um pouco mais de frente e afundados na órbita, sem sobrar da silhueta de lado. Bico ~15% maior, em pedra bem mais clara que a cara (`9890B6`), com perfil curvo do topo ao gancho; mandíbula de baixo visível e a boca acesa numa fresta mais fina. Cabeça com placas facetadas no alto, na nuca e nos lados, como o corpo (frestas escuras, sem brilho), e a máscara lisa só na cara. Placas do corpo maiores em relação ao espaçamento, então as fendas de lava voltam a ser linhas finas (sem manchas largas). Asas ~14% maiores.

Revisor da rodada 11: REPROVADO com 3 PIOR (1 nível, 2 coerência, 3 escada); o brilho (4) e o ícone (6) passaram. Sobre o rosto: olhos muito legíveis, mas "adesivo de desenho" com pupila preta, de outro traço que o Titan e o Dragon; bico da cor do corpo, sem contraste; a boca parece um risco torto; sobrancelhas grossas e cara chata leem como coruja.

## Rodada 12 (31/10/2026)

Olho do lote, como o do Lava Titan: amêndoa facetada acesa (`FFB030`), sem pupila, com núcleo mais claro (`FFD070`) e órbita escura; sobrancelhas mais finas assentadas na borda de cima. Bico em laranja-brasa fosco (`C2561C`, a família das pontas das penas, sem emissão), que contrasta com a cara escura; a boca acesa aparece entre as mandíbulas. Cabeça um pouco mais longa para a frente (ave de rapina, não coruja). Placas do corpo e da cabeça mais angulares (4 a 6 lados, chanfro menor), como as do Titan. Cauda de fênix ~35% mais longa, em leque mais aberto e mais alto.

Revisor da rodada 12: REPROVADO com 3 PIOR (1 nível, 2 coerência, 6 ícone). Sobre o rosto: olhos em amêndoa leem bem de frente e a 3/4, mas de lado viram uma fresta grudada no bico; bico grande demais, encostando nos cantos dos olhos; manchas largas de lava entre placas soltas; penas com degradê marrom que os outros dois não têm; corpo escuro some no fundo escuro do ícone.

## Rodada 13 (31/10/2026)

Placas recortadas em células de Voronoi sobre a camada de lava, com fresta fina e constante entre vizinhas (o mesmo método das placas do Lava Titan): a lava vira uma rede de veios finos no corpo e na cabeça, sem manchas. A cabeça também é placa sobre lava; a cara fica numa máscara lisa saliente, onde estão olhos, sobrancelhas e bico. Pedra em grafite sem lilás (`3E3B40` a `6A656E`), acompanhando a troca do Lava Titan na rodada 13 dele. Penas de asa e cauda em pedra, sem o degradê marrom; o laranja das asas fica nos veios. Bico ~12% menor, olhos mais afastados e mais de lado (aparecem de perfil).

Revisor da rodada 13: REPROVADO com 2 PIOR (1 nível, 6 ícone); coerência (2), escada (3), brilho (4) e paleta (5) passaram. Rosto: olhos naturais de frente, bravos e legíveis; o bico terracota parecia argila e sumia no ícone. A conferência do lote na mesma rodada (outro revisor) pediu também placas menos regulares, leque de cauda, garras grossas e bico mais aberto.

## Rodada 14 (31/10/2026)

Pedra em grafite médio, mais clara (`55525A` a `827D88`), para a silhueta não sumir no fundo escuro; no ícone, uma luz de borda fria de um lado e quente do outro, e margem de 5%. Placas irregulares: sementes deslocadas ao acaso, tamanhos de 0,8× a 1,2× e leve inclinação (sem aspecto de favo); placas grandes no peito e menores nas bordas, coxas e anca; poucas facetas grandes e baixas na cabeça. Asas ~20% maiores; cauda ~15% mais longa, leque mais aberto, penas mais largas com a face voltada meio para cima. Pés e garras mais grossos (pés no chão). Bico em laranja-lava mais claro (`E8782A`) e mais aberto, com a boca acesa mais visível. Olhos um pouco menos de lado.

Revisor da rodada 14: REPROVADO com 2 PIOR (1 nível, 2 coerência); o ícone (6) passou. Pediu cauda de pedra escura (estava cinza-clara e lavada), garras legíveis em vez de espetos, pescoço sem anel de espetos, penas de asa com volume e veios em rede como a membrana do Dragon. Rosto: bom de frente; bico com cara de barro, mandíbula de baixo fina, olho de trás na borda a 3/4.

## Rodada 15 (31/10/2026)

Penas de asa e cauda em pedra escura com rede de rachaduras de lava pintada (o mesmo traço da membrana do Molten Dragon), mais grossas; saem os veios retos em Glow. Pontas da cauda em laranja-brasa. Sem a gola de espetos: as placas cobrem a junção da cabeça com o peito. Pernas visíveis: tarso grosso do pé ao joelho, pé de pedra, 3 dedos à frente e 1 atrás com garra curta e escura. Bico em grafite claro (`8E8993`), mandíbula de baixo mais grossa. Olhos um pouco mais juntos e de frente.

Revisor da rodada 15: REPROVADO com 3 PIOR (1 nível, 2 coerência, 6 ícone). As rachaduras pintadas nas penas ficaram borradas, a cauda parecia varetas saindo do quadril com riscos amarelos, o bico grafite sumia de frente e as asas escuras se fundiam no fundo escuro do ícone.

## Rodada 16 (31/10/2026)

Penas de asa e cauda voltam a ser pedra escura com veio reto aceso (Glow), mais nítido que a rachadura pintada. Cauda em leque de 7 penas atrás do corpo (ângulos simétricos, mais longas no centro) com plumas de brasa. Crista maior, 7 penas. Bico em pedra clara (`B3ADB8`) para separar da cabeça. Penas um pouco mais claras e luz de contorno fria no ícone para destacar do fundo escuro.

Revisor da rodada 16: REPROVADO com 2 PIOR (1 nível, 4 brilho); coerência, escada, paleta e ícone passaram. Pernas em coluna, placas de tom uniforme, cauda chapada e plumas soltas; crista e cauda num vermelho-laranja que competia com o âmbar dos veios; ponto quase branco no peito com efeitos. Rosto: lê bem de frente e a 3/4; borda do olho recortada e laranja sob o bico parecendo língua.

## Rodada 17 (31/10/2026, última desta série)

Crista e pontas da cauda no mesmo âmbar dos veios (`D46F1A`), com a base em pedra; sem plumas chapadas; leque da cauda mais fechado. Placas com valor próprio: quinas mais claras e fundo das fendas mais escuro (pointiness e AO no material assado). Pernas com joelho, tarso afinando com 3 escamas de pedra na frente, tornozelo e garras maiores. Olho em amêndoa lisa (sem borda recortada), bico 9% maior e fresta da boca menor. Luz do peito mais fraca e mais laranja no preview de efeitos.

Revisor da rodada 17: REPROVADO com 1 PIOR (1 nível, contra o Pumpkin Golem). Brilho (4), coerência, escada, paleta e ícone passaram. Falta volume: cauda ainda lê como lâmina plana de lado, pernas finas para a massa do tronco, penas de asa sem espessura, e sem efeitos a silhueta lê mais como coruja de pedra do que como fênix. Rosto: olhos legíveis de frente, a 3/4 e no ícone; o bico ainda se confunde com o cinza da cabeça de frente e o olho de lado vira mancha.

## Origem dos prints

**Render do Blender (não é o jogo).** O Studio está acessível, mas levar a malha para lá sem subir o asset exigiria digitar centenas de KB de dados pelo MCP. Subir o GLB é ação externa e ainda não foi autorizado. Os prints com efeitos usam os flipbooks entregues em planos emissivos (`fx_preview.py`), não os `ParticleEmitter` do Roblox.

## Regenerar

```
pip install bpy pillow            # Blender 5.2 headless, Python 3.13
python fonte/build.py /tmp/vp     # GLB, .blend, tex/
python fonte/render.py /tmp/vp    # renders sem efeitos e ícone
python fonte/render.py /tmp/vp --fx
python fonte/anim_check.py /tmp/vp
```

Os flipbooks: `python .framework/flipbook.py "Recursos/Pets lendarios e miticos/Volcanic Phoenix/vfx/<efeito>.html" --grade 4` (a partir de `jogos/`; spark usa `--grade 2`, heat_aura usa `--loop`).

## Ainda falta (fica com a thread do lote)

Folha de comparação com `comparar.py`, veredito do revisor independente, nota do lote em `19 Projeto em andamento/` e o PR do lote.
