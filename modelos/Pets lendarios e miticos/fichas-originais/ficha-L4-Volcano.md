# Ficha — Volcano (área 4): VolcanicPhoenix · LavaTitan · MoltenDragon

Lido junto com `2026-10-21_plano-leva4-areas4-7.md`, que define as regras R1–R10, o método, os portões, a técnica e o VFX comum.

**Paleta da área:**
| Cor | Hex |
|---|---|
| laranja-lava (Config) | FF6E28 |
| basalto | 2B2526 |
| obsidiana | 15121A |
| cinza-cinza | 6B625E |
| ouro velho | C9962E |
| magma Glow | FF7A1E |
| núcleo quente Glow | FFC040 |

**Texturas de VFX da área (portão C, compartilhadas):**
- `vfx_ember_4x4`: brasa que gira e apaga, 16 frames;
- `vfx_smoke_puff_4x4`: fumaça cartoon cinza-escura com borda clara, 16 frames;
- `vfx_magma_drip`: gota de magma 256²;
- `vfx_heat_wisp_4x4`: chama cartoon laranja, 16 frames;
- `vfx_feather_ember`: pena incandescente 256²;
- `vfx_rock_chip`: lasca de rocha 256², 4 variações num atlas 2×2;
- `vfx_fire_cone_8x8`: sopro de fogo, 64 frames.

---

## 1. VolcanicPhoenix — Legendary · gait `fly`
### A. Conceito
Uma ave de rapina **montada como vitral de obsidiana**: cada pena é uma lâmina fina de vidro vulcânico preto-violeta, **com o miolo de brasa**. Parece forjada, não emplumada. É elegante e aérea, o oposto do LavaTitan. Pose de repouso: **pairando, asas abertas em V alto a ~55°, cabeça erguida em perfil de águia e cauda em leque para baixo**.
Personalidade: orgulhosa e vigilante.

### B. Silhueta e proporções
- Altura **4,8** (do chão ao topo da crista; corpo flutuando a partir de 1,2), **envergadura 6,2**, profundidade ≤ 3,4.
- **3 formas-chave:**
  1. V das asas, com as pontas mais altas que a cabeça;
  2. tórax em quilha (gota invertida, peito projetado à frente);
  3. cauda em leque de 5 penas longas.
- Proporção: o tórax ocupa 35% da altura do corpo, o pescoço é curto em S, a cabeça tem 0,9 de comprimento (do bico à nuca) e o bico tem 0,35.
- Vista lateral: o peito projeta 0,5 à frente da linha do pescoço, as costas são planas e a cauda desce a 30°.

### C. Anatomia e construção (método R10)
- **Núcleo:** loft de ave real com tórax oval profundo (largura 1,1, profundidade 1,3), abdômen afinando para a cloaca, pescoço com seção em gota e cabeça com crânio alto e bico.
- **Peito:** 5 fileiras de **penas-escama de obsidiana** em gota (no peito alto 0,32 × 0,22, diminuindo até 0,18 × 0,12 no ventre), sobrepostas 30%. Cada uma tem borda chanfrada e **miolo rebaixado com brasa** (R2: o miolo é a parte Glow, só nas 3 fileiras centrais).
- **Asas** (3 segmentos: braço, antebraço, mão):
  - coberteiras em 3 fileiras de penas-lâmina curtas e largas;
  - 6 secundárias (comprimento 1,2–1,4);
  - **7 primárias** (1,6 → 2,2, a mais longa na 3ª);
  - cada pena é uma lâmina de 2 faces com **nervura central em V** (R2), afunilando até ponta fina; a borda de ataque tem filete de ouro velho na raiz.
  - A raiz da asa tem um **ombro emplumado grosso** (Ø 0,45) que encaixa no tórax sem vão.
- **Cabeça:**
  - bico curvo de **ouro velho** em 2 placas (superior com gancho, inferior);
  - sobrancelha de placa pesada de obsidiana sobre o olho;
  - olho pequeno e amendoado, Glow amarelo;
  - **crista de 5 penas-lâmina** para trás (0,7 → 0,4), a central maior.
