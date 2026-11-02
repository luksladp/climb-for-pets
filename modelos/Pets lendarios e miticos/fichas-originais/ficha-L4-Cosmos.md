# Ficha — Cosmos (área 10): BlackHoleCat · CelestialWhale · CosmicDeity

Lido junto com o plano mestre (R1–R10, portões, técnica e VFX).

**Versões atuais no jogo** (voxel realista v2/v3), cada uma com o seu defeito:

| Pet | Versão atual | Defeito |
|---|---|---|
| BlackHoleCat | gato preto com pontos de estrelas | o buraco negro não aparece de lado |
| CelestialWhale | baleia arqueada | flutua 2,25 acima do pivô |
| CosmicDeity | divindade de manto galáctico | fina (largura 2,3, corrigida para 4,46 na v3) |

Esta leva substitui as três por hard-surface no nível do MT3.

**Paleta da área:**

| Papel | Hex |
|---|---|
| violeta Config | 8C5AFF |
| espaço | 0E0A1E (médio 2A2050) |
| obsidiana-estelar | 1A1630 |
| prata-lunar | C8CCE0 |
| ouro-estelar | E8C25A |
| nebulosa | 7A3CC8 / D04AB8 / 3A6AE0 |
| Glow estrela | FFF2C8 |
| Glow violeta | B88CFF |
| Glow ciano | 6AE8FF |

**Linguagem da área: relíquia cósmica.** É o oposto do mármore da Sky:
- **placas de obsidiana-estelar** muito escuras, com **campo interno de nebulosa pintada** (R2: a borda é prata, o miolo é "janela para o espaço");
- **filigrana de ouro** em constelações (linhas finas ligando pontos Glow);
- **anéis planetários** feitos de lâminas.

**Risco:** preto que vira mancha escura de longe. Antídoto:
- borda prata clara em toda placa (R3);
- os 2 focos fortes;
- nebulosa saturada nos miolos.

**Texturas de VFX (portão C):**

| Textura | Descrição |
|---|---|
| `vfx_star_twinkle_4x4` | estrela piscando, 16 frames |
| `vfx_nebula_puff_4x4` | nuvem de nebulosa, 16 frames |
| `vfx_accretion_disk` | disco de acreção, 1024², alfa, girando |
| `vfx_constellation` | linhas e pontos, atlas 2×2 |
| `vfx_comet_trail` | Trail, 512×128 |
| `vfx_gravity_lens` | anel de distorção, 512² |

---

## 1. BlackHoleCat — Legendary · gait `ground`

### A. Conceito
Um **gato-esfinge cósmico**: felino esguio e elegante, de postura egípcia, coberto de **placas de obsidiana-estelar** com miolos de nebulosa. No **peito/ventre**, um **buraco negro real**: esfera negra absoluta com **disco de acreção** em lâminas girando na horizontal, legível **de todos os lados** (o defeito da v2/v3).

Usa um **colar-coleira de ouro** em constelação e **brincos de anel planetário** nas orelhas.

Pose: **sentado ereto como estátua egípcia**, cauda enrolada à frente das patas, cabeça alta.

### B. Silhueta e proporções
- Altura **4,8** (orelhas), largura 1,6, comprimento 3,0 (sentado).
- **3 formas-chave:**
  1. **silhueta de gato egípcio sentado** (pescoço longo, orelhas grandes);
  2. **disco de acreção** horizontal Ø 1,8 cruzando o peito, saindo para fora da silhueta dos 2 lados;
  3. cauda enrolada que termina num **cometa**.
- **Proporções:**
  - cabeça 0,8;
  - pescoço 0,6;
  - peito estreito e alto;
  - patas dianteiras retas e finas, com punho marcado.

### C. Anatomia e construção
- **Núcleo:** gato sentado (R10), com ombro e coxa marcados e afunilamento.
- **Placas:**
  - obsidiana em escudos curvos;
  - borda chanfrada **prata-lunar** fina e elevada;
  - **miolo rebaixado** pintado de nebulosa (cor diferente por região: violeta no dorso, magenta no flanco, azul nas patas).
- **Buraco negro:**
  - esfera Ø 0,7 **preta absoluta** (sem Glow, rough 1);
  - **3 anéis de lâminas finas** em volta, todos horizontais com leve inclinação: disco de acreção em ouro e branco Glow, gradiente do quente perto para o frio longe;
  - fixado ao peito por **4 garras de ouro**, como se o corpo o contivesse.
- **Cabeça:**
  - focinho fino;
  - **olhos amendoados** grandes Glow ciano, com pupila em fenda;
  - **orelhas** com placa externa e miolo de nebulosa;
  - **brincos** em anel planetário (Ø 0,3);
  - **diadema** de constelação na testa.
