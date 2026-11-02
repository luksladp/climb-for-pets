---
area: projeto
tipo: estado
resumo: Lote 1 (Volcano) do remake dos 21 pets na régua Steal An Egg — Volcanic Phoenix, Lava Titan e Molten Dragon com GLB, rig, 4 clipes, VFX, renders e ícone; rodadas 1 a 17 de folha de comparação e revisor independente, todas REPROVADAS; conferência 2 do lote (os três na rodada 17, fim das rodadas autorizadas) com Phoenix 2 PIOR, Titan 2 PIOR e Dragon 1 PIOR; o que falta, onde o SAE ainda é melhor e vereditos completos.
termos: lote 1 volcano volcanic phoenix lava titan molten dragon regua steal an egg folha comparacao revisor veredito reprovado rodada 13 conferencia grafite climb for pets rodada 17 conferencia 2 fim das rodadas regra corrigir pior mudar forma testar mais de um estilo nao so cor realismo brinquedo
---
# Lote 1 Volcano — estado em 31/10/2026 (conferência 2 do lote, rodada 17)

Régua: [[Regua Steal An Egg para os 21 pets]]. Arquivos de cada pet em `Recursos/Pets lendarios e miticos/<Pet>/` (GLB, `fonte/` com os scripts do Blender headless, `vfx/` com HTML e flipbooks, `emissores.md`, `entrega.md`, renders e ícone). Folhas de cada rodada em `<Pet>/folhas/`, folhas do lote inteiro em `Lote 1 Volcano/conferencia<N>/`, todas feitas com `.framework/comparar.py` (`--efeitos`, `--icone`).

**Situação: NÃO APROVADO.** Depois da rodada 9, cada pet ganhou uma thread de refino com 8 rodadas próprias (10 a 17), e as 8 acabaram. A conferência 2 juntou os três na rodada 17, montou a folha do lote e pediu um revisor novo por pet, que viu só a folha e a régua: **Volcanic Phoenix 2 PIOR, Lava Titan 2 PIOR, Molten Dragon 1 PIOR (só o ícone)**. O rosto (critério 4) passou nos três. 

**Pedido do usuário (luks, 31/10/2026, depois da conferência 2):** "Os pets parecem brinquedos, faz eles mais realistas mas continuam com o mesmo estilo." As threads dos três pets abrem até 8 rodadas novas (a partir da 18) com esse pedido, e o lote ganha uma conferência nova quando elas entregarem.

**Referência de forma do Molten Dragon (luks, 31/10/2026):** uma imagem gerada no ChatGPT com os [[Prompts de imagem de referencia dos 21 pets]] teve o corpo aprovado ("a seu formato de corpo ficou muito bom"), mas o usuário quer **studs e uma textura menos realista**. A imagem fica em `Recursos/Pets lendarios e miticos/Molten Dragon/MoltenDragon_forma-chatgpt_2026-10-31.png` como referência de forma (anatomia, proporções, pose, asas, chifres, coroa, anéis e cauda), não de textura.

**Imagens-alvo finais (luks, 31/10/2026):** os três pets agora têm de ficar extremamente parecidos com `Alvos finais/01_Volcanic_Phoenix`, `02_Lava_Titan` e `03_Molten_Dragon` (critério 7 da régua). As rodadas seguintes partem dessas imagens.

## Regra do usuário para corrigir um PIOR (31/10/2026)

Palavras do usuário (luks), depois da conferência 2: "Quando é avaliado que tem algo pior não é pro agente só mudar o que ele já criou, ele tem que ver tudo, pensar porque tá pior, e quando tiver pior ele sempre tem que dar pelo menos uma diferença no formato do que tá pior. Se a cabeça tá pior, se o corpo tá muito brinquedo, ele não tem que tentar mudar a cor, profundidade do laranja. Tem que ter alguma diferença. Tentar mais de um estilo, não manter o mesmo porque ele tem menos coisas piores, ele tem que mudar."

Como aplicar em cada rodada:

1. **Antes de mexer, entender o porquê.** Olhar o pet inteiro na folha, ao lado do pet SAE citado, e escrever em uma frase por que aquela parte está pior (forma, proporção, volume, silhueta, material), não só o que o revisor disse.
2. **Todo PIOR muda a forma da parte que está pior.** Se a cabeça está pior, a cabeça muda de formato; se o corpo lê como brinquedo, o corpo muda de volume, proporção ou construção. Trocar só cor, tom, profundidade do laranja, brilho ou intensidade de luz não conta como correção.
3. **Testar mais de um estilo.** Para a parte que está pior, fazer pelo menos duas versões de forma diferentes e comparar na folha. Não ficar no estilo atual só porque ele tem menos PIOR.
4. **Registrar na entrega** qual era o motivo, quais formas foram testadas e por que a escolhida ficou.

A conferência do lote confere isso: uma rodada que só mudou cor ou tom num critério PIOR é anotada como "sem correção de forma".

## Conferência 2 do lote (os três na rodada 17, fim das rodadas)

Commits: Volcanic Phoenix `bfa5516`, Lava Titan `5a86e86`, Molten Dragon `544f310` (com `ffe5aa5`, que só tira o `core.npz` do Git). Na faixa do lote de cada folha, os outros dois aparecem na vista 3/4 da mesma rodada.

| Pet | Veredito | PIOR | IGUAL |
| --- | --- | --- | --- |
| Volcanic Phoenix | REPROVADO | 1 nível, 3 escada | 2, 4, 5, 6 |
| Lava Titan | REPROVADO | 1 nível, 2 coerência | 3, 4, 5, 6 |
| Molten Dragon | REPROVADO | 6 ícone | 1, 2, 3, 4, 5 |

Em relação à conferência 1 (3 PIOR em cada pet), os três melhoraram. O Molten Dragon passou no nível do degrau pela primeira vez numa folha do lote; sobra o ícone, que ocupa pouco do quadro e some no fundo escuro.

**O ponto que se repete:** o critério 1 (nível do degrau) reprova Phoenix e Titan por um material só no corpo todo, contra os 3 materiais e a textura do pumpkin-golem. A coerência (2) ainda oscila entre revisores: na conferência 1 a Phoenix reprovou e o Titan também, cada revisor apontando o outro como o certo; na conferência 2 a Phoenix passou e o Titan reprovou por cacos pequenos contra as placas grandes da Phoenix e do Dragon.

**Ícone do lote ainda sem regra:** o revisor do Dragon pediu o pet enchendo 85 a 90% do quadro; o do Titan reclamou que o ícone dele encosta na borda e tem halo que os outros não têm.

![[Recursos/Pets lendarios e miticos/Lote 1 Volcano/conferencia2/VolcanicPhoenix_comparacao.png]]
![[Recursos/Pets lendarios e miticos/Lote 1 Volcano/conferencia2/VolcanicPhoenix_comparacao_fx.png]]
![[Recursos/Pets lendarios e miticos/Lote 1 Volcano/conferencia2/LavaTitan_comparacao.png]]
![[Recursos/Pets lendarios e miticos/Lote 1 Volcano/conferencia2/LavaTitan_comparacao_fx.png]]
![[Recursos/Pets lendarios e miticos/Lote 1 Volcano/conferencia2/MoltenDragon_comparacao.png]]
![[Recursos/Pets lendarios e miticos/Lote 1 Volcano/conferencia2/MoltenDragon_comparacao_fx.png]]

## Conferência 1 do lote (os três na rodada 13)

Commits: Volcanic Phoenix `19f75c9`, Lava Titan `5a2e97b`, Molten Dragon `37cf341`. Na faixa do lote de cada folha, os outros dois aparecem na vista 3/4 da mesma rodada.

| Pet | Veredito | PIOR | IGUAL |
| --- | --- | --- | --- |
| Volcanic Phoenix | REPROVADO | 1 nível, 2 coerência, 6 ícone | 3, 4, 5 |
| Lava Titan | REPROVADO | 1 nível, 2 coerência, 5 paleta | 3, 4, 6 |
| Molten Dragon | REPROVADO | 1 nível, 3 escada, 6 ícone | 2, 4, 5 |

O rosto (critério 4) passou nos três. O nível do degrau (1) reprovou nos três.

**Os revisores se contradizem na coerência (2):** o da Phoenix diz que as placas dela são arredondadas e regulares, contra as lascas irregulares do Titan e do Dragon; o do Titan diz que Phoenix e Dragon têm placas com linhas finas contínuas, contra os cacos soltos do Titan. O do Dragon deu IGUAL. O ponto em comum é que o traço das placas e das fendas ainda não é o mesmo nos três.

