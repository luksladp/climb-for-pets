---
area: modelos
tipo: ficha
resumo: Entrega do Molten Dragon (Mythic, Volcano) no lote 1 da régua Steal An Egg, na rodada 17 (olhos e boca refeitos no estilo do lote, cabeça nas mesmas placas do corpo; rodadas 16 e 17 com 1 PIOR cada, rosto aprovado) — GLB com rig de 30 ossos e 4 clipes, rochas de lava orbitando, maior malha 15 220 tris, 7 flipbooks de VFX, screenshots de frente, 3/4 e lado (render do Blender) e ícone 128 px.
termos: molten dragon rodada 17 rodada 16 rodada 10 olhos angulosos franzidos nucleo claro boca garganta acesa incisivos lingua placas organicas cabeca focinho chanfrado grafite sem lilas pedras lava orbita icone perspectiva v10 v9 cabeca maior focinho v8 pupila fenda sobrancelha asas maiores v7 olhos grandes carvao v6 olho padrao amendoa presas v5 olhos boca rosto v4 rodada 2 pose v3 correcao revisor entrega lote 1 volcano mythic glb rig clipes idle walk happy breath tris screenshots icone blender flipbook
---
# Molten Dragon: entrega do lote 1 (Volcano)

## Rodadas 10 a 17: olhos e boca (31/10/2026)

Pedido: o usuário achou os olhos e a boca o ponto fraco; corpo mantido. Oito rodadas com revisor independente (só a folha e a régua). Resultado: **não aprovado**, mas o rosto passou. Nas rodadas 16 e 17 sobrou 1 PIOR em cada uma, em critérios diferentes (ícone na 16, asas na 17).

| Rodada | PIOR | O que mudou |
| --- | --- | --- |
| 10 | 1, 2, 4, 6 | Olho de desenho em cúpula com pupila e ponto de luz; boca mais aberta com interior de lava e língua; dentes grossos; fendas acesas no corpo todo; ícone com o pet inteiro |
| 11 | 1, 2 | Olhos amarelos acesos sem aro escuro; fendas do corpo e das asas mais fracas que os olhos; topo da cabeça sem espinhos e chifres pequenos; faixas douradas grossas; ícone em perspectiva com a cabeça maior |
| 12 | 1, 2, 4 | Olho do lote: amarelo chapado, anguloso e franzido, sem pupila, sob sobrancelha de pedra; cabeça em placas sobre as facetas |
| 13 | 1, 2, 4, 6 | Cabeça coberta pelas mesmas placas do corpo (`plates.py` sobre a pele da cabeça e da mandíbula); focinho e queixo chanfrados; olho maior com núcleo claro; garganta acesa, língua com volume, fileiras contínuas de dentes; pedra em grafite sem lilás, como o Lava Titan da rodada 13 |
| 14 | 1, 4, 6 | Boca acesa em laranja; frestas da cabeça no laranja do corpo; coroa mais para trás; pedras de lava maiores; ponta dos chifres, garra e espinho do pulso das asas em ouro; brilho do corpo concentrado no peito, garganta e barriga; ícone mais de frente |
| 15 | 2, 4 | Boca escura na frente com a garganta acesa no fundo e incisivos; olhos maiores; placas maiores na cabeça; ouro só na borda da frente da asa; núcleo das pedras em laranja; ícone enchendo ~90% do quadro com contraluz |
| 16 | 6 | Pedras em órbita como rocha escura com frestas de lava (sem "cara de abóbora"); fumaça da narina translúcida e longe dos olhos; frestas da cabeça mais fracas |
| 17 | 1 | Olhos mais afastados, lado de dentro mais curto (ponte escura entre eles); ícone quase de frente; ouro mais saturado; faixas douradas mais grossas |

**Rosto final:** olhos amarelos angulosos e franzidos com núcleo claro, cada um no seu encaixe sob uma sobrancelha de pedra, maiores que o padrão anterior; boca aberta com garganta acesa que escurece para a frente, língua, oito dentes em cima e sete embaixo de cada lado com presa maior e incisivos na frente. Na rodada 17 o revisor deu IGUAL no brilho/rosto e no ícone.

**O que falta (rodada 17):** asas com membrana fechada até os dedos de baixo, sem varetas soltas nem treliça vista de frente, membrana no valor escuro do corpo e ponta dourada em cada dedo. O corpo e as asas não foram mexidos nessas rodadas, além do brilho das veias.

