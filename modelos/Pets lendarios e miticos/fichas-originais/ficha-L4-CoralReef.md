# Ficha — CoralReef (área 5): PearlSeahorse · Kraken · Leviathan

Lido junto com `2026-10-21_plano-leva4-areas4-7.md` (R1–R10, método, portões, técnica, VFX comum).

**Paleta da área:**
| Cor | Hex |
|---|---|
| turquesa (Config) | 28C8DC |
| azul-abissal | 0E2A47 |
| tinta-profunda | 081A2E |
| coral | FF7A6B |
| coral-escuro | B84A44 |
| nácar | F2EEE6 (reflexo E6D8F0 / D8F0EE, pintado em manchas grandes) |
| ouro-areia | D6B46A |
| ardósia | 4A5A66 |
| bio Glow | 3CF0FF |
| pérola-quente Glow | FFE6B0 |

**Os 3 flutuam** (gait `swim`): o pivô fica no chão e o corpo, na altura indicada.

**Texturas de VFX da área (portão C):**
- `vfx_bubble`: bolha com reflexo e iridescência, 256²;
- `vfx_bubble_pop_4x4`: bolha estourando, 16 frames;
- `vfx_bio_mote`: ponto bioluminescente suave, 128²;
- `vfx_ink_cloud_4x4`: nuvem de tinta escura com borda azul, 16 frames;
- `vfx_water_ring_8x8`: anel de água girando com espuma, 64 frames;
- `vfx_caustic`: luz cáustica para Beam, 512² em tile.

**Proibido na área inteira** (a v1 virou máquina):
- parafusos e rebites;
- tiras de LED retas;
- bocais sextavados;
- anéis completos em volta do corpo/membro;
- ladrilhos retangulares.

A bioluminescência é sempre **pontos ou manchas orgânicas** seguindo a anatomia.

---

## 1. PearlSeahorse — Legendary · gait `swim`
### A. Conceito
Um cavalo-marinho real tratado como **joia art nouveau**: placas ósseas de **nácar** com bordas de **ouro-areia** em curvas orgânicas (como joalheria Lalique), e uma pérola enorme engastada no peito. É a peça mais delicada e elegante do jogo: **leveza**.
Pose: ereto, levemente inclinado para a frente, cauda em espiral, focinho apontando para a frente e para baixo.
Personalidade: aristocrática e serena.

### B. Silhueta e proporções
- Altura **4,8** (do chão ao topo da coroa; corpo de 1,0 a 4,8), largura ≤ 1,6, profundidade ~2,2.
- **3 formas-chave:**
  1. **S vertical**: cabeça em ângulo de 90° com o pescoço, **barriga saliente à frente** e costas arqueadas;
  2. focinho tubular longo;
  3. cauda em espiral de 1,5 volta.
- **Proporções:**
  - cabeça com 0,9 de comprimento (focinho 0,55);
  - tronco com largura 1,3 e profundidade **1,6** na barriga;
  - pescoço com Ø 0,55;
  - cauda afunilando de Ø 0,5 até 0,08.

### C. Anatomia e construção
- **Núcleo:** loft com seção em **D** (barriga arredondada à frente, costas com quilha) e raio variável: largo na barriga, fino no pescoço, afunilando na cauda.
- **Placas ósseas** (a anatomia real tem anéis segmentados; aqui são **placas por segmento**):
  - 11 segmentos no tronco e ~30 na cauda;
  - cada segmento tem **4 placas**: dorsal, 2 laterais e ventral;
  - as placas têm contorno de escudo curvo, se sobrepõem levemente e **seguem a curva** do corpo;
  - nas junções há uma **crista óssea com espinho curto** (0,08) em ouro-areia.