![[Recursos/Pets lendarios e miticos/Lote 1 Volcano/conferencia1/VolcanicPhoenix_comparacao.png]]
![[Recursos/Pets lendarios e miticos/Lote 1 Volcano/conferencia1/VolcanicPhoenix_comparacao_fx.png]]
![[Recursos/Pets lendarios e miticos/Lote 1 Volcano/conferencia1/LavaTitan_comparacao.png]]
![[Recursos/Pets lendarios e miticos/Lote 1 Volcano/conferencia1/LavaTitan_comparacao_fx.png]]
![[Recursos/Pets lendarios e miticos/Lote 1 Volcano/conferencia1/MoltenDragon_comparacao.png]]
![[Recursos/Pets lendarios e miticos/Lote 1 Volcano/conferencia1/MoltenDragon_comparacao_fx.png]]

## O que existe por pet (rodada 9)

| Pet | Raridade | Malhas (tris) | Rig | Clipes (loop) | VFX (normal) |
| --- | --- | --- | --- | --- | --- |
| Volcanic Phoenix | Legendary | Body 13 269, Glow 2 112, Eyes 160, EyeCore 160 | 24 ossos | Idle, Fly, Happy, Flare | 6 emissores + 2 trails + 1 luz; anel de chão FF7A1E |
| Lava Titan | Legendary | Rock 8 136, Magma 6 753, Crystal 252, Eyes 144 | 17 ossos | Idle 3,5 s, Walk 2,0 s, Happy 2,5 s, Slam 2,2 s | 6 emissores + 1 luz (low: 3, 0 luz) |
| Molten Dragon | Mythic | maior malha 15 220 (total 38 684) | 30 ossos | Idle 4,0 s, Walk 1,8 s, Happy 3,0 s, Breath 2,4 s | 5 emissores + 1 luz, 3 no Breath |

Todas as malhas abaixo de 20 000 tris. Detalhes e orçamento em `entrega.md` e `emissores.md` de cada pasta (ou da branch do pet).

**Origem dos prints: render do Blender (não é o jogo).** O Studio do usuário responde pelo MCP, mas a malha inteira só entra por Import 3D. O usuário autorizou o Import 3D, mas o controle da tela (computer use) continuou desligado no PC dele, então nenhum print do Studio foi feito.

## Placar das rodadas (PIOR por critério)

| Rodada | Volcanic Phoenix | Lava Titan | Molten Dragon |
| --- | --- | --- | --- |
| 1 | 6 PIOR | 5 PIOR | 5 PIOR |
| 2 | 4 PIOR | 4 PIOR | 3 PIOR |
| 3 | 4 PIOR | 3 PIOR | 3 PIOR |
| 4 | 4 PIOR | 2 PIOR | 4 PIOR |
| 5 | 4 PIOR | 3 PIOR | 4 PIOR |
| 6 | 4 PIOR (1, 2, 4, 6) | 2 PIOR (1, 4) | 3 PIOR |
| 7 | 4 PIOR (1, 2, 4, 6) | 3 PIOR (1, 4, 6) | 3 PIOR (1, 4, 6) |
| 8 | 4 PIOR (1, 2, 3, 6) | **1 PIOR (6)** | **1 PIOR (6)** |
| 9 | 2 PIOR (1, 6) | 2 PIOR (1, 4) | 2 PIOR (2, 6) |
| 10 | 3 PIOR (1, 2, 4) | 2 PIOR (1, 6) | 4 PIOR (1, 2, 4, 6) |
| 11 | 3 PIOR (1, 2, 3) | 2 PIOR (1, 6) | 2 PIOR (1, 2) |
| 12 | 3 PIOR (1, 2, 6) | 2 PIOR (1, 5) | 3 PIOR (1, 2, 4) |
| 13 | 2 PIOR (1, 6) | 1 PIOR (1) | 4 PIOR (1, 2, 4, 6) |
| conferência 1 (r13) | 3 PIOR (1, 2, 6) | 3 PIOR (1, 2, 5) | 3 PIOR (1, 3, 6) |
| 14 | 2 PIOR (1, 2) | 1 PIOR (1) | 3 PIOR (1, 4, 6) |
| 15 | 3 PIOR (1, 2, 6) | 1 PIOR (1) | 2 PIOR (2, 4) |
| 16 | 2 PIOR (1, 4) | 1 PIOR (1) | 1 PIOR (6) |
| 17 | 1 PIOR (1) | 2 PIOR (1, 4) | 1 PIOR (1) |
| **conferência 2 (r17)** | **2 PIOR (1, 3)** | **2 PIOR (1, 2)** | **1 PIOR (6)** |

Depois do pedido do usuário (corpo bom, olhos e boca estranhos), o rosto foi refeito nas rodadas 4 a 8. Na rodada 8 o critério 4 (rosto) passou nos três; na 9 passou na Phoenix e no Dragon. A paleta (5) passou em todas as rodadas de 3 a 11; na 12 e na conferência 1 o Lava Titan reprovou nela (lilás na 12, cinza claro demais na conferência 1). As rodadas 10 a 17 foram julgadas pelo revisor de cada thread de refino (vereditos em `Lava Titan/vereditos rodadas 10 a 17.md`, `Molten Dragon/entrega.md` e `Volcanic Phoenix/LEIA-ME.md`), com folhas em `<Pet>/folhas/`; as conferências 1 e 2 tiveram revisores novos, um por pet.

## Folhas da rodada 9

![[Recursos/Pets lendarios e miticos/Volcanic Phoenix/folhas/VolcanicPhoenix_comparacao_rodada9.png]]
![[Recursos/Pets lendarios e miticos/Volcanic Phoenix/folhas/VolcanicPhoenix_comparacao_fx_rodada9.png]]
![[Recursos/Pets lendarios e miticos/Lava Titan/folhas/LavaTitan_comparacao_rodada9.png]]
![[Recursos/Pets lendarios e miticos/Lava Titan/folhas/LavaTitan_comparacao_fx_rodada9.png]]
![[Recursos/Pets lendarios e miticos/Molten Dragon/folhas/MoltenDragon_comparacao_rodada9.png]]
![[Recursos/Pets lendarios e miticos/Molten Dragon/folhas/MoltenDragon_comparacao_fx_rodada9.png]]

As folhas das rodadas 1 a 8 estão na mesma pasta `folhas/` de cada pet (a rodada 8 é a de melhor resultado para Titan e Dragon).

## O que falta (depois da conferência 2)

- **Volcanic Phoenix (1, 3):** asas com penas em camadas e espessura; cauda em leque com volume (de lado ainda lê como tábua); segunda camada de detalhe (penas de brasa ou placas maiores no peito); peito e ombros mais largos, pernas e garras mais grossas, para ter o porte de Legendary sem depender das asas.
- **Lava Titan (1, 2):** acento nos espinhos das costas e um segundo tom de rocha; fissuras acesas na cabeça, nos antebraços e nos punhos, para a vista de lado mostrar rosto e braço; placas maiores com juntas laranja mais grossas, no traço da Phoenix e do Dragon; ícone sem o halo exclusivo e com a mesma margem dos outros.
- **Molten Dragon (6):** ícone com o pet enchendo 85 a 90% do quadro, de frente ou 3/4 com as asas abertas, com luz de borda laranja ou dourada para separar do fundo escuro.
- **Pedido novo do usuário:** menos cara de brinquedo, mais realismo, mesmo estilo (rodadas 18 em diante), seguindo a regra de corrigir um PIOR mudando a forma e testando mais de um estilo (seção acima).
- **Decisões do usuário:** se o Lava Titan pode reorganizar as placas do corpo (a thread dele perguntou e ficou sem resposta); um enquadramento único de ícone para o lote; e ligar o computer use no PC para os prints do Studio.

## O que faltava depois da conferência 1

- **Os três, critério 1:** cada um precisa de pontos de foco e peças secundárias, não uma só textura de placas no corpo todo (o pumpkin-golem e o bone-emperor têm vários materiais e uma área que chama atenção).
- **Traço comum das placas (critério 2):** escolher um só método de placas e fendas para os três e aplicar também na cabeça. Hoje a Phoenix lê como favo arredondado, o Titan como cacos soltos com cabeça lisa e o Dragon como células.
- **Volcanic Phoenix:** penas de pedra com borda acesa nas asas, gola no peito, leque de cauda com várias penas, pernas e garras mais grossas, bico entreaberto com brilho; rim light ou pedra um pouco mais clara para o ícone no fundo escuro; anel no chão mais forte.
- **Lava Titan:** cabeça com as mesmas placas e fendas do corpo e no tom do tronco; punhos com nós, ombros e pernas separados dos braços de frente; veias contínuas; escurecer o grafite até o tom de Phoenix e Dragon (na faixa de 128 px ele lê cinza médio); ícone com a mesma margem dos outros e sem halo exclusivo.
- **Molten Dragon:** elemento em volta grande o bastante para o ícone (pedras de lava maiores e acesas, ou chama); placas maiores no dorso e peito, brilho concentrado no peito, garganta e boca; dourado mais grosso; ícone a 3/4 de frente com os dois olhos e o pet preenchendo o quadro.
- **Prints do Studio:** ligar o computer use no PC do usuário para importar os GLB e tirar os prints dentro do jogo.
- **Regra do ícone:** decidir um enquadramento único de ícone para o lote. Os revisores alternaram entre "pet inteiro com margem" e "cabeça grande".