Totais da rodada 17: 39 576 tris, maior malha `plates` 15 220; rig de 30 ossos, mesmos 4 clipes (`Idle`, `Walk`, `Happy`, `Breath`). Mudanças nos efeitos em `emissores.md` (fumaça translúcida, faísca da coroa sem rosa). Folhas das rodadas 10 a 17 em `folhas/`; vereditos completos abaixo.

Como refazer: igual ao "Como refazer" abaixo (`core.py`, `build.py`, `rig.py`, `shots.py`), com Blender 5.2 em Python (`pip install bpy scikit-image scipy`). O `core.npz` é gerado pelo `core.py` e não vai para o Git.

### Vereditos do revisor independente, rodadas 10 a 17
#### Rodada 10 (olhos de desenho com pupila e ponto de luz, boca aberta com interior de lava, fendas acesas no corpo todo, ícone com o pet inteiro)

##### Molten Dragon (Mythic) — REPROVADO (4 PIOR: 1, 2, 4, 6)

| Critério | Veredito | Pet SAE | Motivo |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | bone-emperor | Corpo com placas densas, mas focinho em caixa de facetas lisas sem placas nem fissuras; topo da cabeça amontoa chifres, coroa, espinhos e cristas; aros dourados finos parecem bambolês |
| 2 Coerência com o lote | PIOR | bone-emperor | Titan e Phoenix têm olhos amarelos chapados que brilham; o Dragon tem esferas laranja com pupila e aro escuro que parecem óculos de frente |
| 3 Escada de raridade | IGUAL | bone-emperor | Coroa, chifres com anéis, asas com borda dourada, pedras flutuando, anel e chamas no fx |
| 4 Brilho só onde importa | PIOR | voidseer-pumpkin | Fendas no corpo todo e nas asas com a mesma força; olhos na mesma cor das fendas, não são o ponto mais claro; ouro e boca vermelha somam três acentos |
| 5 Paleta | IGUAL | voidseer-pumpkin | Cinza-escuro com laranja vulcânico; ouro de raridade |
| 6 Ícone 128 px | PIOR | voidseer-pumpkin | Silhueta lê, mas cabeça pequena no canto; olhos laranja se perdem na coroa e nas fendas |

Correções que faltariam: olhos amarelos acesos acima das fendas, sem aro escuro; focinho com o acabamento do corpo e topo mais limpo; boca menos buraco vermelho de frente; fendas mais fracas nas asas e nas costas; aros dourados mais grossos; ícone com a cabeça maior.

#### Rodada 11 (olhos amarelos acesos sem aro escuro, fendas do corpo e das asas mais fracas, fissuras no focinho, topo da cabeça mais limpo, faixas douradas grossas, ícone em perspectiva com a cabeça maior)

##### Molten Dragon (Mythic) — REPROVADO (2 PIOR: 1, 2)

| Critério | Veredito | Pet SAE | Motivo |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | cursed-monarch-rainbow, bone-emperor | Do pescoço para baixo no nível; cabeça em caixa facetada lisa, mais clara que o corpo, com 3 ou 4 riscos; olhos redondos com pupila fina e reflexo, expressão de susto; de frente encostam na aba da coroa e leem como óculos; boca boa |
| 2 Coerência com o lote | PIOR | bone-emperor; Phoenix e Titan | Corpo combina; Phoenix e Titan têm olhos amarelos chapados, angulosos e franzidos, sem pupila; o Dragon tem olho redondo de desenho; cabeça lisa e mais clara quebra o material em placas |
| 3 Escada de raridade | IGUAL | bone-emperor | Coroa, chifres com anéis de ouro, asas com borda dourada, pedras orbitando, anel dourado no chão |
| 4 Brilho só onde importa | IGUAL | voidseer-pumpkin | Corpo fosco, brilho numa cor, olhos amarelos fortes; ressalva: membrana da asa é a maior área acesa |
| 5 Paleta | IGUAL | voidseer-pumpkin | Carvão + lava + olhos amarelos, como Phoenix e Titan |
| 6 Ícone 128 px | IGUAL | bone-emperor | Dragão alado coroado legível nos dois fundos; olhos como dois discos amarelos |

Correções que faltariam: olhos no estilo do lote (amarelo chapado, anguloso e franzido, sem pupila nem reflexo, cada um no seu encaixe sob sobrancelha de pedra, longe da coroa); cabeça com o material do corpo (placas escuras com fissuras); opcional, membrana da asa mais escura.