- **Barriga:** placas ventrais maiores, como um peitoral de nácar polido; nelas fica a pérola.
- **Focinho:** tubular, afunilando até uma **boca pequena e delicada** (uma fenda). Tem 3 anéis de crista orgânica, irregulares, nunca anel de máquina.
- **Olho:** grande para o corpo, mas sério, com íris pequena, aro de ouro e **sobrancelha espinhosa** (3 espinhos).
- **Coronet (coroa):** 5 pontas de **coral ramificado** (cada uma com 2–3 ramos), coral-escuro na base e coral-claro na ponta, com uma pérola pequena na ponta central.
- **Barbatana dorsal:** leque de 12 raios de nácar curvos com membrana Spirit; altura 0,9, nas costas, legível de lado.
- **Peitorais:** 2 pequenas atrás da cabeça, em leque.
- **Pérola do peito:** esfera de Ø 0,55 engastada em **4 garras de ouro em voluta art nouveau**.

### D. Materiais
| Material | Hex | Rough | Metal | Onde |
|---|---|---|---|---|
| nácar | F2EEE6, manchas iridescentes E6D8F0 e D8F0EE | 0,2 | 0,1 | placas |
| ouro-areia | D6B46A | 0,3 | 0,9 | bordas das placas (filete fino), cristas, garras, aro do olho |
| coral | FF7A6B / B84A44 | 0,6 | 0 | coronet |
| pele interna | C8B8B0 | 0,5 | 0 | frestas entre as placas, nunca cinza de máquina |

### E. Glow e Spirit
- **Foco 1:** a **pérola do peito** (FFE6B0, com gradiente pintado no Glow: centro quente, borda nácar).
- **Foco 2:** a pérola da coronet + os olhos (aro bio).
- **Secundário:** 8 pontos bio pequenos ao longo da crista dorsal.
- **Spirit:** membranas da dorsal e das peitorais (Transparency 0,35), cor turquesa clara.

### F. Marcas de identidade
- **Uma placa lateral** do tronco é de **coral-escuro** em vez de nácar, como coral crescendo sobre ela.
- A **voluta de ouro** da garra superior da pérola é maior, um floreio assimétrico.

### G. Rig e FX
- **Ossos:**
  - root, body1–3, neck, head, snout, coronet;
  - tail1–10 (espiral), dorsal1–3, pec_L, pec_R.
- **Âncoras:** `pearl` (body2), `crown` (coronet), `tail` (tail10).

### H. VFX
- **Ambiente:**
  - **exclusivo** `pearl_shine`: `core_pulse` com cor pérola (FFE6B0) a cada 2,0 s, mais um flash `star4` de brilho de joia a cada 4 s;
  - **exclusivo** `iridescent_bubbles`: bolhas (`vfx_bubble`) subindo do focinho, a 0,8/s (low 0,4), com leve oscilação e pop no fim (`bubble_pop`);
  - `sparkle` dourado pequeno na coronet;
  - orçamento normal: 4 emissores e 1 luz (pérola).
- **Ação "Shine":**
  - antecipação 0,5 s: a cauda se enrola e a pérola escurece;
  - impacto em 0,06 s: **flash de pérola** + `fx_halo_soft` nácar expandindo + 12 `star4`;
  - dissipação 1,2 s: bolhas e brilho caindo;
  - low: halo + 5 estrelas.

### I. Animações
| Clipe | Duração | Loop | Notas |
|---|---|---|---|
| Idle | 3,5 s | sim | flutua subindo e descendo 0,15; a dorsal vibra rápida; a cauda abre e fecha |
| Swim | 2,0 s | sim | ereto, deslocando à frente com a dorsal batendo |
| Happy | 2,5 s | não | giro vertical com a cauda se desenrolando |
| Shine | 2,0 s | não | marcador fx em 0,5 s |

### J. Aceitação e proibições
- Lê como cavalo-marinho de verdade, com barriga e S claros.
- As placas seguem a curva; nada de "mola de anéis empilhados".
- O focinho termina em boca delicada.
- A coronet é de coral ramificado (nunca penacho liso).

---