- **Colar:** placas de ouro com 7 pontos Glow ligados por filigrana (constelação).
- **Cauda:** segmentada em placas, enrolada; a ponta é um **cometa**, um cristal com rastro.

### D. Materiais

| Material | Hex | Rough | Metal | Onde |
|---|---|---|---|---|
| obsidiana-estelar | 1A1630 | 0,2 | 0,3 | placas |
| nebulosa | 7A3CC8 / D04AB8 / 3A6AE0 (pintada) | 0,3 | 0 | miolos |
| prata-lunar | C8CCE0 | 0,25 | 1 | bordas |
| ouro-estelar | E8C25A | 0,2 | 1 | colar, garras, brincos |
| preto absoluto | 000000 | 1 | 0 | buraco negro |

### E. Glow
- **Foco 1:** o **disco de acreção**.
- **Foco 2:** os **olhos**.
- **Secundário:**
  - pontos do colar e do diadema;
  - estrelas pequenas nos miolos de nebulosa (pintadas);
  - o cometa.

### F. Marcas de identidade
- **Uma placa do flanco "sugada"**, deformada e esticada em direção ao buraco negro, como se estivesse sendo engolida.
- Brinco **só na orelha esquerda**.

### G. Rig e FX
- **Ossos:**
  - root, pelvis, spine1–2, chest, neck1–2, head, jaw, ear_L, ear_R;
  - 4 pernas × 3;
  - tail1–8;
  - disk (girando no Idle).
- **Âncoras:** `hole` (centro do buraco negro), `eyes`, `tail_tip`.

### H. VFX
- **Ambiente:**
  - **exclusivo** `accretion`: `vfx_accretion_disk` como partícula plana no disco, girando em `hole` (low: estático);
  - **exclusivo** `infall`: partículas de estrela **sugadas em espiral** para o centro, Rate 2 (low 0,8);
  - `vfx_gravity_lens`: anel de distorção sutil;
  - `trail` com `vfx_comet_trail` na cauda.
  - Orçamento normal: 5 emissores, 4 beams, 0 luz.
- **Ação "Devour":**
  1. Antecipação 0,6 s: o disco acelera e as partículas são puxadas de 4 studs.
  2. Impacto 0,08 s: **implosão** (Size 3 → 0) + flash branco + anel `gravity_lens` expandindo.
  3. Dissipação 1,2 s: estrelas voltam a orbitar.
  - Low: implosão + anel.

### I. Animações

| Clipe | Dur | Loop | Notas |
|---|---|---|---|
| Idle | 4,0 | sim | sentado; cauda move a ponta; orelhas giram; disco gira |
| Walk | 1,6 | sim | felino elegante e altivo |
| Happy | 2,2 | não | se lambe e o disco pisca |
| Devour | 2,4 | não | fx em 0,6 |

### J. Aceitação e proibições
- **Buraco negro legível de lado e de frente**, sempre fora da silhueta.
- Lê como gato egípcio.
- Contraste prata/escuro visível a 30 studs.
- **Proibido:**
  - preto chapado sem borda;
  - pontinhos de estrela aleatórios pelo corpo todo (só nos miolos);
  - cara fofa.

---

## 2. CelestialWhale — Legendary · gait `swim` (flutua)

### A. Conceito
Uma **baleia-azul constelação**: o corpo é um **casco de placas de obsidiana-estelar** com miolos de nebulosa, mas o **ventre e as nadadeiras são translúcidos** (Spirit). Por dentro aparece uma **galáxia** e um **sistema solar em miniatura**: 3 planetas orbitando dentro da barriga.

Linhas de **constelação em ouro** desenham o "esqueleto" por fora. Leitura: baleia-azul longa, hidrodinâmica e serena, diferente da jubarte da Sky.

Pose: **nadando reta e longa**, cauda em leve curva para cima, nadadeiras para baixo.

### B. Silhueta e proporções
- Comprimento **8,4**, altura **3,6**, corpo flutua a **1,2** (corrige os 2,25 da v2).
- **3 formas-chave:**
  1. corpo **longo e fino** de baleia-azul, com cabeça em U plana;
  2. **barriga translúcida** com a galáxia;
  3. **cauda ampla** com lobos em lâmina.
- **Proporções:**
  - cabeça 25% do comprimento;
  - nadadeiras peitorais pequenas (1,2);
  - nadadeira dorsal pequena, a 3/4 do corpo;
  - fluke de 2,6.

### C. Construção
- **Núcleo:** baleia-azul real (dorso reto, cabeça larga e plana, afunilamento longo).
- **Dorso e flancos:** placas de obsidiana alongadas no sentido do corpo (6 fileiras), borda prata e miolo de nebulosa (azul e violeta).
- **Ventre:** **janela Spirit** longa (60% do comprimento), com **pregas ventrais** de prata como nervuras atravessando o vidro.
- **Dentro da janela:**
  - galáxia espiral (malha plana Glow com textura);
  - **3 planetas** (esferas de 0,25 a 0,5, com anel no maior) presos em órbitas.