#### Rodada 12 (olhos angulosos e franzidos, amarelos chapados sem pupila; cabeça coberta de placas com frestas de lava; asas mais escuras)

##### Molten Dragon (Mythic) — REPROVADO (3 PIOR: 1, 2, 4)

| Critério | Veredito | Pet SAE | Motivo |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | cursed-monarch-rainbow | Focinho e mandíbula em duas caixas retas com grade de tijolos; boca é buraco marrom-avermelhado chapado, sem gradiente, com poucos dentes espaçados |
| 2 Coerência com o lote | PIOR | bone-emperor; LavaTitan, VolcanicPhoenix | Corpo em placas orgânicas como o lote, mas a cabeça em blocos retangulares com linhas retas, como muro de tijolos; células das asas mais carregadas que as fissuras do Titan |
| 3 Escada de raridade | IGUAL | bone-emperor | Coroa com gema, asas com borda dourada, anéis, rochas em órbita, anel dourado e chama no fx |
| 4 Brilho só onde importa | PIOR | voidseer-pumpkin | A grade laranja das asas é a maior área acesa; olhos em cunha chapada, sem núcleo, cobertos em parte pela sobrancelha; a 3/4 o segundo olho vira lasca |
| 5 Paleta | IGUAL | voidseer-pumpkin | Grafite, lava e ouro, como Titan e Phoenix |
| 6 Ícone 128 px | IGUAL | bone-emperor | Silhueta lê nos dois fundos; coroa e linhas laranja seguram a leitura; segundo olho é um ponto (no limite) |

Correções que faltariam: cabeça em placas orgânicas com fissuras finas e focinho chanfrado; garganta com brilho quente que escurece para dentro, fileiras contínuas de dentes e língua com volume; olhos maiores com núcleo claro, sem a sobrancelha cobrindo, os dois legíveis a 3/4; grade das asas mais fina e escura.

#### Rodada 13 (cabeça coberta pelas placas do corpo, focinho e queixo chanfrados, olhos maiores com núcleo claro, garganta acesa e fileiras de dentes, pedra grafite sem lilás como o Titan 13)

##### Molten Dragon (Mythic) — REPROVADO (4 PIOR: 1, 2, 4, 6)

| Critério | Veredito | Pet SAE | Motivo |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | bone-emperor, cursed-monarch-rainbow | Corpo no nível; de frente a boca é um buraco vinho-escuro sem brilho; de lado a cabeça tem rejunte vermelho chapado e o olho é pequeno sob a aba da coroa |
| 2 Coerência com o lote | PIOR | bone-emperor; LavaTitan | Rejunte da cabeça vermelho fosco, não laranja como o corpo; a boca não brilha, a do Titan brilha em laranja |
| 3 Escada de raridade | IGUAL | bone-emperor | Coroa com cristal, asas com borda e pontas douradas, rochas em órbita, halo dourado no fx |
| 4 Brilho só onde importa | PIOR | bone-emperor | Fissuras laranja, rejunte vermelho, boca vinho e chamas do fx quase brancas: mais de uma cor de brilho |
| 5 Paleta | IGUAL | voidseer-pumpkin | Preto, grafite e laranja como Titan e Phoenix; vermelho da cabeça é o único ruído |
| 6 Ícone 128 px | PIOR | voidseer-pumpkin | A 3/4 os dois olhos se fundem numa mancha amarela colada na coroa; boca vira faixa escura |

Correções que faltariam: boca acesa em laranja como a do Titan; rejunte da cabeça no mesmo laranja do corpo; olhos separados da coroa e maiores de lado; ícone com os dois olhos visíveis e separados; chamas do fx em laranja.

#### Rodada 14 (boca acesa em laranja, frestas da cabeça no laranja do corpo, coroa afastada dos olhos, pedras de lava maiores, pontas dos chifres e garras das asas em ouro, brilho concentrado no peito, ícone mais de frente)

##### Molten Dragon (Mythic) — REPROVADO (3 PIOR: 1, 4, 6)