## 2. Kraken — Legendary · gait `swim`
### A. Conceito
Um polvo colossal **velho e encrustado**: carapaça abissal áspera coberta de **cracas, coral e conchas incrustadas**, como algo que dorme no fundo há séculos. É o oposto rústico da joia do cavalo-marinho. Pose: **flutuando, manto inclinado para trás, 2 tentáculos de ataque erguidos à frente em curva ameaçadora e 6 curvados para baixo**, como se agarrasse algo.
Personalidade: um predador antigo.

### B. Silhueta e proporções
- Altura **4,8** (corpo flutua a 1,4; as pontas dos tentáculos chegam a 0,5), largura **≤ 5,6** com os tentáculos.
- **3 formas-chave:**
  1. **manto em gota alongada para trás e para cima** (nunca cilindro);
  2. **olhos visíveis de frente**;
  3. coroa de 8 tentáculos em curvas contínuas.
- **Proporções:**
  - manto com 2,2 de comprimento × 1,7 de largura;
  - cabeça/olhos na base do manto;
  - tentáculos com **Ø 0,45 na base → 0,06 na ponta** e comprimento 2,8–3,4.

### C. Anatomia e construção
- **Núcleo:** manto orgânico (gota com dobra lateral e um vinco central dorsal suave) + cabeça com 2 bulbos oculares + 8 tentáculos com **seção oval achatada em baixo** (onde ficam as ventosas).
- **Carapaça:** **5–7 placas irregulares** derivadas da superfície do manto, de borda ondulada, abissais, com borda coral-escura. Entre elas há **frestas onde aparece a pele** (azul-tinta), nunca uma luz em tira.
- **Incrustações (assinatura):**
  - 3 grupos de **cracas** (cones de 0,08–0,15 com abertura no topo);
  - 2 tufos de **coral ramificado** coral;
  - 1 **concha espiral** grudada no flanco direito.
- **Olhos:** grandes (Ø 0,45), na frente e na lateral da cabeça, com **pálpebra-placa pesada** caindo sobre metade do olho, **pupila horizontal** em fenda e íris turquesa. Devem aparecer na vista 3/4.
- **Tentáculos:**
  - o dorso tem **pele com placas-escama pequenas** que acompanham a curva (decrescendo para a ponta), **sem segmentos retangulares**;
  - em baixo, **2 fileiras de ventosas** (Ø 0,18 → 0,04), cada uma com aro e centro rebaixado (R2);
  - curvas suaves contínuas (spline), sem quebras.
- **Bico:** de ardósia, visível por baixo entre os tentáculos.

### D. Materiais
| Material | Hex | Rough | Metal | Onde |
|---|---|---|---|---|
| carapaça | 0E2A47, borda B84A44 | 0,55 | 0 | placas do manto |
| pele | 081A2E, ventre 3A5068 | 0,45 | 0 | frestas, tentáculos |
| ventosas | D8B8B0 (rosado claro) | 0,5 | 0 | ventosas |
| cracas | C8C0B0 / 8A8478 | 0,8 | 0 | incrustações |
| coral | FF7A6B | 0,6 | 0 | tufos de coral |

### E. Glow
- **Foco 1:** os **2 olhos** (aro bio 3CF0FF fino, a íris pintada).
- **Foco 2:** **manchas fotóforas** no manto, 9 pontos/manchas irregulares, **nunca em tira**.
- **Secundário:** o centro das 6 primeiras ventosas dos 2 tentáculos de ataque.

### F. Marcas de identidade
- **Cicatriz** de 3 riscos (garras) na placa frontal do manto.
- Um tentáculo traseiro **mais curto, com a ponta cortada**.

### G. Rig e FX
- **Ossos:** root, mantle1, mantle2, head, beak, eyelid_L, eyelid_R e 8 tentáculos × 8 ossos.
- **Âncoras:**
  - `core` (mantle1);
  - `eye_L` e `eye_R`;
  - `ink` (sob o manto, no sifão);
  - `tip_atk_L` e `tip_atk_R`.