- **Constelação externa:** ~20 pontos Glow estrela nas articulações do "esqueleto" (crânio, coluna, nadadeiras), ligados por filigrana de ouro em relevo.
- **Cabeça:**
  - placa de ouro no rostro, em forma de **astrolábio** (círculos concêntricos);
  - olho pequeno ciano;
  - **barbatanas**: placas prata longas.
- **Cauda:** lobos com 5 lâminas cada, as pontas Spirit.

### D. Materiais

| Material | Hex | Rough | Metal |
|---|---|---|---|
| obsidiana-estelar | 1A1630 | 0,2 | 0,3 |
| nebulosa | 3A6AE0 / 7A3CC8 | 0,3 | 0 |
| prata-lunar | C8CCE0 | 0,25 | 1 |
| ouro-estelar | E8C25A | 0,2 | 1 |
| Spirit | vidro, B88CFF, Transparency 0,5 | — | — |

### E. Glow e Spirit
- **Foco 1:** a **galáxia no ventre**.
- **Foco 2:** a **constelação externa** (pontos fortes, linhas finas).
- **Secundário:** planetas, olho, astrolábio.
- **Spirit:** janela do ventre, pontas da cauda e das nadadeiras.

### F. Marcas de identidade
- Um dos planetas internos **escapou**: ele orbita **por fora**, em volta da cabeça.
- Uma **estrela da constelação apagada**, uma falha, na nadadeira esquerda.

### G. Rig e FX
- **Ossos:**
  - root, body1–4, head, jaw;
  - pec_L, pec_R, dorsal;
  - tail1–5, fluke;
  - planets (gira), moon_out.
- **Âncoras:** `galaxy`, `moon_out`, `fluke`, `blowhole`.

### H. VFX
- **Ambiente:**
  - **exclusivo** `star_wake`: `vfx_star_twinkle` atrás da fluke, 2/s (low 0,8);
  - **exclusivo** `nebula_breath`: `vfx_nebula_puff` pelo espiráculo, a cada 7 s;
  - `orbit_ring` em volta da lua externa;
  - `core_pulse` violeta na galáxia.
  - Orçamento normal: 5 emissores, 6 beams, 1 luz.
- **Ação "Supernova Song":**
  1. Antecipação 0,6 s: a galáxia gira rápido.
  2. Impacto 0,08 s: **flash de estrela** no ventre + 3 anéis violeta expandindo + 20 estrelas radiais.
  3. Dissipação 1,6 s.
  - Low: flash + 1 anel.

### I. Animações

| Clipe | Dur | Loop | Notas |
|---|---|---|---|
| Idle | 5,5 | sim | ondulação longa; a galáxia gira; os planetas orbitam |
| Swim | 3,2 | sim | batida lenta e ampla |
| Happy | 3,0 | não | rolamento lento |
| Song | 3,0 | não | fx em 0,6 |

### J. Aceitação e proibições
- Distinta da SkyWhale: é **baleia-azul** (longa e lisa) e não jubarte; é escura e cósmica, e não mármore.
- Flutua a 1,2.
- **Proibido:**
  - arqueada em U para caber;
  - ventre opaco;
  - pontinhos aleatórios.

---

## 3. CosmicDeity — Mythic · gait `fly` (paira)

### A. Conceito
A **Divindade Cósmica**, criadora de galáxias: figura humanoide **colossal e serena**, com **armadura de placas de obsidiana-estelar** e filigrana de ouro. O **manto é o próprio espaço**: lâminas de tecido rígido com nebulosa e estrelas, que **se dissolvem em galáxia** embaixo.

Tem **4 braços**: 2 em gesto de meditação no peito e 2 erguidos segurando **um planeta com anel** e **uma estrela**. A cabeça não tem rosto: é uma **máscara de prata lisa** com uma **coroa-eclipse** (sol negro com coroa de luz) atrás. O eixo vertical é cruzado por **2 anéis planetários** de lâminas.

Pose: pairando de pernas cruzadas (lótus), braços em leque e coroa-eclipse no alto.

### B. Silhueta e proporções
- Altura **6,8** (topo da coroa), largura **5,4** (braços e anéis), paira a 0,4.
- **3 formas-chave:**
  1. **coroa-eclipse** grande (Ø 2,0) atrás da cabeça;
  2. **4 braços** com planeta e estrela;
  3. **2 anéis planetários** inclinados cruzando o corpo.
- **Proporções:**
  - torso largo (1,8 nos ombros);
  - pernas cruzadas cobertas pelo manto;
  - mãos grandes;
  - cabeça pequena (0,6) em relação à coroa (efeito de escala divina).