| Critério | Veredito | Pet SAE | Motivo |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | bone-emperor | Pedrinhas com fissuras por igual, sem forma grande dominante; fios dourados em zigue-zague soltos na borda de trás da asa; faixas douradas do flanco parecem barras soltas; tronco estreito de frente |
| 2 Coerência com o lote | IGUAL | bone-emperor | Mesma pedra cinza fosca, fissuras laranja e olhos amarelos angulosos do Titan e da Phoenix |
| 3 Escada de raridade | IGUAL | bone-emperor | Coroa, anéis nos chifres, pontas douradas nas asas, pedras de lava em órbita, anel e chamas no fx |
| 4 Brilho só onde importa | PIOR | cursed-monarch-rainbow | De frente a boca é retângulo laranja chapado mais forte que os olhos, com poucas presas; de lado o focinho tem grade com contorno laranja forte; núcleos amarelos das pedras somam outra cor; partícula rosada no fx |
| 5 Paleta | IGUAL | voidseer-pumpkin | Carvão com laranja, como os outros dois do Volcano |
| 6 Ícone 128 px | PIOR | cursed-monarch-rainbow | Pet ocupa ~60% do quadro; rosto é mancha de poucos pixels e a boca chama tanto quanto os olhos; asa de trás, cauda e pernas somem no fundo escuro |

Correções que faltariam: borda de trás da asa sem fios soltos; faixas presas ao corpo; boca com gradiente do escuro para o laranja e fileira de dentes; olhos mais claros que tudo e maiores de perfil; focinho sem grade forte; núcleo das pedras no laranja das fissuras; sem partícula rosada; ícone preenchendo ~85% com contraluz.

#### Rodada 15 (boca escura com garganta acesa e incisivos, olhos maiores, placas maiores na cabeça, ouro só na borda da frente da asa, faixas encostadas nas pernas, núcleo das pedras em laranja, ícone enchendo o quadro com contraluz)

##### Molten Dragon (Mythic) — REPROVADO (2 PIOR: 2, 4)

| Critério | Veredito | Pet SAE | Motivo |
| --- | --- | --- | --- |
| 1 Nível do degrau | IGUAL | bone-emperor | Dedos das asas com pontas douradas, membrana com rachaduras, coroa com gema, chifres com anéis, corpo todo em placas com fissuras, faixas douradas nas patas; patas simples |
| 2 Coerência com o lote | PIOR | cursed-monarch-rainbow | Pedras flutuantes laranja com placas escuras por cima formam "rostos" de abóbora; tema de Halloween que não aparece no Titan nem na Phoenix |
| 3 Escada de raridade | IGUAL | bone-emperor | Coroa, chifres e pontas das asas douradas, peças em órbita, anel dourado com efeitos |
| 4 Brilho só onde importa | PIOR | voidseer-pumpkin | Sem efeitos certo; com efeitos a fumaça da narina vira disco cinza opaco na frente do focinho e cobre um olho; ponte do focinho acesa disputa com os olhos |
| 5 Paleta | IGUAL | voidseer-pumpkin | Grafite com laranja e amarelo, como Titan e Phoenix |
| 6 Ícone 128 px | IGUAL | bone-emperor | Coroa, asa, boca com dentes e dois olhos legíveis (~22 px e ~6 px) |

Correções que faltariam: fumaça translúcida e fora do rosto; pedras flutuantes como rocha escura com fissuras finas, sem cara de abóbora.

#### Rodada 16 (pedras em órbita como rocha escura com frestas de lava, fumaça translúcida longe dos olhos, frestas da cabeça mais fracas)

##### Molten Dragon (Mythic) — REPROVADO (1 PIOR: 6)

| Critério | Veredito | Pet SAE | Motivo |
| --- | --- | --- | --- |
| 1 Nível do degrau | IGUAL | bone-emperor | Asas com pontas douradas, coroa, couraça de placas recortadas, boca com fileira de dentes nas três vistas; faixas douradas finas e asa de trás em leque atrás da cabeça a 3/4 |
| 2 Coerência com o lote | IGUAL | bone-emperor | Mesma pedra facetada com fissuras laranja e mesmos olhos amarelos sextavados com sobrancelha do Titan |
| 3 Escada de raridade | IGUAL | bone-emperor | Coroa, espinhos dourados nas asas e chifres, orbes de lava, anel dourado e chamas no fx |
| 4 Brilho só onde importa | IGUAL | bone-emperor | Corpo fosco, brilho numa cor; olhos amarelos são o ponto mais claro de frente e de lado |
| 5 Paleta | IGUAL | voidseer-pumpkin | Preto, laranja e dourado, como Titan e Phoenix |
| 6 Ícone 128 px | PIOR | voidseer-pumpkin | Em 128 px os dois olhos se encostam e viram uma faixa amarela só, colada na coroa; espinhos da coroa somem no fundo claro |