## O que faltava no fim da rodada 9

- **Volcanic Phoenix:** cabeça perto de 1/3 da altura e um ponto focal no peito; placas maiores no peito e nos ombros; asas com volume (ombro e antebraço), para não virarem lâmina de lado; pernas mais grossas; ícone fechado na cabeça, com olhos de 8 a 10 px e luz de contorno.
- **Lava Titan:** cabeça maior e mais à frente dos ombros; detalhe secundário nas placas (variação de tom, chanfros, fissuras finas internas); espinhos grossos na base e sem ponta acesa.
- **Molten Dragon:** fendas acesas no tronco, nas patas e na cauda, na densidade do Titan, com placas angulosas; ícone com o pet inteiro a 3/4 e margem de 8 a 10% (o revisor da rodada 8 pediu o contrário, a cabeça grande com as asas cortadas).
- **Prints do Studio:** ligar o computer use no PC do usuário para importar os GLB e tirar os prints dentro do jogo.
- **Regra do ícone:** decidir um enquadramento único de ícone para o lote. Os revisores alternaram entre "pet inteiro com margem" e "cabeça grande".

## Padrão do lote (decidido entre as rodadas)

Obsidiana/basalto cinza-ardósia a violeta-escuro fosco; rede contínua de fendas laranja-lava finas entre placas grandes; uma só cor de brilho; olhos emissivos amarelo-laranja em órbita funda sob sobrancelha de pedra, como ponto mais forte (Dragon com pupila em fenda); boca recortada com brilho de lava por dentro; dourado só no Mythic; ícone em fundo transparente com luz de recorte.

## Onde o Steal An Egg ainda é melhor (rodadas 8 e 9)

- **Centro de atenção:** a cara acesa do pumpkin-golem e o olho do voidseer-pumpkin dominam o pet; a cabeça dos pets do lote ainda é pequena (Phoenix ~1/5 da altura, Titan afundado nos ombros).
- **Camadas de material:** o pumpkin-golem mistura casca, cipó, espinho e folha; os pets do lote são um tipo de placa lisa.
- **Ornamento do Mythic:** o dourado do bone-emperor é volumoso (garras, ombreiras, coroa grossa); no Molten Dragon são frisos e argolas finas que somem a 128 px.
- **Ícone:** os SAE se leem numa olhada nos dois fundos; os ícones do lote dependem de detalhe pequeno e o corpo escuro afunda no fundo escuro.
- **Pose e massa:** abomination-kong e graveyard-brute têm punhos e postura de ataque; Titan de lado e Phoenix ficam parados.

## Vereditos completos do revisor independente

### Conferência 2 do lote (os três na rodada 17)

#### Volcanic Phoenix (Legendary, rodada 17) — REPROVADO (2 PIOR: 1, 3)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | pumpkin-golem | O golem tem três camadas de material (escamas, cipós com espinhos, rosto aceso); a Phoenix tem um só, células cinza do mesmo tamanho com fissuras laranja; asas em lâminas pretas planas sem volume de pena; na vista 3 a cauda é uma tábua cinza com ponta laranja. |
| 2 Coerência com o lote | IGUAL | graveyard-brute / LavaTitan, MoltenDragon | Células poligonais cinza, fissuras laranja finas e olhos amarelos angulados no mesmo traço e densidade do Titan e do corpo do Dragon. |
| 3 Escada de raridade | PIOR | graveyard-brute / LavaTitan | Corpo em ovo estreito com pernas finas; a largura vem só das asas; ao lado da massa do graveyard-brute e do Titan, parece um degrau abaixo. |
| 4 Brilho só onde importa | IGUAL | abomination-kong | Corpo fosco, brilho só no laranja das fissuras e da crista; olhos amarelos com sobrancelha angulada legíveis nas vistas 1 e 2. |
| 5 Paleta da área | IGUAL | graveyard-brute | Cinza-escuro com laranja igual ao Titan e ao Dragon; o lote se reconhece pela cor. |
| 6 Ícone 128 px | IGUAL | graveyard-brute | Lê ave de asas abertas com crista laranja; os dois olhos aparecem nos dois fundos; ressalva: ocupa pouco do quadro e a cauda se perde. |

Com efeitos: chamas nas pontas, faíscas, brilho no peito e anel no chão, mas o anel é bem mais fraco que os do Titan e do Dragon.
Onde o SAE é melhor: material secundário e textura de superfície (pumpkin-golem); peça de destaque com volume (cristais do graveyard-brute); porte largo e pesado; rosto grande como ponto focal no ícone.
Correções que faltam: asas com penas em camadas e espessura, cauda em leque com volume; segunda camada de detalhe (penas de brasa ou placas maiores no peito); peito e ombros mais largos, pernas e garras mais grossas; opcional: cabeça e olhos maiores no ícone.

#### Lava Titan (Legendary, rodada 17) — REPROVADO (2 PIOR: 1, 2)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | pumpkin-golem | O golem tem 3 materiais com textura; o Titan é um só material grafite facetado e liso; os espinhos das costas têm o preto do corpo e somem; na vista 3 cabeça e punho erguido viram um amontoado de pedras sem rachadura, sem leitura de rosto nem de braço. |
| 2 Coerência com o lote | PIOR | graveyard-brute / VolcanicPhoenix, MoltenDragon | Phoenix e Dragon têm placas grandes quase hexagonais com junta laranja grossa; o Titan tem muitos cacos pequenos e soltos com frestas finas mais amareladas; no ícone é o único com halo laranja em volta. |
| 3 Escada de raridade | IGUAL | graveyard-brute | Corpo largo e atarracado com ombros e punhos grandes, fissuras laranja no tronco e nas pernas, sem coroa nem dourado. |
| 4 Brilho só onde importa | IGUAL | abomination-kong | Corpo fosco, brilho numa família quente; olhos amarelos bravos legíveis de frente e a 3/4. |
| 5 Paleta da área | IGUAL | graveyard-brute | Os três se reconhecem pelo preto-grafite com laranja-lava. |
| 6 Ícone 128 px | IGUAL | abomination-kong | Olhos e boca acesa se leem nos dois fundos; silhueta de gorila curvado com espinhos; ressalva: encosta na borda do quadro. |

Com efeitos: só um anel de lava no chão e poucas brasas nas costas; não corrige a vista de lado sem brilho na cabeça e nos braços.
Onde o SAE é melhor: textura de superfície e material secundário (pumpkin-golem); acentos de cor que destacam a silhueta (cristais do graveyard-brute); leitura de qualquer ângulo; ícone com margem e sem contorno extra.
Correções que faltam: acento nos espinhos (ponta acesa ou rachadura) e segundo tom de rocha; fissuras acesas na cabeça, antebraços e punhos para o perfil mostrar rosto e braço; placas maiores e juntas laranja mais grossas no tom dos outros dois; tirar o halo do ícone (ou aplicar nos três) e dar a mesma margem.

#### Molten Dragon (Mythic, rodada 17) — REPROVADO (1 PIOR: 6)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | IGUAL | bone-emperor | Mesmos elementos de topo: coroa dourada com cristal, asas grandes com bordo dourado, faixas douradas nas pernas; corpo todo em placas de pedra e membrana com padrão hexagonal laranja; nem mais simples nem mais carregado. |
| 2 Coerência com o lote | IGUAL | bone-emperor / VolcanicPhoenix, LavaTitan | Mesma pedra carvão em placas com fissuras laranja e mesmos olhos amarelos; ressalva: fissuras do Dragon mais finas e puxando para o vermelho, as do Titan mais largas e amarelo-laranja. |
| 3 Escada de raridade | IGUAL | bone-emperor | Coroa dourada, chifres com pontas douradas, asas e pedras de lava flutuando dos dois lados na vista 1; corpo mais largo do lote; a peça em volta é discreta e some na vista 3. |
| 4 Brilho só onde importa | IGUAL | voidseer-pumpkin | Corpo fosco, brilho numa cor só; dois olhos amarelos grandes e legíveis na vista 1. |
| 5 Paleta da área | IGUAL | bone-emperor / voidseer-pumpkin | Os três do Volcano se reconhecem pelo carvão com laranja, como o trio Divine pelo roxo com dourado. |
| 6 Ícone 128 px | PIOR | bone-emperor | O Dragon ocupa bem menos o quadro que os SAE, com espaço vazio dos lados; no fundo escuro o corpo carvão se mistura e asas e patas se perdem; só a coroa e os olhos aparecem. |

Com efeitos: anel dourado, chamas nas costas, faíscas e brilho na coroa somam sem cobrir o rosto; o ícone é o mesmo nas duas folhas.
Onde o SAE é melhor: muito mais massa dourada no bone-emperor; contorno escuro e cor saturada; fissuras grossas e saturadas no voidseer; ícones que ocupam o quadro todo.
Correções que faltam: ícone com o pet ocupando 85 a 90% do quadro, de frente ou 3/4 com as asas abertas; rim light ou contorno laranja ou dourado para separar do fundo escuro; opcional: coroa maior ou dourado nas garras e pontas das asas.