- **Cauda:** 5 penas longas (2,0) em leque, com nervura, as pontas em gota incandescente (Glow) e 4 coberteiras curtas na base.
- **Patas:** recolhidas sob o corpo, tarso coberto de escamas de basalto e **4 garras de ouro velho** curvas.

### D. Materiais
| Material | Hex | Rough | Metal | Onde |
|---|---|---|---|---|
| obsidiana-vidro | 15121A, borda 3A2E44 (reflexo violeta) | 0,12–0,2 | 0,0 | penas, sobrancelha |
| basalto | 2B2526 | 0,7 | 0 | tarso, base das penas |
| ouro velho | C9962E | 0,35 | 0,9 | bico, garras, filetes da raiz |
| brasa (Color, não Glow) | 7A2A10 → FF6E28 | 0,6 | 0 | transição entre obsidiana e Glow nas penas |

### E. Glow e Spirit
- **Foco 1:** o **coração-brasa**, um losango Glow de 0,4 no centro do peito, entre as penas centrais (FFC040 no centro, FF7A1E na borda).
- **Foco 2:** os olhos.
- **Secundário fino:** miolo das penas das 3 fileiras centrais do peito, ponta das 7 primárias (os 25% finais de cada uma, cortados em segmento) e gotas da cauda.
- Spirit: nenhum.

### F. Marcas de identidade (R5)
- A asa **esquerda** tem 1 primária **quebrada pela metade**, com ponta lascada.
- O bico tem **um arranhão de ouro mais claro**.

### G. Rig e FX
- **Ossos:**
  - root, body, chest, neck1, neck2, head, jaw, crest;
  - por asa: shoulder, arm, forearm, hand, prim_a e prim_b (as primárias em 2 grupos), sec;
  - tail1, tail2, tail_fan_L, tail_fan_R;
  - por perna: thigh, tarsus, toes.
- **Âncoras:**
  - `core` (chest, no losango);
  - `tail` (tail2, na ponta do leque);
  - `wing_L` e `wing_R` (prim_b, na ponta).

### H. VFX
- **Ambiente** (normal / low):
  - `aura` recolorida em brasa (FF7A1E→FFC040) só em 2 pontos sob as asas, com Rate baixo (pássaro quente, sem fogueira);
  - **exclusivo** `ember_fall`: 1 emissor na cauda solta `vfx_feather_ember` girando e caindo devagar, a 0,6/s (low 0,3), vida 2,5 s, com a cor apagando para cinza;
  - `trail` com textura de faísca só quando ele se move (gait fly), da ponta de cada asa;
  - `core_pulse` laranja no `core`, 1,4 s;
  - orçamento normal: 5 emissores e 2 trails.
- **Ação "Flare"** (clipe Flare):
  - antecipação 0,4 s: penas fecham e o núcleo carrega com o brilho subindo;
  - impacto em 0,08 s: abre as asas, **anel de brasas** (`fx_ring_soft` laranja, Size 0→6) e rajada de 24 `vfx_ember` radiais;
  - dissipação 1,2 s: penas incandescentes caem e fumaça leve sobe;
  - low: anel + 10 brasas.

### I. Animações (portão C)
| Clipe | Duração | Loop | Notas |
|---|---|---|---|
| Idle | 3,0 s | sim | paira; batida lenta a cada 1,5 s; a cabeça vira de lado; a cauda ondula |
| Fly | 1,2 s | sim | batida completa; corpo inclinado 15° para a frente |
| Happy | 2,2 s | não | giro de barril de 360° + grito (bico abre) |
| Flare | 2,0 s | não | abertura dramática das asas; marcador fx em 0,4 s |

### J. Aceitação e proibições
- As penas leem como **lâminas de vidro**, não como cartas de baralho retangulares. A nervura em V é visível no close.
- O tórax não é barril: tem quilha.
- A raiz da asa não é palito.
- **Proibido:**
  - penas em losango chapado;
  - cor laranja chapada no corpo todo;
  - Glow em mais de 25% da superfície.

---

## 2. LavaTitan — Legendary · gait `ground`
### A. Conceito
Um titã-gorila feito de **basalto colunar**, as colunas hexagonais que se formam quando a lava esfria (Calçada dos Gigantes). O corpo é **crosta de rocha fria rachada sobre um interior de magma vivo**. As colunas hexagonais são a assinatura do pet e não aparecem em nenhum outro.
Pose: **curvado, nós dos dedos apoiados no chão à frente** (postura de gorila), a cabeça baixa entre os ombros.
Personalidade: um brutamonte calmo.