Correções que faltariam: ponte escura de ~4 px entre os olhos no ícone (olhos mais afastados ou câmera mais de frente); faixa escura entre coroa e olhos ou dourado mais saturado.

#### Rodada 17, última (olhos mais afastados com o lado de dentro mais curto, ícone quase de frente, ouro mais saturado, faixas douradas mais grossas)

##### Molten Dragon (Mythic) — REPROVADO (1 PIOR: 1)

| Critério | Veredito | Pet SAE | Motivo |
| --- | --- | --- | --- |
| 1 Nível do degrau | PIOR | bone-emperor | Asas: membrana cinza lavada, mais clara que o corpo; de frente hastes finas cruzam a asa como treliça; a 3/4 e de lado a borda de baixo termina em varetas soltas, sem membrana entre elas. O resto (placas, coroa, garras) no nível |
| 2 Coerência com o lote | IGUAL | bone-emperor; LavaTitan, VolcanicPhoenix | Mesmas placas carvão, mesma fissura laranja e mesmos olhos amarelos em cunha do Titan |
| 3 Escada de raridade | IGUAL | bone-emperor | Coroa com espinho central, anéis nos chifres, faixas douradas, lâmina dourada na cauda, anel e chamas no fx; pedras em órbita encostam no corpo a 3/4 |
| 4 Brilho só onde importa | IGUAL | voidseer-pumpkin | Corpo fosco, uma cor de brilho; de frente dois olhos amarelos grandes e separados e boca aberta com dentes e interior laranja; de lado um olho legível sob a sobrancelha |
| 5 Paleta | IGUAL | voidseer-pumpkin | Carvão, lava e ouro, como Titan e Phoenix |
| 6 Ícone 128 px | IGUAL | voidseer-pumpkin | Dois olhos separados, boca com dentes e coroa legíveis nos dois fundos; ocupa ~82×120 px |

Correções que faltariam: membrana fechada até os dedos de baixo, sem varetas soltas nem treliça de frente; membrana no valor escuro do corpo; ponta dourada marcada em cada dedo da asa.


## Ícone da rodada 9 (31/10/2026)

Na rodada 8 só o ícone (critério 6) ficou PIOR; modelo, prints e efeitos não mudaram. O `icone_128.png` foi refeito em render próprio (`ICON_ONLY=1 python3 shots.py ...`): 3/4 de frente (24° do eixo, como a vista `tres_quartos`), câmera fechada na cabeça, que ocupa mais de um terço do quadro com os dois olhos visíveis; asas cortadas pelo quadro, sem as rochas em órbita; luz de recorte clara por trás e contorno claro fino de 1 px.

## v10: rodada 7 do revisor (31/10/2026)

PIOR em 1, 4 e 6; corpo mantido. O que mudou:

- **Cabeça** 1,6× a base (era 1,38×), focinho e mandíbula ~35% mais largos na ponta, sobrancelha de pedra mais alta. Para caber em 9 studs, o pet inteiro foi reescalado (comprimento 8,99, altura 6,7 com a coroa).
- **Boca** com abertura menor no `Idle` (12°), céu da boca e mandíbula em pedra escura; o brilho vem da brasa na garganta. Dentes regulares e contínuos: 8 em cima e 7 embaixo de cada lado.
- **Olhos** ~30% maiores, laranja `FF9A1E` (núcleo `FFE070`) para se separar do dourado da coroa, pupila em fenda mais grossa, voltados para a frente; os dois aparecem a 3/4.
- **Âncoras FX** da cabeça (`FX_Crown`, `FX_Nostril`, `FX_Mouth`) acompanham a cabeça nova.
- **Ícone** mais perto da cabeça e da coroa, com as luzes de borda.

Totais do v10: 38 684 tris, maior malha `plates` 15 220; rig de 30 ossos, mesmos 4 clipes.


## v9: rodada 6 do revisor (31/10/2026)

PIOR em 1, 4 e 6. Meio-termo do lote para o olho: tamanho do v8 menos ~25%, afundado na frente da cabeça sob sobrancelha zangada, `FFB030` com pupila em fenda fina. O que mudou:

- **Olhos** saíram da lateral (pareciam fones) para a frente da cabeça: amêndoa `FFB030` com núcleo claro e fenda escura vertical, afundada numa órbita de pedra e inclinada com o canto de dentro para baixo; os dois aparecem de frente e a 3/4.
- **Cabeça com estrutura**: arcada da sobrancelha em placa de pedra que avança sobre o olho e maçãs do rosto; chifres saem do crânio.
- **Boca aberta** (22°) com as duas arcadas: 5 dentes em cima e 4 embaixo, presas maiores nos cantos; interior em lava escura `7A2414` com emissão baixa, mais fraco que os olhos.
- **Asas** 25% maiores e mais abertas no `Idle`, veias laranja de volta na membrana, pontas douradas nos dedos e borda dourada.
- **Ícone** 3/4 frontal (24° do eixo) com os dois olhos, asas abertas, e uma luz de borda clara a mais para o fundo escuro.

Totais do v9: 38 516 tris, maior malha `plates` 15 220; rig de 30 ossos, mesmos 4 clipes.


## v8: rodada 5 do revisor (31/10/2026)

PIOR em 1, 2, 4 e 6; os 3 pets do lote caíam nos olhos pequenos. O que mudou:

- **Olhos** com o dobro da altura: amêndoa inclinada com contorno escuro, halo laranja `FF6A14`, íris `FFC040` e núcleo `FFF0C0`; são a área mais clara do rosto e aparecem de frente, 3/4, lado e no ícone. Cabeça 1,38× a base.
- **Boca** com interior escuro e brasa pequena recuada na garganta; dentes grandes visíveis também de frente. Sumiu o triângulo vermelho.
- **Fissuras** em laranja-lava `FF7A1A`, um pouco mais grossas (fresta ~1,6× a do v7), como Lava Titan e Volcanic Phoenix.
- **Pedra** puxada para cinza-carvão violeta (`3A3442`, arestas `565064`).
- **Dourado só em coroa, anéis e bordas das asas**: chifres, leque do peito, espinhos das ombreiras, machado da cauda e garras das asas viraram pedra.
- **Membrana** escura e contrastada (`2E2838`/`252030`), sem tom marrom.
- **Garras das patas** maiores, em osso claro.
- **Ícone** mais perto da cabeça e sem o contorno laranja.

Totais do v8: 39 248 tris, maior malha `plates` 15 220; rig de 30 ossos, mesmos 4 clipes.


## v7: rodada 4 do revisor (31/10/2026)

PIOR em 1, 2, 4 e 6. O que mudou (corpo igual ao v6):

- **Olho padrão do lote**: amêndoa inclinada (~18°, canto de dentro para baixo), inteira emissiva `FFC040` com núcleo mais claro `FFE48A`, **sem pupila e sem anel**, achatada e embutida numa órbita rasa de pedra escura sob a sobrancelha-placa. Some o disco que saltava na lateral da cabeça.
- **Boca**: 4 dentes grandes em cima e 3 embaixo, de tamanhos diferentes, com presas maiores no canto (0,42 e 0,34); interior da boca em laranja-lava escuro aceso e brasa maior na garganta.
- **Ícone**: 3/4 de frente (30° do eixo), câmera mirando a cabeça, cabeça grande no quadro, dois olhos e boca acesa visíveis; asas recolhidas, sem rochas, contorno quente.
- **Garras de ouro** nas pontas dos dedos das asas.

Totais do v7: 38 384 tris, maior malha `plates` 15 220; rig de 30 ossos, mesmos 4 clipes.


## v6: rosto refeito (rodada 3 do revisor + pedido do usuário, 31/10/2026)

O usuário gostou do corpo e achou **boca e olhos estranhos**; o revisor deu PIOR em 1, 4 e 6. O corpo ficou como estava; o que mudou:

- **Olhos sem esclera** (decisão do lote para os 3 pets): halo laranja atrás, contorno escuro, íris acesa `FFC040` e um núcleo pequeno branco-quente. Embutidos sob a sobrancelha, maiores e virados para a frente.
- **Boca natural**: mandíbula a 13° (antes 24°), céu da boca e língua em pedra escura com dentes regulares; o brilho de lava ficou só no fundo da garganta. Sumiu a placa laranja que parecia bico.
- **Cabeça** 28% maior que a base, um pouco mais à frente.
- **Pernas**: no `Idle`, dianteira esquerda avançada e flexionada, direita um pouco para trás; placa-espinho de obsidiana em cada joelho para marcar a junta.
- **Asas**: membrana um tom mais clara e 4 nervuras finas acesas ao longo dos dedos, além da borda.
- **Menos dourado**: tiradas as bolas de ouro e as joias das ombreiras e faixas (ficam 3 espinhos de ouro em cada), leque do peito de 8 para 5 lâminas.
- **Ícone** em render próprio: 3/4 com focinho e cauda, asas recolhidas, sem as rochas em órbita, quadro fechado no corpo, contorno quente.