### Conferência 1 do lote (os três na rodada 13, pedra grafite)

#### Volcanic Phoenix (Legendary, rodada 13) — REPROVADO (3 PIOR: 1, 2, 6)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | pumpkin-golem | Uma só camada de pedra em placas num corpo de ovo; cauda em duas lâminas finas; pernas e garras como palitos; sem efeitos lê como corvo gordo de pedra, não fênix. |
| 2 Coerência com o lote | PIOR | graveyard-brute / LavaTitan, MoltenDragon | Material e veios combinam, mas as placas são arredondadas e regulares (favo de mel) contra lascas facetadas e irregulares do Titan e do Dragon; rosto é esfera lisa com olhos e bico, sem boca esculpida. |
| 3 Escada de raridade | IGUAL | graveyard-brute | Veios laranja no corpo todo como os veios ciano do Brute; sem dourado, que fica para o Mythic; corpo largo. |
| 4 Brilho só onde importa | IGUAL | abomination-kong | Pedra fosca, brilho numa família laranja-amarelo; dois olhos amarelos com sobrancelha brava legíveis nas vistas 1 e 2. |
| 5 Paleta da área | IGUAL | abomination-kong | Os três do Volcano se reconhecem pelo carvão com laranja antes da forma. |
| 6 Ícone 128 px | PIOR | graveyard-brute | No fundo claro lê pássaro com crista e olhos; no escuro o corpo carvão some e sobram veios, olhos e crista; o ícone escuro mais fraco da linha. |

Com efeitos: chamas nas pontas das asas, crista e cauda dão identidade de fênix, mas o anel no chão quase não aparece perto do anel do Titan.
Onde o SAE é melhor: vários materiais e peças secundárias (pumpkin-golem); silhueta pesada com punhos e ombros; contorno e valor mais claro no fundo escuro (graveyard-brute); rosto com boca e dentes.
Correções que faltam: penas de pedra em placas com borda acesa nas asas, gola no peito e leque de cauda com várias penas; pernas e garras mais grossas; lascas facetadas irregulares como Titan e Dragon; rosto esculpido (sulco de sobrancelha, bico entreaberto com brilho dentro); rim light ou pedra um pouco mais clara para o ícone escuro; anel no chão tão forte quanto o do Titan.

#### Lava Titan (Legendary, rodada 13) — REPROVADO (3 PIOR: 1, 2, 5)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | graveyard-brute | Braços descem até o chão como colunas de placas soltas, sem punho visível na vista 1; peito e pernas não se separam dos braços; cabeça cinza lisa de facetas grandes parece outro modelo colado no corpo de cacos. |
| 2 Coerência com o lote | PIOR | graveyard-brute / VolcanicPhoenix, MoltenDragon | Phoenix e Dragon têm placas pretas com linhas laranja finas e contínuas, também na cabeça; o Titan tem cacos 3D soltos com brilho só nas frestas e a cabeça sem nenhuma linha. |
| 3 Escada de raridade | IGUAL | graveyard-brute | Corpo largo e mais maciço que a Phoenix, fissuras laranja fortes em braços e tronco, sem coroa nem dourado; ressalva: fissuras curtas e picotadas. |
| 4 Brilho só onde importa | IGUAL | pumpkin-golem | Corpo fosco, brilho laranja-amarelo; olhos grandes e boca com dentes acesos se leem como a cara acesa do pumpkin-golem. |
| 5 Paleta da área | PIOR | graveyard-brute / VolcanicPhoenix, MoltenDragon | Na faixa de 128 px o Titan é cinza médio, com a cabeça mais clara; Phoenix e Dragon são quase pretos com laranja; pela cor lembra mais o graveyard-brute que o lote. |
| 6 Ícone 128 px | IGUAL | abomination-kong | Olhos amarelos e boca acesa se leem nos dois fundos; silhueta de gorila-golem; ressalva: único ícone com halo claro e enquadramento colado nas bordas. |

Com efeitos: anel laranja fino no chão e brasas nos espinhos das costas; mais discreto que as chamas e o anel dourado do Dragon.
Onde o SAE é melhor: anatomia com punhos, ombros e pernas separados; veias contínuas que cruzam cabeça, peito e braços; cabeça do mesmo material do corpo; elemento de assinatura na silhueta do ícone.
Correções que faltam: cabeça com as mesmas placas e fissuras do corpo e no quase-preto do tronco; peito, ombros e punhos com nós, pernas separadas dos braços de frente; veias contínuas em vez de frestas picotadas; escurecer o cinza até o tom de Phoenix e Dragon e aumentar a área de laranja; ícone com a mesma margem dos outros e sem halo exclusivo.

#### Molten Dragon (Mythic, rodada 13) — REPROVADO (3 PIOR: 1, 3, 6)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | bone-emperor | A mesma malha de rachaduras laranja cobre corpo, asas, cauda e cabeça, sem área de foco; dourado só na coroa e em faixas finas nas pernas; na vista 1 as asas de frente viram hastes finas e o corpo fica quadrado; fica perto demais do Lava Titan (Legendary). |
| 2 Coerência com o lote | IGUAL | voidseer-pumpkin | Mesma pedra cinza-escura fosca, mesmo traço de rachadura em células e mesmos olhos amarelos em amêndoa do Titan e da Phoenix; densidade igual à da Phoenix. |
| 3 Escada de raridade | PIOR | voidseer-pumpkin | Coroa dourada se lê, mas a peça em volta são duas pedrinhas escuras que somem na vista 3 e no ícone; no Voidseer as chamas em volta ocupam quase a área do corpo e seguem legíveis a 128 px. |
| 4 Brilho só onde importa | IGUAL | bone-emperor | Corpo fosco, brilho numa família laranja; olhos amarelos mais legíveis que os do crânio do Bone Emperor na vista 1; ressalva: focinho e membrana puxam para o vermelho na vista 3. |
| 5 Paleta da área | IGUAL | cursed-monarch-rainbow | Os três se reconhecem pelo cinza-escuro com rachadura laranja e olho amarelo; o dourado soma sem quebrar a paleta. |
| 6 Ícone 128 px | PIOR | voidseer-pumpkin | Ícone de lado e comprido, canto de cima vazio, só um olho visível como pontinho; no fundo escuro asas e corpo se misturam ao fundo. |

Com efeitos: anel dourado no chão, chamas nas costas e brilho na coroa somam pouco; Titan e Phoenix também têm anel, então o efeito não marca o Mythic; nada de efeito aparece no ícone.
Onde o SAE é melhor: hierarquia de formas com pontos de foco (bone-emperor); dourado grosso visível de longe; elemento em volta que faz parte da silhueta (voidseer-pumpkin); ícones que preenchem o quadro com foco central.
Correções que faltam: elemento em volta grande o bastante para o ícone (pedras de lava maiores e acesas em órbita ou chama em volta); quebrar a malha uniforme com placas maiores no dorso e peito e brilho concentrado no peito, garganta e boca; dourado mais grosso em chifres ou garras das asas; ícone a 3/4 de frente com os dois olhos e o pet preenchendo o quadro, com luz de contorno; focinho e asas no laranja do corpo, sem vermelho.

O revisor recebeu só a folha da rodada e esta régua, abriu as imagens antes de responder e não viu a opinião de quem fez o pet. Um revisor novo a cada rodada.

### Rodada 9 (última). Titan e Dragon: só o ícone mudou, modelo igual à rodada 8. Phoenix: tronco maior, rede de fendas, crista laranja-brasa.

#### Lava Titan (Legendary) — REPROVADO (2 PIOR: 1, 4)

Observação: o modelo, os prints e os efeitos são os mesmos da rodada 8, quando outro revisor deu IGUAL em 1 e 4. Só o ícone mudou, e agora passou.

| Critério | Veredito | Pet SAE | Motivo |
|---|---|---|---|
| 1 Nível do degrau | PIOR | pumpkin-golem | Placas grandes lisas de um material só; cabeça pequena afundada nos ombros (rosto < 1/6 da altura); espinhos finos como palitos |
| 2 Coerência com o lote | IGUAL | graveyard-brute | Mesma placa facetada, fissura laranja e fosco do trio |
| 3 Escada de raridade | IGUAL | graveyard-brute | Largo e massivo, fissuras no corpo todo, sem coroa |
| 4 Brilho só onde importa | PIOR | graveyard-brute | Três focos competem: fissuras, rosto e pontas amarelas acesas de 5–6 espinhos |
| 5 Paleta | IGUAL | abomination-kong | Roxo-carvão + laranja agrupa os três ícones |
| 6 Ícone 128 px | IGUAL | graveyard-brute | Dois olhos e silhueta larga legíveis nos dois fundos |