### B. Silhueta e proporções
- Altura **5,6** (topo dos cristais dos ombros; a cabeça fica em ~4,6), largura **≤ 4,4**, profundidade ~2,8 com os braços à frente.
- **3 formas-chave:**
  1. trapézio enorme dos ombros e das costas;
  2. **braços longos e grossos com antebraços muito maiores que os braços**, punhos no chão;
  3. pernas curtas e grossas.
- Proporções: ombro com 2× a largura do quadril; antebraço com Ø 1,0 e braço com Ø 0,7; perna com Ø 0,8 e altura da coxa ao pé 1,6.

### C. Anatomia e construção
- **Núcleo:** massa de gorila (dorso alto e largo, cintura menor, glúteo baixo) em **magma escuro** (é ele que aparece nas fendas).
- **Crosta (R10 + assinatura):** a superfície do núcleo é coberta por **placas de crosta poligonais irregulares** (5–7 lados, 0,25–0,6), derivadas da superfície, com fendas de 0,04–0,08 entre elas. **Não são tijolos**: cada placa tem forma e tamanho próprios, e são maiores nas costas e nos ombros.
- **Colunas de basalto hexagonais:**
  - **nos ombros e nas costas**: aglomerados de 7–12 colunas hexagonais de alturas diferentes (0,3–0,9), com o topo plano levemente inclinado, saindo da crosta como formação geológica;
  - **nos antebraços**: colunas mais curtas apontando para trás, como um "punho de rocha";
  - nos ombros há também 2–3 **cristais de obsidiana** pontudos entre as colunas.
- **Peito:** placa dupla de crosta grossa com uma **fenda central em forma de estrela de 5 pontas**, rachada de dentro, e dentro dela a fornalha.
- **Cabeça:** pequena e afundada, com mandíbula pesada saliente (placa separada), **testa de rocha em aba**, olhos em fenda e 2 chifres de obsidiana curtos curvados para a frente, visíveis de frente.
- **Costas:** **cone de cratera** (base Ø 0,9, altura 0,6, borda irregular) entre as escápulas, com magma dentro.
- **Mãos:** 4 dedos grossos de 2 segmentos, unhas de obsidiana e nós dos dedos de basalto colunar curto (a pose em punhos apoiados mostra isso).
- **Pés:** largos, com 3 dedos, sola plana e crosta grossa no calcanhar.

### D. Materiais
| Material | Hex | Rough | Metal | Onde |
|---|---|---|---|---|
| crosta de basalto | 2B2526, topo das placas 4A403D | 0,8 | 0 | crosta |
| basalto colunar | 3A3436, faces laterais 252022 | 0,65 | 0 | colunas (faces de topo mais claras, R3) |
| obsidiana | 15121A | 0,15 | 0 | cristais, chifres, unhas |
| magma resfriado (Color) | 5A1A0C | 0,5 | 0 | fundo das fendas, a 1 mm do Glow |
| cinza-cinza | 6B625E | 0,9 | 0 | poeira no topo das colunas e nos nós dos dedos |

### E. Glow
- **Foco 1:** a **fornalha do peito** (a estrela rachada, FFC040 no centro).
- **Foco 2:** a **boca da cratera** das costas.
- **Secundário:**
  - fendas entre as placas, só nos 35% mais fundos e **irregulares e finas** (nada de traço tracejado reto);
  - olhos em fenda;
  - veios nas palmas.

### F. Marcas de identidade
- O ombro **direito** tem uma coluna **partida** (topo quebrado com lascas).
- O antebraço esquerdo tem **uma placa de crosta caída**, que mostra mais magma.

### G. Rig e FX
- **Ossos:**
  - root, pelvis, spine, chest, neck, head, jaw, crater;
  - por lado: clavicle, upperarm, forearm, hand, fingers (agrupados), thumb, thigh, shin, foot.
- **Âncoras:** `core` (chest), `crater` (crater), `fist_L` e `fist_R` (hand).