### C. Construção
- **Núcleo:** humanoide atlético sentado em lótus (R10).
- **Armadura:**
  - **peitoral** com **mapa de constelação** em relevo de ouro sobre obsidiana, cintura marcada;
  - **ombreiras** em **luas crescentes** de prata em 3 camadas;
  - braçais e manoplas com placa frontal e miolo de nebulosa;
  - **cinto** com fivela-planeta.
- **Manto:**
  - 8 lâminas grandes de tecido rígido, com o lado de fora em nebulosa escura estrelada e o forro em violeta;
  - as pontas de baixo se **fragmentam em estrelas e lâminas Spirit** que viram uma **galáxia em disco** sob a figura.
- **Máscara:** prata lisa, oval, com **3 pontos Glow** em triângulo no lugar dos olhos.
- **Coroa-eclipse:**
  - disco preto absoluto (Ø 1,2);
  - **coroa solar de 16 lâminas** de ouro e branco Glow em volta, de comprimentos alternados;
  - presa à nuca por haste.
- **Braços:**
  - os de cima seguram um **planeta com anel** (Ø 0,7, faixas pintadas) e uma **estrela** (cristal Glow facetado);
  - os do meio, em mudra de meditação, com as mãos juntas formando um losango no peito.
- **Anéis planetários:** 2 anéis de lâminas finas (prata e ouro), Ø 4,8 e 4,0, inclinados ±20° e girando opostos. Ficam soltos, presos por âncora.

### D. Materiais

| Material | Hex | Rough | Metal |
|---|---|---|---|
| obsidiana-estelar | 1A1630 | 0,2 | 0,3 |
| nebulosa | (3 tons) | 0,3 | 0 |
| prata-lunar | C8CCE0 | 0,2 | 1 |
| ouro-estelar | E8C25A | 0,2 | 1 |
| preto absoluto | (eclipse) | — | — |
| forro violeta | 4A2A8A | 0,6 | 0 |

### E. Glow e Spirit
- **Foco 1:** a **coroa-eclipse**.
- **Foco 2:** a **estrela** na mão erguida.
- **Secundário:**
  - os 3 pontos da máscara;
  - a constelação do peitoral;
  - as faixas do planeta;
  - a galáxia da base.
- **Spirit:** a base do manto se dissolvendo e a galáxia em disco.

### F. Marcas de identidade
- **Uma lâmina da coroa-eclipse quebrada.**
- O planeta tem uma **lua pequena** que orbita **só ele**.

### G. Rig e FX
- **Ossos:**
  - root, pelvis, spine1–3, chest, neck, head, crown;
  - 4 braços × (clav, upper, fore, hand, fingers);
  - legs (lótus) × 2;
  - cape1–4 × 2;
  - ring_A, ring_B, planet, star.
- **Âncoras:** `crown`, `star`, `planet`, `chest`, `base` (galáxia).

### H. VFX
- **Ambiente:**
  - **exclusivo** `eclipse_corona`: `halo_glow` + 16 beams curtos pulsando na coroa;
  - **exclusivo** `galaxy_base`: `vfx_accretion_disk` violeta e azul girando sob a figura + `vfx_star_twinkle` subindo;
  - `orbit_ring` nos 2 anéis;
  - `sparkle` na estrela.
  - Orçamento normal: 8 emissores, 12 beams, 1 luz.
- **Ação "Creation":**
  1. Antecipação 0,7 s: os 4 braços se juntam acima da cabeça e as estrelas são sugadas.
  2. Impacto 0,08 s: **nasce uma galáxia**, com flash branco, disco nebuloso (Size 0 → 8) e 24 estrelas radiais; os anéis expandem.
  3. Dissipação 1,8 s: nebulosa se dissolvendo.
  - Low: flash + disco.

### I. Animações

| Clipe | Dur | Loop | Notas |
|---|---|---|---|
| Idle | 5,0 | sim | paira; os anéis giram opostos; os braços de cima balançam o planeta e a estrela; o manto ondula |
| Fly | 2,6 | sim | mantém o lótus e inclina à frente |
| Happy | 3,0 | não | os 4 braços abrem e a coroa gira |
| Creation | 3,2 | não | fx em 0,7 |

### J. Aceitação e proibições
- **Imponente e larga:** largura ≥ 5 (o defeito da v2 era a figura fina).
- A coroa-eclipse e os 4 braços leem a 30 studs.
- Distinta do Seraph e do LichKing: é sentada, com 4 braços, cósmica.
- **Proibido:**
  - manto de pano mole;
  - rosto humano;
  - preto sem borda prata;
  - anéis presos rígidos ao corpo (devem ser soltos, orbitando).