Correções que faltariam: cabeça maior e mais à frente dos ombros; detalhe secundário nas placas (variação de tom, chanfros, fissuras finas internas); espinhos mais grossos na base e sem ponta acesa.

#### Molten Dragon (Mythic) — REPROVADO (2 PIOR: 2, 6)

Observação: modelo igual à rodada 8 (quando 2 foi IGUAL). O ícone novo segue a correção pedida na rodada 8 (cabeça grande, asas cortadas), e este revisor pediu o oposto (pet inteiro com margem).

| Critério | Veredito | Pet SAE | Motivo |
|---|---|---|---|
| 1 Nível do degrau | IGUAL | bone-emperor | Coroa com gema, asas com membrana em células e borda dourada, medalhão, argolas, pedras flutuando |
| 2 Coerência com o lote | PIOR | cursed-monarch-rainbow | Corpo, patas e cauda em pedras cinza arredondadas quase sem fenda acesa; laranja só nas asas, menos lava no corpo que os Legendary |
| 3 Escada de raridade | IGUAL | bone-emperor | Coroa, asas, chifres, medalhão, órbita de pedras, anel dourado e chamas no fx |
| 4 Brilho só onde importa | IGUAL | voidseer-pumpkin | Corpo fosco, brilho laranja só; dois olhos grandes legíveis nas três vistas |
| 5 Paleta | IGUAL | cursed-monarch-rainbow | Grafite + lava + olhos amarelos agrupa o trio |
| 6 Ícone 128 px | PIOR | voidseer-pumpkin | Ícone corta asa, coroa, patas e cauda; asa ocupa metade; halo claro no fundo escuro |

Correções que faltariam: fendas acesas no tronco, patas e cauda na densidade do Titan, placas angulosas; ícone com pet inteiro a 3/4, 8–10% de margem, sem halo claro.

#### Volcanic Phoenix (Legendary) — REPROVADO (2 PIOR: 1, 6)

| Critério | Veredito | Pet SAE | Motivo |
|---|---|---|---|
| 1 Nível do degrau | PIOR | pumpkin-golem | Bola de placas do mesmo tamanho sem centro de atenção; cabeça ~1/5 da altura; asas em leque chato que viram lâmina de lado; pernas finas sob o corpo |
| 2 Coerência com o lote | IGUAL | graveyard-brute | Mesma pedra, rachaduras laranja e olhos amêndoa do Titan e do Dragon; fendas um pouco mais grossas |
| 3 Escada de raridade | IGUAL | pumpkin-golem | Corpo largo, fissuras no corpo todo, sem coroa nem ouro; degrau para o Dragon visível |
| 4 Brilho só onde importa | IGUAL | abomination-kong | Corpo fosco, brilho numa família, olhos com pupila e sobrancelha legíveis de frente e a 3/4 |
| 5 Paleta | IGUAL | pumpkin-golem | Preto-roxo + laranja agrupa o trio |
| 6 Ícone 128 px | PIOR | pumpkin-golem | Cabeça pequena, olhos de poucos px; corpo some no fundo escuro |

Correções que faltariam: cabeça ~1/3 da altura e ponto focal no peito; placas maiores no peito e ombros; asas com volume (ombro e antebraço); pernas mais grossas; ícone mais justo na cabeça com olhos de 8–10 px e luz de contorno.

### Rodada 8 (Titan: cabeça integrada e boca recortada; Dragon: cabeça 1,6×, olhos laranja com fenda; Phoenix: máscara lisa, placas maiores, penas roxas)

#### Volcanic Phoenix (Legendary) — REPROVADO (4 PIOR: 1, 2, 3, 6)

| Critério | Veredito | Pet SAE | Motivo |
|---|---|---|---|
| 1 Nível do degrau | PIOR | pumpkin-golem | Bola de lascas roxas com manchas laranja soltas, asas finas em leque, pernas-palito; massa menor que os SAE |
| 2 Coerência com o lote | PIOR | graveyard-brute | Laranja em manchas e losango solto, não rede contínua de fendas finas como Titan/Dragon; roxo mais saturado |
| 3 Escada de raridade | PIOR | graveyard-brute | Corpo estreito e alto; crista amarelo-dourada lê como coroa de Mythic |
| 4 Rosto/brilho | IGUAL | abomination-kong | Corpo fosco, dois olhos amarelos grandes legíveis nas 3 vistas |
| 5 Paleta | IGUAL | pumpkin-golem | Escuro + laranja agrupa os 3 Volcano na faixa de ícones |
| 6 Ícone 128 px | PIOR | graveyard-brute | Tronco some no fundo escuro; olhos pequenos no quadro |

Correções: tronco maior e mais largo em relação às asas, pernas mais grossas; rede contínua de fendas finas entre placas, roxo puxado ao cinza-ardósia do Titan; crista laranja-brasa (sem dourado); borda/fendas acesas no contorno do tronco e olhos mais brilhantes para o ícone; efeitos mais fortes.

#### Molten Dragon (Mythic) — REPROVADO (1 PIOR: 6)

| Critério | Veredito | Pet SAE | Motivo |
|---|---|---|---|
| 1 Nível do degrau | IGUAL | bone-emperor | Placas recortadas, asas com borda dourada e veias, coroa de 3 pontas, chifres, pedras de lava em órbita |
| 2 Coerência com o lote | IGUAL | bone-emperor | Mesma pedra, fissura laranja e olhos amarelos com pupila do Titan/Phoenix; ouro como marca de Mythic |
| 3 Escada de raridade | IGUAL | bone-emperor | Coroa, asas, chifres, órbita de pedras, anel dourado e chamas no fx; chifres ainda cinza |
| 4 Rosto/brilho | IGUAL | voidseer-pumpkin | Corpo fosco, brilho numa cor; dois olhos grandes legíveis nas vistas 1 e 2 |
| 5 Paleta | IGUAL | voidseer-pumpkin | Cinza-escuro + laranja agrupa o lote |
| 6 Ícone 128 px | PIOR | voidseer-pumpkin | Ícone de lado com asa na metade esquerda, cabeça pequena, um olho só; corpo some no fundo escuro |

Correção: ícone a 3/4 de frente, cabeça ≥ 1/3 do quadro com os dois olhos, rim light ou contorno claro; pode recortar as asas.

#### Lava Titan (Legendary) — REPROVADO (1 PIOR: 6)

| Critério | Veredito | Pet SAE | Motivo |
|---|---|---|---|
| 1 Nível do degrau | IGUAL | graveyard-brute | Placas facetadas com rachaduras acesas, espinhos, punhos pesados; rosto lê melhor (olhos amarelos, boca laranja com dentes) |
| 2 Coerência com o lote | IGUAL | pumpkin-golem | Mesmas placas, fissuras e olhos de Phoenix e Dragon |
| 3 Escada de raridade | IGUAL | abomination-kong | O mais largo do lote, fissuras no corpo todo, sem coroa |
| 4 Rosto/brilho | IGUAL | graveyard-brute | Brilho numa família quente; olhos mais legíveis que os do brute |
| 5 Paleta | IGUAL | pumpkin-golem | Pedra ameixa + laranja + amarelo agrupa o trio |
| 6 Ícone 128 px | PIOR | graveyard-brute | Enquadramento apertado numa caixa roxa: espinhos e pés tocam a borda; único ícone com fundo próprio |

Correção: câmera mais afastada, corpo inteiro com 8–10% de margem, sem tocar a moldura.

### Rodada 7 (olho afundado de tamanho médio, boca aberta, Phoenix em placas de pedra)

#### Lava Titan (Legendary) — REPROVADO (3 PIOR)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | graveyard-brute | Corpo com peso de golem; cabeça é caixa achatada e a boca um bloco laranja liso que de lado parece gaveta solta. |
| 2 Coerência com o lote | IGUAL | graveyard-brute | Mesmas placas roxo-escuras facetadas e fissuras laranja nos três. |
| 3 Escada de raridade | IGUAL | abomination-kong | Postura larga, braços até o chão, fissuras laranja; sem coroa. |
| 4 Brilho e rosto | PIOR | pumpkin-golem | Olhos são elipses pequenas que viram ponto a 3/4 e de lado; boca é faixa chapada sem brilho nem recorte. |
| 5 Paleta da área | IGUAL | pumpkin-golem | Roxo-carvão com rede de fissuras laranja nos três, inclusive nos ícones. |
| 6 Ícone 128 px | PIOR | abomination-kong | Silhueta se lê, mas a cabeça some no corpo; olhos viram pontinhos e a barra da boca é o que mais aparece. |
Onde o SAE é melhor: rosto como foco; cabeça integrada com volume e expressão; cabeça separada do corpo no ícone; acessórios que fazem parte do desenho.