### H. VFX
- **Ambiente:**
  - **exclusivo** `bio_motes`: 6 motas bio (`vfx_bio_mote`) flutuando lentas em volta do manto, a Rate 1,5 (low 0,6), com vida 4 s e drift aleatório;
  - `sparkle` bio nos olhos, raro (piscada a cada 5 s);
  - bolhas pequenas do sifão a cada 3 s;
  - orçamento normal: 4 emissores.
- **Ação "Grab":**
  - antecipação 0,5 s: os tentáculos de ataque recuam e os fotóforos acendem em sequência;
  - impacto em 0,08 s: os tentáculos fecham, **nuvem de tinta** (`vfx_ink_cloud_4x4`) do sifão e anel de água (`water_ring`);
  - dissipação 1,5 s: a tinta se dissolve e as motas se espalham;
  - low: tinta + anel.

### I. Animações
| Clipe | Duração | Loop | Notas |
|---|---|---|---|
| Idle | 4,0 s | sim | tentáculos ondulam em onda defasada; o manto respira; os olhos piscam com a pálpebra |
| Swim | 1,6 s | sim | **pulso de jato**: o manto contrai, os tentáculos juntam e abrem |
| Happy | 2,5 s | não | gira, com os tentáculos se espalhando em estrela |
| Grab | 2,2 s | não | marcador fx em 0,5 s |

### J. Aceitação e proibições
- O manto é orgânico (gota), nunca "cápsula ou tanque".
- Os tentáculos são carne contínua afunilando, nunca "corrente de esteira".
- Os olhos são visíveis de frente.
- **Proibido:**
  - parafusos;
  - tiras ciano retas;
  - segmentos retangulares.

---

## 3. Leviathan — Mythic · gait `swim`
### A. Conceito
A **serpente real das profundezas**. Escamas de **pérola negra** (preto-azulado iridescente) com borda turquesa, coroa de coral-branco e pérolas e uma juba de barbatanas translúcidas. É majestoso e enorme: **regalia abissal**.
Pose: **corpo em espiral ascendente** (1 volta e meia), a cabeça erguida no topo olhando para a frente e para baixo, a boca entreaberta.
Personalidade: um rei antigo.

### B. Silhueta e proporções
- Altura **6,4** (topo da coroa), comprimento total do corpo **~16**, em espiral com **pegada ≤ 7 × 7**. O corpo flutua com a volta mais baixa a 0,8.
- **3 formas-chave:**
  1. espiral ascendente;
  2. **cabeça grande coroada** (comprimento 1,6, **~50% maior que a v1**);
  3. crista dorsal contínua de barbatanas translúcidas.
- **Proporções:**
  - corpo com Ø 1,1 no terço anterior, afunilando para 0,25 na cauda;
  - pescoço sem estreitamento brusco;
  - **seção do corpo oval** (mais alta que larga).

### C. Anatomia e construção
- **Núcleo:** serpente com seção oval e barriga achatada.
- **Escamas dorsais:** fileira de escamas-placa **em gota grande** (0,35 × 0,28) de pérola negra, com **borda turquesa elevada** (R2), sobrepostas 30% e acompanhando a curva.
- **Flancos:** escamas menores (0,14) em fileiras diagonais.
- **Barriga:** placas segmentadas de **nácar**, mais largas no meio e estreitando para a cabeça e a cauda.
- **Crista dorsal:** raios de nácar curvos (0,5 → 0,15) com membrana Spirit **ondulada**, desde o crânio até 2/3 do corpo.
- **Cabeça:**
  - crânio de dragão marinho longo e anguloso;
  - sobrancelha de placa;
  - **mandíbula com 2 fileiras de dentes de nácar**, boca entreaberta mostrando a língua;
  - **barbatanas laterais em leque** no lugar das orelhas (raios curvos e membrana);
  - barbilhões (2 bigodes longos, de 1,2, rígidos, curvos);
  - **2 chifres em espiral de concha** (tipo náutilo alongado, 0,9) para trás.