### H. VFX
- **Ambiente:**
  - **exclusivo** `crater_smoke`: emissor no `crater` com `vfx_smoke_puff_4x4` a 1,2/s (low 0,5), sobe 2 studs e cresce;
  - **exclusivo** `magma_drip`: 1 emissor por punho, gota caindo a 0,4/s com Acceleration −30, apagando ao chegar no chão;
  - `core_pulse` laranja lento, 2,0 s (respiração);
  - orçamento normal: 4 emissores e 1 luz (cratera).
- **Ação "Slam":**
  - antecipação 0,5 s: ergue os 2 punhos e o magma das fendas brilha +50%;
  - impacto em 0,06 s: punhos no chão, **anel de choque no chão** (`fx_ring_soft` laranja, Size 1→8, 0,4 s), 16 `vfx_rock_chip` em arco e flash da luz;
  - dissipação 1,0 s: poeira (`smoke_puff` cinza) rolando no chão;
  - low: anel + 6 lascas.

### I. Animações
| Clipe | Duração | Loop | Notas |
|---|---|---|---|
| Idle | 3,5 s | sim | respiração pesada (ombros sobem), a cabeça olha em volta |
| Walk | 2,0 s | sim | **knuckle-walk** de gorila (punhos e pés alternando), peso visível |
| Happy | 2,5 s | não | bate no peito 3× (a fornalha pisca) |
| Slam | 2,2 s | não | marcador fx em 0,5 s |

### J. Aceitação e proibições
- **Ninguém deve ler "tijolos" nem "pneus"**: placas poligonais irregulares e colunas hexagonais são obrigatórias.
- Os antebraços são claramente maiores que os braços.
- A postura é de gorila (punhos no chão), não de robô ereto.
- **Proibido:**
  - placas retangulares em fileiras;
  - segmentos em anel nos membros;
  - Glow em traços retos tracejados.

---

## 3. MoltenDragon — Mythic · gait `ground`
### A. Conceito
Um dragão imperial de **obsidiana polida, com filigrana de ouro velho incrustada nas bordas das escamas** e magma correndo por baixo. Ele é a peça mais luxuosa da área, contra a crosta rústica do Titã e o vidro leve da Fênix. Pose: **de pé nas 4 patas, peito estufado, pescoço em S erguido e cabeça olhando para a frente e para baixo** (régio). Asas fechadas rente ao corpo.
Personalidade: um monarca.

### B. Silhueta e proporções
- Altura **6,4** (topo dos chifres), comprimento **≤ 9,0** (cauda curvada lateralmente), largura do tórax **2,8**.
- **3 formas-chave:**
  1. pescoço em S com a cabeça coroada;
  2. tórax profundo com as asas dobradas formando um "manto";
  3. cauda longa terminando em lâmina dupla.
- Proporções:
  - pescoço = 28% do comprimento e cauda = 40%;
  - patas dianteiras mais robustas que as traseiras;
  - pegada das patas com Ø 0,7.

### C. Anatomia e construção
- **Núcleo:** dragão realista: peito profundo (profundidade 2,2), cintura, ancas musculosas, pescoço que afina da base (Ø 1,1) até a nuca (Ø 0,6) e cauda afunilando até Ø 0,1.
- **Escamas dorsais:** fileira central de **13 espinhos-lâmina de obsidiana** (do maior, 0,6, nas escápulas, até 0,15 na cauda), ladeada por 2 fileiras de escamas-placa grandes em gota (0,4 × 0,3) **com filete de ouro elevado na borda** (R2: obsidiana no campo, ouro na moldura).
- **Flancos:** escamas menores (0,15–0,2) em fileiras sobrepostas 30%, sem filete de ouro (hierarquia R1).
- **Barriga:** 14 placas segmentadas de **basalto escuro**, mais largas no peito e estreitando no pescoço e na cauda, com fresta de magma entre elas.
- **Peito:** placa-escudo de obsidiana com **filigrana de ouro em espiral** em relevo, emoldurando a fornalha da garganta.
- **Cabeça:**
  - focinho longo e anguloso;
  - sobrancelha de placa pesada;
  - mandíbula com 2 fileiras de dentes de obsidiana visíveis;
  - narinas em fenda;
  - **4 chifres**: 2 grandes, de 1,2, varrendo para trás em curva, com anéis de ouro; 2 pequenos laterais;
  - **coroa de 3 lâminas de ouro velho** fundida à nuca.