#### Molten Dragon (Mythic) — REPROVADO (3 PIOR)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | bone-emperor | Corpo, asas e coroa no nível; cabeça é cunha pequena para o corpo; olho em disco liso; boca vermelho-salmão chapada com dentes esparsos. |
| 2 Coerência com o lote | IGUAL | bone-emperor | Mesmo material e densidade de placas do Titan e da Phoenix; olho um pouco diferente. |
| 3 Escada de raridade | IGUAL | bone-emperor | Coroa com cristal, chifres, asas com borda dourada, anéis, pedras flutuando; com efeitos anel e chamas. |
| 4 Brilho e rosto | PIOR | voidseer-pumpkin | Olhos ovais pequenos na lateral; a 3/4 só um, sem brilho; interior da boca rosado compete com os olhos. |
| 5 Paleta da área | IGUAL | cursed-monarch-rainbow | Pedra escura, lava e dourado reconhecíveis como Volcano. |
| 6 Ícone 128 px | PIOR | voidseer-pumpkin | Silhueta funciona; cabeça some no fundo escuro e o olho vira um pixel. |
Onde o SAE é melhor: rosto como ponto focal; contraste da silhueta; expressão da boca; hierarquia de cor (olho no mesmo amarelo do dourado).

#### Volcanic Phoenix (Legendary) — REPROVADO (4 PIOR: 1, 2, 4, 6)

| Critério | Veredito | Pet SAE | Motivo |
|---|---|---|---|
| 1 Forma/material | PIOR | pumpkin-golem | Seixo igual do bico à cauda; asas em leque liso e fino; lê como "pombo de pedra" |
| 2 Coerência com o lote | PIOR | graveyard-brute | Seixos pequenos e densos com manchas laranja largas, não veios finos; único pet com penas vermelho-alaranjadas |
| 3 Escada de raridade | IGUAL | graveyard-brute | Corpo largo, asas abertas, fissuras e losango no peito, sem dourado |
| 4 Rosto | PIOR | abomination-kong | Olhos em cunha amarela sem órbita; bico do mesmo amarelo gruda nos olhos; garras douradas e penas vermelhas competem |
| 5 Paleta | IGUAL | pumpkin-golem | Roxo escuro + laranja reconhecível; vermelho das asas é desvio pequeno |
| 6 Ícone 128 px | PIOR | graveyard-brute | Asas somem no fundo escuro; olhos com 1–2 px |

Correções: cabeça em material próprio (máscara lisa ou placas grandes, sem seixos), asas em camadas com bordas grossas e veios, crista e cauda mais longas em chamas; placas do tamanho do Titan com veios finos; penas roxo escuro com ponta laranja; órbitas fundas e olhos amêndoa maiores; bico escuro; garras escurecidas; borda das asas mais clara para o ícone; anel no chão mais forte.

### Rodada 6 (olhos com o dobro da altura, boca esculpida)

#### Volcanic Phoenix (Legendary) — REPROVADO (4 PIOR)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | pumpkin-golem | De lado, barriga, costas e cabeça são bola lisa roxa; penas do peito iguais e repetidas. |
| 2 Coerência com o lote | PIOR | graveyard-brute; LavaTitan, MoltenDragon | Corpo liso e arredondado vs. placas facetadas com junta laranja; bordas de pena laranja-neon mais saturadas que as juntas dos outros. |
| 3 Escada de raridade | IGUAL | abomination-kong | Rede de rachaduras no peito e barriga e asas abertas dão largura; de lado as rachaduras somem. |
| 4 Brilho e rosto | PIOR | pumpkin-golem | Olhos em disco com aro e centro escuro parecem óculos; bico pequeno sem boca; brilho dividido em amarelo, laranja-neon e dourado. |
| 5 Paleta da área | IGUAL | graveyard-brute | Roxo-escuro com laranja e amarelo no grupo do lote. |
| 6 Ícone 128 px | PIOR | pumpkin-golem | Asas e crista saem do quadro; corpo se perde no fundo escuro. |
Onde o SAE é melhor: rosto com expressão; nenhuma área lisa; massa e peso plantados; uma só cor de brilho.

#### Molten Dragon (Mythic) — REPROVADO (3 PIOR)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | bone-emperor | Corpo de pedra bem resolvido, mas a cabeça é bloco liso; asas finas e escuras somem atrás do corpo nas vistas 2 e 3. |
| 2 Coerência com o lote | IGUAL | voidseer-pumpkin | Mesmas placas cinza-escuras com fissuras laranja e mesmos olhos amarelos com contorno do Titan e da Phoenix. |
| 3 Escada de raridade | IGUAL | bone-emperor | Coroa dourada, anéis dourados, pedras de lava orbitando; com efeitos chamas e anel; hierarquia clara sobre os Legendary. |
| 4 Brilho e rosto | PIOR | voidseer-pumpkin | Olhos em discos chapados nas laterais da cabeça (de frente parecem fones); boca é laje reta com dentes só embaixo, sem interior. |
| 5 Paleta da área | IGUAL | cursed-monarch-rainbow | Os três se agrupam pelo cinza-escuro com laranja. |
| 6 Ícone 128 px | PIOR | voidseer-pumpkin | No fundo escuro o corpo se funde, asas não aparecem, só um olho visível. |
Onde o SAE é melhor: olhar com pupila e halo; boca aberta com interior brilhando; asas grandes com varetas douradas; contraste no ícone.

#### Lava Titan (Legendary) — REPROVADO (2 PIOR)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | pumpkin-golem | Corpo no nível; cabeça é caixa enterrada entre os ombros com tampa chata (capacete); boca em zigue-zague fino que some na sombra. |
| 2 Coerência com o lote | IGUAL | graveyard-brute | Mesmas placas foscas, mesmo traço de fissura e mesmos olhos nos três. |
| 3 Escada de raridade | IGUAL | abomination-kong | O mais largo e pesado do lote, fissuras no corpo todo, sem dourado de Mythic. |
| 4 Brilho só onde importa | PIOR | graveyard-brute | Olhos em discos amarelo-pálidos chapados como adesivos; pontas dos espinhos em outro amarelo; estrela do peito puxa o olho. |
| 5 Paleta da área | IGUAL | abomination-kong | Roxo-escuro + laranja reconhecível antes da forma. |
| 6 Ícone 128 px | IGUAL | graveyard-brute | Ícone ocupa o quadro, contorno laranja destaca no fundo escuro, olhos e espinhos aparecem. |
Onde o SAE é melhor: rosto aceso como foco; punhos com dedos legíveis; segundo material que quebra a massa; contorno escuro a 128 px.

### Rodada 5

#### Volcanic Phoenix (Legendary) — REPROVADO (4 PIOR)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | pumpkin-golem | Mesma malha de fissuras por igual no corpo, sem ponto focal; rosto lê como corvo (bico marrom opaco, olhos semicerrados); cabeça manchada de lado. |
| 2 Coerência com o lote | PIOR | graveyard-brute | Placas pequenas e arredondadas com fissuras finas e densas (casco de tartaruga) vs. placas grandes facetadas do Titan e do Dragon; cabeça lisa sem fissuras. |
| 3 Escada de raridade | IGUAL | graveyard-brute | Fissuras laranja sobre corpo escuro; asas abertas dão largura e presença. |
| 4 Brilho só onde importa | PIOR | abomination-kong | Brilho espalhado; olhos em fenda pequenos, de lado só um ponto; bico marrom-oliva fora da paleta. |
| 5 Paleta da área | IGUAL | pumpkin-golem | Os três do Volcano formam grupo roxo-escuro com laranja. |
| 6 Ícone 128 px | PIOR | pumpkin-golem | Cabeça some no fundo escuro, olhos viram pontinhos, bico some. |
Onde o SAE é melhor: hierarquia com um rosto como foco; disciplina de brilho; traço consistente da cabeça aos pés; base larga e plantada.

#### Molten Dragon (Mythic) — REPROVADO (4 PIOR)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | bone-emperor | Corpo no nível; de frente a boca é um triângulo vermelho liso, olhos ovais amarelos chapados, cabeça pequena, patas em coluna. |
| 2 Coerência com o lote | PIOR | bone-emperor; LavaTitan, VolcanicPhoenix | Fissuras finas amarelo-douradas (parecem friso de metal) vs. laranja grossas dos outros dois; pedra mais roxa, asas marrons. |
| 3 Escada de raridade | IGUAL | bone-emperor | Coroa com gema, asas com nervuras douradas, pedras orbitando; com efeitos anel de fogo e chamas. |
| 4 Brilho só onde importa | PIOR | voidseer-pumpkin | Três cores de brilho (olhos amarelos, boca vermelha, dourado); a boca vermelha aparece mais que os olhos. |
| 5 Paleta da área | IGUAL | cursed-monarch-rainbow | Os três do Volcano aparecem como grupo de pedra escura com linhas quentes. |
| 6 Ícone 128 px | PIOR | voidseer-pumpkin | Silhueta funciona; olhos viram pontinhos e o que aparece é o ponto vermelho da boca. |
Onde o SAE é melhor: rosto com olho grande que se lê de longe; extremidades com garras e cauda trabalhadas; disciplina de cor; asas contrastadas.