- **Coroa (marca Mythic):** arco de **coral-branco ramificado** sobre a nuca, com **5 pérolas** (central maior) e filetes de ouro-areia.
- **Nadadeiras:** 2 pares (peito e meio do corpo), com **forma de nadadeira** (raios curvos, borda ondulada, afunilada), nunca leque de mão.
- **Cauda:** leque grande e assimétrico (lobo superior maior), com raios e membrana Spirit.

### D. Materiais
| Material | Hex | Rough | Metal | Onde |
|---|---|---|---|---|
| pérola negra | 141A2A, iridescência 2A3A5A / 3A2A4A em manchas | 0,15 | 0,2 | escamas dorsais |
| turquesa | 28C8DC | 0,3 | 0,1 | borda das escamas |
| nácar | F2EEE6 | 0,2 | 0,1 | barriga, crista, dentes, chifres |
| coral-branco | EDE6DA | 0,6 | 0 | coroa |
| ouro-areia | D6B46A | 0,3 | 0,9 | filetes da coroa |

### E. Glow e Spirit
- **Foco 1:** **linha lateral de fotóforos**: 26 pontos por lado, **seguindo a linha lateral** do corpo (pontos de Ø 0,06–0,1, mais densos perto da cabeça).
- **Foco 2:** as **pérolas da coroa** (FFE6B0) + os olhos.
- **Spirit:** crista dorsal, barbatanas laterais da cabeça, nadadeiras e leque da cauda (Transparency 0,4), turquesa clara.

### F. Marcas de identidade
- **Uma pérola da coroa falta**: o engaste está vazio, à esquerda.
- O chifre direito tem uma **craca** grudada.

### G. Rig e FX
- **Ossos:**
  - root, head, jaw, whisker_L, whisker_R, fin_head_L, fin_head_R;
  - neck1–4, spine1–14, tail1–6, tail_fan;
  - 4 nadadeiras × 2 ossos.
- **Âncoras:**
  - `crown` (head);
  - `mouth` (jaw);
  - `core` (spine5);
  - `tail` (tail_fan);
  - `coil_center` (root, no centro da espiral, para o anel de água).

### H. VFX
- **Ambiente:**
  - **exclusivo** `water_ring`: anel de água (`vfx_water_ring_8x8`, mais Beam `orbit_ring` turquesa com textura `caustic`) girando devagar em volta da espiral, em `coil_center`, raio 3,0, inclinado 10°;
  - **exclusivo** `bubble_spiral`: bolhas subindo em espiral pelo corpo, 4 pontos `orbit` a Rate 1,0 (low 0,5);
  - `sparkle` pérola na coroa;
  - `core_pulse` turquesa suave;
  - orçamento normal: 7 emissores e 8 beams (o anel).
- **Ação "Roar":**
  - antecipação 0,6 s: a cabeça recua e os fotóforos acendem da cauda para a cabeça em onda;
  - impacto em 0,08 s: a boca abre, o anel de água **expande** (Size 3→7) e sai uma onda de bolhas radial;
  - dissipação 1,5 s: espuma e motas;
  - low: anel + 8 bolhas.

### I. Animações
| Clipe | Duração | Loop | Notas |
|---|---|---|---|
| Idle | 5,0 s | sim | a espiral ondula (onda que sobe pelo corpo); barbilhões e barbatanas ondulam |
| Swim | 2,4 s | sim | ondulação lateral serpentina, deslocando à frente |
| Happy | 3,0 s | não | a espiral sobe, a cabeça gira 360° e volta |
| Roar | 2,6 s | não | marcador fx em 0,6 s |

### J. Aceitação e proibições
- Escamas em gota seguindo a curva, nunca "ladrilhos".
- Cabeça grande e coroada, legível a 30 studs.
- Nadadeiras com forma de nadadeira.
- Comprimento ~16 e pegada ≤ 7 × 7.
- **Proibido:**
  - leques de mão;
  - painéis de vidro retos;
  - tiras de LED.