Totais do v6: 38 772 tris, maior malha `plates` 15 220; rig de 30 ossos, mesmos 4 clipes.


## v5: correção da 2ª rodada do revisor (31/10/2026)

Rodada 2 deu PIOR em 1, 4 e 6 (IGUAL em 2, 3, 5). Padrão revisado do lote: veias só nos veios principais, grandes áreas de pedra fosca, uma cor de brilho laranja-lava, olhos branco-amarelo quente com halo como o ponto mais forte, dourado fosco, luz de borda quente. O que mudou:

- **Brilho só onde importa:** a fresta entre placas fica laranja só no peito, garganta e barriga; nas pernas, costas e cauda ela virou pedra escura. A membrana das asas perdeu as veias laranja e ficou só com a borda acesa.
- **Dourado fosco** (rugosidade 0,55–0,62, metal 0,7) em coroa, chifres, argolas, medalhões e garras.
- **Olhos** branco-amarelo quente (`FFF4C8`, emissão 6) com halo laranja atrás, o ponto mais forte do pet; a coroa recuou para longe deles.
- **Presença:** cabeça 20% maior e um pouco à frente; mandíbula aberta a 24° com dentes e brilho de magma dentro da boca; no `Idle`, pescoço erguido, peito à frente, pata dianteira esquerda avançada e asas 14° menos abertas. Os prints são o 1º quadro do `Idle` (a pose que o jogador vê); a vista de frente tem a câmera a 16° de altura para mostrar o rosto.
- **Rochas em órbita** com núcleo de lava aceso entre 3 lascas de pedra, legíveis sem efeitos.
- **Ícone** 3/4 com as asas menos abertas e contorno quente de 2 px.

Totais do v5: 38 878 tris, maior malha `plates` 15 220, `part_head` 2 562, `part_orbit` 620; rig de 30 ossos, mesmos 4 clipes.


Feito segundo `12 Modelos e pets/Pets lendarios e miticos/Regua Steal An Egg para os 21 pets.md` e a ficha `Molten Dragon.md` (só o não visual: nome, espécie, raridade, gait, clipes e pontos de efeito). Data: 31/10/2026.

## Arquivos

| Arquivo | O que é |
| --- | --- |
| `MoltenDragon.glb` | modelo com rig e clipes (2,8 MB, sem texturas: cores por material) |
| `screenshots/frente.png`, `tres_quartos.png`, `lado.png` | sem efeitos, fundo transparente, 1024² |
| `screenshots/*_fx.png` | as mesmas vistas com os efeitos ligados |
| `icone_128.png` | ícone de inventário 128 px (vista 3/4) |
| `vfx/*.html` e `vfx/*_4x4.png` | 7 efeitos e seus flipbooks 1024² 4×4 |
| `emissores.md` | lista de emissores e orçamento |
| `fonte/` | scripts do Blender que geram tudo (ver "Como refazer") |

**Origem dos screenshots: render do Blender (não é o jogo).** O GLB tem ~37 mil triângulos em 13 malhas; para pôr no Studio do usuário seria preciso subir o asset (ação externa, não autorizada aqui) ou mandar a malha inteira como código Luau pelo MCP, o que não cabe. Luz neutra (sol + ambiente cinza), câmera ortográfica, sem bloom.

## Limites técnicos

| Malha | Tris | | Malha | Tris |
| --- | --- | --- | --- | --- |
| `plates` (placas do corpo) | **15 220** (maior) | | `part_wing_R` | 3 540 |
| `core` (magma entre as placas) | 8 880 | | `part_wing_L` | 3 396 |
| `part_head` | 2 282 | | `part_chest` | 592 |
| `part_flegL/R`, `part_hlegL/R` | 874 cada | | `part_tail_tip` | 204 |
| `part_jaw` | 186 | | `part_spikes` | 182 |
| `part_orbit` (rochas) | 500 | | | |

Total 38 478 tris; **todas as malhas ≤ 20 000**. 15 materiais, nenhuma textura (≤ 1024² atendido). Comprimento 8,95 studs, altura 6,0 (topo da coroa), largura de asas 6,4. Pivô no chão; no Blender +X é a frente e +Z é cima (o GLB segue o padrão glTF, Y para cima). Escala no jogo: Mythic ×2,0.