#### Lava Titan (Legendary) — REPROVADO (3 PIOR)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | pumpkin-golem | Corpo no nível; cabeça é caixa achatada tipo capacete com viseira; olhos em fenda fina; boca é faixa laranja reta. |
| 2 Coerência com o lote | IGUAL | graveyard-brute | Mesma pedra roxo-escura em placas com fissuras laranja dos outros dois. |
| 3 Escada de raridade | IGUAL | graveyard-brute | Corpo largo, punhos maiores que a cabeça, fissuras fortes e estrela-runa; sem dourado de Mythic. |
| 4 Brilho só onde importa | PIOR | abomination-kong | Olhos estreitos e meio escondidos pela aba, "cara de sono"; boca com o mesmo brilho das fissuras parece cinto. |
| 5 Paleta da área | IGUAL | pumpkin-golem | Roxo-escuro com laranja-lava, igual ao lote. |
| 6 Ícone 128 px | PIOR | pumpkin-golem | Contorno laranja separa do fundo, mas olhos viram pontinhos e a cabeça some entre os ombros. |
Onde o SAE é melhor: expressão clara no rosto; cristais que parecem cristais (os pilares parecem lápis); veias que seguem a forma; cabeça que se destaca no ícone.

### Rodada 4 (corpo mantido, olhos e boca refeitos a pedido do usuário)

#### Lava Titan (Legendary) — REPROVADO (2 PIOR)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | graveyard-brute, pumpkin-golem | Corpo no nível (placas densas, fissuras, cristais com ponta amarela), mas a cabeça é uma caixa pequena com olhos redondos, boca fina e torta e duas antenas finas; de lado vira bola com olho saltado. |
| 2 Coerência com o lote | IGUAL | graveyard-brute | Mesmo material roxo-escuro fosco e fissuras laranja dos outros dois; só os olhos são menores. |
| 3 Escada de raridade | IGUAL | abomination-kong | Corpo largo e pesado, fissuras laranja e estrela no peito; sem dourado de Mythic. |
| 4 Brilho só onde importa | PIOR | graveyard-brute | Corpo fosco e brilho laranja certos, mas olhos são discos sem expressão e a boca é um risco torto. |
| 5 Paleta da área | IGUAL | pumpkin-golem | Os três se reconhecem pelo roxo-escuro com laranja. |
| 6 Ícone 128 px | IGUAL | graveyard-brute | Borda laranja segura a silhueta nos dois fundos; cristais e olhos aparecem. |
Onde o SAE é melhor: rosto expressivo e ameaçador; contraste do brilho; cabeça integrada ao tronco; efeitos com mais peso.

#### Volcanic Phoenix (Legendary) — REPROVADO (4 PIOR)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | pumpkin-golem | De lado, costas e flanco lisos e manchados, sem fissuras nem penas; penas das asas em placas chapadas. |
| 2 Coerência com o lote | PIOR | graveyard-brute | Fissuras só no peito; resto liso com outro traço; pontas salmão chapadas. |
| 3 Escada de raridade | PIOR | abomination-kong | Fissuras presas ao peito; corpo redondo de "pombo gordinho", sem porte de Legendary. |
| 4 Brilho só onde importa | PIOR | pumpkin-golem | Olhos são discos amarelos enormes com pupila preta centrada, como óculos de coruja; bico pequeno sem expressão; pontas salmão competem. |
| 5 Paleta da área | IGUAL | pumpkin-golem | Roxo-escuro com laranja-lava, a mesma base do lote. |
| 6 Ícone 128 px | IGUAL | graveyard-brute | Asas com borda laranja marcam a silhueta e os olhos aparecem nos dois fundos. |
Onde o SAE é melhor: rosto com expressão; acabamento em todas as faces; porte de topo; riqueza de material.

#### Molten Dragon (Mythic) — REPROVADO (4 PIOR)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | bone-emperor | Corpo no nível; boca com fileira de dentinhos iguais que vira serrote de lado, sem luz; asas apagadas. |
| 2 Coerência com o lote | PIOR | cursed-monarch-rainbow | Olhos saltados com contorno claro e pupila, diferentes dos discos chapados do Titan e da Phoenix; disco colado na lateral na vista de lado. |
| 3 Escada de raridade | IGUAL | bone-emperor | Coroa, chifres e aros dourados, medalhão, pedras orbitando; com efeitos anel e chamas. |
| 4 Brilho só onde importa | PIOR | voidseer-pumpkin | Olhos de desenho animado que não parecem emitir luz; boca é buraco escuro. |
| 5 Paleta da área | IGUAL | voidseer-pumpkin / cursed-monarch-rainbow | Pedra escura, fissura laranja e olho amarelo nos três. |
| 6 Ícone 128 px | PIOR | voidseer-pumpkin | Ícone de perfil, cabeça pequena, olho vira ponto, boca some. |
Onde o SAE é melhor: rosto como ponto focal; ouro distribuído nas garras e asas; contorno em miniatura; hierarquia de formas.

### Rodada 3

#### Lava Titan (Legendary) — REPROVADO (3 PIOR)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | pumpkin-golem | O anel dourado do peito domina a vista 1; cabeça pequena sob uma aba; blocos planos sem textura; cristais roxos opacos somem no corpo. |
| 2 Coerência com o lote | IGUAL | abomination-kong | Mesma pedra roxa fosca, mesmas fissuras laranja e mesmo olho dos outros dois; ressalva: fissuras do Titan mais largas. |
| 3 Escada de raridade | IGUAL | abomination-kong | Corpo largo e pesado, braços até o chão, fissuras laranja; sem dourado de Mythic. |
| 4 Brilho só onde importa | PIOR | abomination-kong | Olhos brancos chapados, pequenos sob a aba, não brilham; anel dourado e cristais roxos disputam atenção. |
| 5 Paleta da área | IGUAL | pumpkin-golem | Os três se reconhecem pelo roxo-escuro com laranja, também nos ícones. |
| 6 Ícone 128 px | PIOR | graveyard-brute | Olhos viram pontinhos brancos; o que se lê é o anel do peito; corpo some no fundo escuro. |
Onde o SAE é melhor: rosto legível em qualquer tamanho; textura de superfície; acento e olhos na mesma cor; efeitos fracos (anel quase invisível na vista 1).

#### Molten Dragon (Mythic) — REPROVADO (3 PIOR)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | bone-emperor | Quatro pernas retas como colunas e pose dura; membranas escuras somem no corpo; faixas douradas com bolas parecem coladas; cabeça pequena. |
| 2 Coerência com o lote | IGUAL | bone-emperor | Mesmas placas de pedra com fissuras quentes e mesmos olhos dos outros dois; o dourado a mais é o que a regra 3 pede para o Mythic. |
| 3 Escada de raridade | IGUAL | bone-emperor | Coroa com gema, chifres dourados, asas com borda dourada, pedras flutuando; com efeitos anel e chamas. |
| 4 Brilho só onde importa | PIOR | bone-emperor | Olhos brancos de desenho que não brilham; brilho dividido entre metal dourado e fissuras. |
| 5 Paleta da área | IGUAL | voidseer-pumpkin / cursed-monarch-rainbow | Os três do Volcano se reconhecem pela pedra escura arroxeada com brilho quente, também a 128 px. |
| 6 Ícone 128 px | PIOR | voidseer-pumpkin | O ícone da folha usa a vista de frente: lê "coroa + dois olhos brancos"; corpo some no fundo escuro. |
Onde o SAE é melhor: olhar que brilha; silhueta e pose; hierarquia de cor; força do ícone.

#### Volcanic Phoenix (Legendary) — REPROVADO (4 PIOR)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | pumpkin-golem | Low-poly facetada; na vista de lado cabeça e corpo viram massa amassada; pernas finas; asa de lado é placa chapada. |
| 2 Coerência com o lote | PIOR | graveyard-brute / LavaTitan, MoltenDragon | Rachaduras finas irregulares sobre facetas, sem as placas com juntas grossas dos outros dois. |
| 3 Escada de raridade | IGUAL | graveyard-brute | Rachaduras numa só cor forte pelo corpo todo; envergadura dá largura; sem coroa. |
| 4 Brilho só onde importa | PIOR | pumpkin-golem | Olhos são discos brancos que não emitem; rachaduras passam por cima do rosto; pontas laranja, bico e losango dourado competem. |
| 5 Paleta da área | IGUAL | abomination-kong | Os três se reconhecem pelo roxo-escuro com laranja na faixa de ícones. |
| 6 Ícone 128 px | PIOR | pumpkin-golem | No fundo escuro só a franja das asas desenha a silhueta; cabeça pequena; olhos viram pontinhos brancos. |
Com efeitos: chamas nas pontas funcionam, mas duas flutuam soltas na vista de lado; falta anel no chão como nos outros dois.
Onde o SAE é melhor: microdetalhe de superfície; rosto como foco; silhueta limpa em qualquer vista; leitura no ícone escuro.