- **Asas fechadas:** dobradas, com o cotovelo alto acima das escápulas e os dedos para trás e para baixo. A membrana tem placas finas de **obsidiana rachada como vitral** (4 dedos + polegar com garra de ouro), cobrindo os flancos como manto.
- **Patas:** coxa e ombro musculosos com escamas grandes, canela afunilando e **4 garras de obsidiana com base de ouro**.
- **Cauda:** termina em **lâmina dupla de obsidiana** (tipo machado), com filete de ouro.

### D. Materiais
| Material | Hex | Rough | Metal | Onde |
|---|---|---|---|---|
| obsidiana polida | 15121A, highlight 4A3A5A | 0,08–0,15 | 0 | escamas, espinhos, chifres |
| ouro velho | C9962E, bordas gastas E0B85A | 0,3 | 0,95 | filigrana, coroa, anéis, garras |
| basalto | 2B2526 | 0,7 | 0 | barriga |
| magma resfriado | 5A1A0C | 0,5 | 0 | frestas |

### E. Glow
- **Foco 1:** **fornalha da garganta e do peito**, visível entre as placas da barriga do peito e na boca entreaberta.
- **Foco 2:** **joia de magma na coroa**, um losango engastado entre as 3 lâminas.
- **Secundário:**
  - veios finos na membrana das asas, seguindo os dedos;
  - frestas da barriga, só no tórax;
  - olhos em fenda.

### F. Marcas de identidade
- O chifre grande **esquerdo** tem **2 anéis de ouro** e o direito só 1, um troféu.
- Uma escama dorsal do pescoço é **substituída por placa de ouro**, uma cicatriz remendada.

### G. Rig e FX
- **Ossos:**
  - root, pelvis, spine1–3, chest;
  - neck1–4, head, jaw;
  - 4 pernas × (upper, lower, foot, toes);
  - tail1–7;
  - por asa: shoulder, arm, forearm, hand, finger1–4.
- **Âncoras:**
  - `mouth` (jaw);
  - `core` (chest);
  - `crown` (head);
  - `tail` (tail7);
  - `nostril_L` e `nostril_R` (head).

### H. VFX
- **Ambiente:**
  - `aura` com `vfx_heat_wisp_4x4` subindo de 4 pontos no dorso, Rate baixo;
  - **exclusivo** `nostril_smoke`: a cada 4 s, 2 baforadas curtas de fumaça (`smoke_puff`) pelas narinas, sincronizadas com o Idle;
  - `sparkle` dourado na coroa (3 estrelas);
  - `core_pulse` laranja na fornalha;
  - orçamento normal: 7 emissores e 1 luz (garganta).
- **Ação "Breath":**
  - antecipação 0,6 s: ergue a cabeça, a garganta brilha e brasas são sugadas para a boca;
  - impacto em 0,1 s: **cone de fogo** (`vfx_fire_cone_8x8`, 3 emissores escalonados), 2,5 studs à frente;
  - dissipação 1,2 s: fumaça e brasas caindo;
  - low: 1 emissor do cone + brasas.

### I. Animações
| Clipe | Duração | Loop | Notas |
|---|---|---|---|
| Idle | 4,0 s | sim | respiração; pescoço oscila; baforada em 2,0 s; a cauda varre |
| Walk | 1,8 s | sim | quadrúpede, peso no peito, cabeça estável |
| Happy | 3,0 s | não | abre as asas por completo e ruge para cima |
| Breath | 2,4 s | não | marcador fx em 0,6 s |

### J. Aceitação e proibições
- As pernas são de dragão (músculo + afunilamento), nunca cascas cilíndricas de mecha.
- As asas fechadas formam manto, nunca "painel quadrado em pé".
- Pescoço sem cara de girafa: grosso na base e com S.
- A filigrana de ouro está legível no close.
- **Proibido:**
  - placas de pescoço tipo vértebra de robô;
  - membrana opaca chapada sem veios;
  - mancha clara de bake no dorso (defeito da v1).