**Rig:** 30 ossos: 24 que deformam (`root`, corpo, quadril, pescoço 2, cabeça, mandíbula, cauda 4, asas 2×2, patas 4×2, `orbit` das rochas) + 6 âncoras `FX_Crown`, `FX_Nostril`, `FX_Mouth`, `FX_Furnace`, `FX_Back`, `FX_Ground`, sem peso de pele.

**Clipes** (24 fps, primeiro quadro = último, loop sem salto):

| Clipe | Duração | O que faz |
| --- | --- | --- |
| `Idle` | 4,0 s | respira, cauda varre, asas respiram, mandíbula abre na baforada (2,0 s) |
| `Walk` | 1,8 s | passo diagonal de 4 patas, quique leve, cauda e asas acompanham |
| `Happy` | 3,0 s | abre as asas, levanta a cabeça e ruge com dois pulinhos |
| `Breath` (especial) | 2,4 s | cabeça sobe e infla (antecipação) → fogo de 0,6 a 1,8 s → volta |

## v4: correção depois do veredito do revisor (31/10/2026)

O revisor independente reprovou o v3 (PIOR nos critérios 1, 2, 3, 4 e 6; IGUAL no 5) e a thread do lote fixou um padrão comum aos 3 pets: obsidiana violeta-escura **fosca**, fissuras laranja **finas** como veias, brilho em ~20% da superfície numa só cor, olhos grandes e acesos de frente, luz de borda quente. O que mudou:

- **Material fosco** (rugosidade 0,85–0,9, sem reflexo nas facetas) e **fissuras finas**: a fresta entre placas caiu para menos da metade.
- **Asas escuras**: membrana em violeta-escuro fosco, laranja só nas veias entre as células e numa borda acesa.
- **Uma cor de brilho**: veias, borda das asas e rochas passaram do amarelo para laranja-lava `FF8A2A`; o amarelo ficou só nos olhos.
- **Ouro como foco**: peitoral em leque de 8 lâminas em volta da fornalha, ombreiras e placas de quadril de ouro com joia, garras de ouro, ponta de cauda em machado toda de ouro.
- **Mythic**: coroa ~60% maior (lâmina central de 1,7), chifres grandes inteiros de ouro, e **5 rochas de lava orbitando** o corpo no próprio modelo (osso `orbit`, uma volta por clipe, loop sem salto).
- **Olhos** ~35% maiores, virados para a frente e com emissão 4× mais forte: aparecem na vista de frente.
- **Prints** com luz de borda quente (2 luzes por trás) e **ícone** com contorno claro-quente de 2 px, legível no fundo claro e no escuro.

## O que mudou do v2 para o v3

O v2 (Blender, da pasta do projeto `pets-v2/`, trazido para cá em `fonte/` nesta entrega) já tinha rig e 4 clipes. Para a régua nova:

- **Placas em bloco chanfrado** com topo plano, no lugar das pirâmides facetadas: lê como os blocos grossos dos pets do degrau, sem ruído de facetas.
- **Olhos** amarelos 40% maiores, com pupila em fenda e brilho branco: legíveis no ícone de 128 px.
- **Coroa de 5 lâminas de ouro** com joia, e **pontas de ouro** nos chifres grandes (escada do Mythic: coroa e chifres dourados).
- **Faixas de ouro** abraçando coxas e ombros, no lugar dos aros soltos que pareciam brincos.
- **Âncoras FX_** no rig e efeitos em flipbook (chama no dorso, baforada, brilho da coroa, pulso da fornalha, anel de brasas no chão e o fogo do Breath).

## Como refazer

Precisa de `pip install bpy scikit-image scipy` (Blender 5.2 em Python). Em `fonte/`:

```
python3 core.py      # corpo base por SDF -> core.npz
python3 build.py     # placas + peças -> out/dragon.blend
python3 rig.py       # escala, ossos, pesos, clipes -> out/molten-dragon-v4.glb
python3 shots.py out/molten-dragon-v4.glb ../vfx out/shots   # screenshots, _fx e ícone
```

Os flipbooks saem de `vfx/*.html` com `python .framework/flipbook.py ... --grade 4` (com `--loop` nos efeitos em loop), a partir de `jogos/`.

## Pendente

- Folha de comparação (`comparar.py`) e veredito do revisor independente: feitos pela thread do lote 1.
- Screenshot no Roblox Studio quando o asset for enviado.