### Rodada 2

#### Lava Titan (Legendary) — REPROVADO (4 PIOR)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | graveyard-brute | Cabeça pequena afundada entre os ombros; braços se confundem com tronco e pernas; lê como parede de pedras. |
| 2 Coerência com o lote | PIOR | pumpkin-golem / VolcanicPhoenix, MoltenDragon | Sem efeitos combina (roxo fosco + fissuras laranja), mas blocos grandes com vãos vs. superfície contínua dos outros; com efeitos não tem anel no chão nem chama, só fumaça cinza fraca. |
| 3 Escada de raridade | IGUAL | abomination-kong | Corpo largo e maciço, fissuras fortes, sem dourado de Mythic; mais largo que a Phoenix. |
| 4 Brilho só onde importa | PIOR | graveyard-brute | Fissuras cobrem o corpo todo; olhos são fendas pequenas sob a aba; com efeitos tudo vira amarelo, mesma cor dos olhos. |
| 5 Paleta da área | IGUAL | pumpkin-golem | Os três do Volcano se reconhecem pelo roxo-escuro com fissuras laranja, também nos ícones. |
| 6 Ícone 128 px | PIOR | pumpkin-golem | Massa retangular roxa; olhos viram um ponto; cabeça não se distingue no fundo escuro. |
Onde o SAE é melhor: rosto como ponto focal; hierarquia do brilho; pose e personagem; variação de material.

#### Volcanic Phoenix (Legendary) — REPROVADO (4 PIOR)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | pumpkin-golem | Mesmo mosaico de placas cobre corpo, cabeça e asas; corpo de bola com bico de coruja e pernas finas; com efeitos não há fogo nas asas nem na cauda. |
| 2 Coerência com o lote | PIOR | graveyard-brute | Dezenas de células pequenas por asa e fissuras finas vermelho-laranja vs. placas grandes e fissuras grossas douradas no Titan e no Dragon. |
| 3 Escada de raridade | PIOR | graveyard-brute | Fissuras finas que mal se distinguem de pintura sem efeitos; tronco pequeno e redondo. |
| 4 Brilho só onde importa | PIOR | pumpkin-golem | 3 a 4 tons quentes competindo (olhos amarelo chapado, fissuras, pontas laranja, bico e garras dourados, losango). |
| 5 Paleta da área | IGUAL | abomination-kong | Os 3 do lote se agrupam pelo roxo-escuro com laranja na faixa de ícones. |
| 6 Ícone 128 px | IGUAL | abomination-kong | Asas abertas são a silhueta mais distinta da faixa e os olhos aparecem; no fundo escuro o miolo vira ruído. |
Onde o SAE é melhor: foco visual; brilho que lê como luz; separação de materiais; contorno no ícone.

#### Molten Dragon (Mythic) — REPROVADO (3 PIOR)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | bone-emperor | Parado sobre 4 pernas retas como pilares; cabeça pequena quase escondida pela coroa; olhos em placas lisas, boca só na vista 3; falta pose e carisma. |
| 2 Coerência com o lote | IGUAL | bone-emperor | Mesma pedra roxo-acinzentada com fissuras e olhos amarelos dos outros dois; ressalva: fissuras douradas vs. vermelho-laranja da Phoenix. |
| 3 Escada de raridade | IGUAL | bone-emperor | Coroa dourada com cristais, chifres dourados, asas, medalhões, pedras orbitando; com efeitos chamas e anel; sem efeitos as pedras em órbita somem. |
| 4 Brilho só onde importa | PIOR | voidseer-pumpkin | Fissuras cobrem 100% do corpo e das asas, mais dourado especular; olhos se perdem no amarelo da coroa. |
| 5 Paleta da área | IGUAL | cursed-monarch-rainbow | Os três do Volcano se reconhecem pela pedra escura com fissuras laranja-amarelas, também a 128 px. |
| 6 Ícone 128 px | PIOR | voidseer-pumpkin | Asas ocupam a largura, corpo pequeno; corpo some no fundo escuro; olhos colados na coroa. |
Onde o SAE é melhor: ponto focal; pose e atitude; silhueta com contorno; elementos em volta que brilham sem efeitos.

#### Padrão do lote revisado depois da rodada 2
Veias só nos veios principais (peito, garganta, juntas, bordas das asas), calibre médio igual nos três, grandes áreas de pedra fosca sem brilho; uma cor de brilho laranja-lava; olhos branco-amarelo quente com halo, maiores, o ponto mais forte e separados de qualquer dourado; dourado fosco; contorno escuro ou rim light quente; pose com atitude.

### Rodada 1 (31/10/2026, folhas com render do Blender) — todos REPROVADOS

#### Volcanic Phoenix (Legendary) — REPROVADO (6 PIOR)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | pumpkin-golem, abomination-kong | Tronco pequeno e estreito entre asas enormes; asas em placas facetadas com reflexos brancos; os SAE têm corpo maciço com detalhe de superfície em todo o corpo. |
| 2 Coerência com o lote | PIOR | graveyard-brute | Fissuras finas só no peito e barriga, asas e cauda roxas lisas; Titan e Dragon têm rede de fissuras no corpo todo. |
| 3 Escada de raridade | PIOR | abomination-kong | Corpo de passarinho; sem efeitos as fissuras parecem pintura, não luz. |
| 4 Brilho só onde importa | PIOR | graveyard-brute | Corpo roxo com reflexos especulares; brilho dividido entre amarelo e laranja; com efeitos a gema do peito rouba a atenção dos olhos. |
| 5 Paleta da área | PIOR | pumpkin-golem | Maior massa de cor é o leque amarelo, que não aparece nos outros pets do Volcano. |
| 6 Ícone 128 px | PIOR | pumpkin-golem | Corpo minúsculo no centro, olhos viram pontinhos, roxo some no fundo escuro. |
Onde o SAE é melhor: massa e presença; rosto como ponto focal; disciplina de cor; contraste no fundo escuro.

#### Lava Titan (Legendary) — REPROVADO (5 PIOR)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | graveyard-brute | Bloco de pedras hexagonais sem braços, mãos ou cabeça distinguíveis; juntas laranja quase tão grandes quanto as pedras. |
| 2 Coerência com o lote | PIOR | graveyard-brute | Cinza-claro com juntas grossas, enquanto Phoenix e Dragon são roxo-escuros. |
| 3 Escada de raridade | IGUAL | abomination-kong | O mais largo do lote, fissuras laranja fortes, sem coroa (certo para Legendary). |
| 4 Brilho só onde importa | PIOR | pumpkin-golem | Brilho em ~40% do corpo, em duas cores; olhos minúsculos; a estrela do peito chama mais que o rosto. |
| 5 Paleta da área | PIOR | abomination-kong | Único pet claro na faixa de ícones; não casa com o par roxo + laranja. |
| 6 Ícone 128 px | PIOR | graveyard-brute | Silhueta de retângulo de pedras, olhos invisíveis, cinza some no fundo claro. |
Onde o SAE é melhor: rosto; silhueta de brutamonte com punhos; contraste de valores; acento secundário que não compete com o rosto.

#### Molten Dragon (Mythic) — REPROVADO (5 PIOR)
| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | bone-emperor | Um único padrão de células de lava por todo o corpo; anéis finos, coroa pequena; nenhuma peça que chame atenção. |
| 2 Coerência com o lote | PIOR | cursed-monarch-rainbow | Fissuras largas e densas e asas cheias de laranja, enquanto a Phoenix tem linhas finas. |
| 3 Escada de raridade | PIOR | bone-emperor | Coroa pequena que some no ícone; chifres não dourados; nada em volta do corpo sem efeitos. |
| 4 Brilho só onde importa | PIOR | voidseer-pumpkin | Brilho no corpo inteiro; olhos pequenos nas laterais, não aparecem de frente; facetas com reflexo. |
| 5 Paleta da área | IGUAL | cursed-monarch-rainbow | Os três do Volcano se reconhecem pelo laranja sobre escuro. |
| 6 Ícone 128 px | PIOR | bone-emperor | De frente o focinho some e os olhos não aparecem; no fundo escuro sobra só a rede laranja. |
Onde o SAE é melhor: ponto de foco; variedade de materiais; elementos em volta do corpo; contraste no ícone.

#### Padrão do lote definido depois da rodada 1
Obsidiana/basalto violeta-escuro fosco + fissuras laranja-lava finas como veias, densidade média, brilho ≤ ~20% da superfície, uma só cor de brilho; olhos grandes e acesos como ponto mais forte; luz de borda quente.

## Conexoes

[[Regua Steal An Egg para os 21 pets]] · [[00 Remake dos pets lendarios e miticos]] · [[Volcanic Phoenix]] · [[Lava Titan]] · [[Molten Dragon]] · [[Climb for Pets]]
