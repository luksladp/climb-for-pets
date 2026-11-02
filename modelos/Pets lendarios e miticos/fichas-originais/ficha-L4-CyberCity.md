# Ficha — CyberCity (área 9): QuantumCat · (MechaTitan v3 pronto) · AIOverlord

Lido junto com o plano mestre: R1–R10, portões, técnica e VFX.

**Área com tema robótico:** aqui o **método do MechaTitan vale literalmente**. Caixas articuladas, chanfro de máquina, parafusos, grelhas e visores **são permitidos**; o R10 continua valendo para a anatomia felina do QuantumCat. Os 3 devem parecer **da mesma fabricante** que o MechaTitan v3 (mesma linguagem de painéis, faixa de aviso, números de série), cada um numa linha de produto diferente.

**MechaTitan:** já pronto (v3, aprovado). **Não entra nesta leva.** É a régua dos outros dois.

**Paleta da área** (alinhada ao MT3):

| Papel | Hex |
|---|---|
| ciano Config | 28E6FF |
| aço claro | B8C0CC |
| grafite | 2E3440 |
| navy | 1C2640 |
| faixa de aviso | F2C230 + 1A1A1A |
| magenta | FF3CA8 |
| Glow ciano | 3CF0FF |
| Glow magenta | FF5AD0 |

**Texturas de VFX da área (portão C):**

| Textura | Descrição |
|---|---|
| `vfx_hex_grid` | grade hexagonal holográfica, 512², tile |
| `vfx_glitch_4x4` | blocos de glitch RGB, 16 frames |
| `vfx_data_bits` | atlas 4×4 de 0/1 e glifos |
| `vfx_scanline` | faixa de varredura para Beam |
| `vfx_spark_elec_4x4` | faísca elétrica, 16 frames |
| `vfx_portal_ring` | anel de portal quântico, 1024² |

---

## 1. QuantumCat — Legendary · gait `ground`

### A. Conceito
Um **gato-mecha de infiltração** (linha "Stealth" da fabricante do MechaTitan). Felino ágil, com **chassi fino de placas de aço e grafite** sobre um **esqueleto de músculo sintético** (cabos e pistões visíveis nas juntas).

A assinatura quântica: o **corpo "se desfaz" em cubos de voxel/glitch** na cauda e nas orelhas, como se estivesse em dois lugares ao mesmo tempo. Um **anel de portal** orbita a cauda.

Pose: andando à espreita, cabeça baixa, uma pata dianteira erguida, cauda alta em S.

### B. Silhueta e proporções
- Comprimento **5,6**, altura **3,4** (até a ponta da cauda), largura 1,4.
- **3 formas-chave:**
  1. corpo felino **alongado e magro**, com dorso arqueado;
  2. **orelhas grandes em lâmina** com antena;
  3. **cauda longa em S** que se fragmenta em cubos.
- **Proporções:**
  - cabeça pequena (0,9), com focinho curto em cunha;
  - pernas longas e finas com **articulação digitígrada** (jarrete alto);
  - patas com 4 dedos em garra retrátil.

### C. Anatomia e construção
- **Núcleo:** gato real (R10). Peito estreito, cintura fina, coxas fortes e afunilamento claro.
- **Placas** derivadas da superfície, no estilo MT3:
  - capacete craniano;
  - placa de focinho;
  - colar segmentado;
  - **dorso em 7 placas sobrepostas** com fenda central de luz;
  - placas de ombro e de coxa;
  - canelas com placa frontal.
- **Juntas expostas:** cotovelo, joelho e jarrete com **pistões e cabos** (grafite e magenta).
- **Cabeça:**
  - **visor em V** (Glow ciano), como os olhos do gato;
  - orelhas em lâmina com borda chanfrada;
  - 2 antenas finas;
  - bigodes = 3 hastes de cada lado.
- **Cauda:** os primeiros 60% em segmentos de vértebra com placas; os 40% finais se **desfazem em 30 cubos** de tamanhos decrescentes, que flutuam com espaçamento, como ilhas separadas.
- **Marcação de série:** "Q-02" pintado no ombro esquerdo e a faixa de aviso na coxa direita, mesma linguagem do "07" do MT3.

### D. Materiais

| Material | Hex | Rough | Metal | Onde |
|---|---|---|---|---|
| aço claro | B8C0CC | 0,35 | 0,9 | placas |
| grafite | 2E3440 | 0,5 | 0,7 | núcleo, juntas |
| navy | 1C2640 | 0,4 | 0,5 | faixas |
| magenta | FF3CA8 | 0,3 | 0,3 | cabos e acentos |

### E. Glow
- **Foco 1:** o **visor em V**.
- **Foco 2:** o **núcleo quântico** no peito: esfera magenta em gaiola, visível por uma janela do peitoral.
- **Secundário:** a fenda do dorso (linha fina ciano) e os cubos da cauda (alternando ciano e magenta).

### F. Marcas de identidade
- "Q-02" + faixa de aviso.
- **Uma orelha com a ponta cortada** e um entalhe em V (gato de rua).

### G. Rig e FX
- **Ossos:**
  - root, pelvis, spine1–3, chest, neck, head, jaw, ear_L, ear_R;
  - 4 pernas × (upper, lower, meta, paw);
  - tail1–8;
  - cubes (1 osso que oscila).
- **Âncoras:** `visor`, `core`, `tail_tip`, `paw_FR`.

### H. VFX
- **Ambiente:**
  - **exclusivo** `quantum_ghost`: a cada 3 s, um **eco translúcido** (flipbook `vfx_glitch_4x4`) do corpo pisca 0,3 stud ao lado;
  - **exclusivo** `portal_ring`: Beam em anel (`vfx_portal_ring`) orbitando a cauda, inclinado;
  - `sparkle` ciano nos cubos.
  - Orçamento normal: 5 emissores, 8 beams, 0 luz.
- **Ação "Blink"** (teleporte):
  1. Antecipação 0,4 s: agacha e os cubos se juntam.
  2. Impacto 0,05 s: **o corpo some** (`Transparency` → 1 no clipe), com burst de cubos e glitch, e **reaparece 2 studs à frente** com anel de portal no destino.
  3. Dissipação 1,0 s.
  - Low: só o burst e o anel.

### I. Animações

| Clipe | Dur | Loop | Notas |
|---|---|---|---|
| Idle | 3,5 | sim | sentado, cauda abanando, orelhas giram, cubos orbitam |
| Walk | 1,4 | sim | felino furtivo, ombros em pêndulo |
| Happy | 2,2 | não | se espreguiça e faz pounce |
| Blink | 1,8 | não | fx em 0,4; deslocamento só visual, o root volta |

### J. Aceitação e proibições
- **Lê como gato** de longe (silhueta felina). As placas seguem a anatomia.
- **Proibido:**
  - cara de cachorro ou raposa;
  - pernas de tubo;
  - visual fofo (olhões);
  - neon espalhado.

---

## 2. AIOverlord — Mythic · gait `fly` (paira)

### A. Conceito
A **IA suprema** da fabricante: um **cérebro-núcleo colossal** dentro de uma **cúpula de vidro blindado**, sustentado por um **tronco de servidor** em anéis, com **6 braços-cabo mecânicos** de garras finas. Uma **coroa de antenas e satélites** completa a figura. Ele não anda: **paira** sobre um anel de propulsão.

Leitura: **chefe final cyberpunk**, entre polvo mecânico e trono de dados. Corrige a v2, uma "água-viva" com o topo rosa confuso.

Pose: ereto, braços abertos em leque (2 altos, 2 médios, 2 baixos), cúpula inclinada à frente como quem observa.

### B. Silhueta e proporções
- Altura **6,4**, largura **5,6** (com braços), paira a 0,6.
- **3 formas-chave:**
  1. **cúpula grande** com cérebro luminoso;
  2. **leque de 6 braços** segmentados;
  3. **coroa de antenas** assimétrica.
- **Proporções:**
  - cúpula Ø 2,2 (35% da altura);
  - tronco que afunila de 1,6 para 0,9;
  - braços com 2,4–3,0;
  - anel de propulsão Ø 2,0 na base.

### C. Construção (hard-surface MT3 puro)
- **Cúpula:** vidro (Spirit, `Transparency` 0,45) com **armação de 8 nervuras** de aço e **frisos de parafusos**.
- **Cérebro:** malha orgânica com sulcos, magenta e ciano, com **linhas de circuito** em relevo (R2).
- **Colar:** anel de grafite com 6 conectores, de onde saem os braços.
- **Tronco:** 4 **módulos de servidor** empilhados, cada um com:
  - painel frontal chanfrado;
  - **grelhas de ventilação**;
  - LEDs de status (Glow pequeno em fila **curta**, permitida aqui);
  - número de série.
  - Cabos pendentes entre os módulos.
- **Braços:**
  - 8–10 segmentos em **vértebra mecânica** (anel com placa dorsal), que afinam;
  - **mão** com 3 garras finas e 1 sensor;
  - 2 braços com ferramenta: um **soldador** (Glow ciano) e uma **lente/scanner**.
- **Coroa:**
  - 3 antenas de alturas diferentes;
  - **2 pratos de satélite** pequenos;
  - 1 **mastro com anel holográfico**.
- **Base:**
  - **anel de propulsão** com 8 bocais;
  - **emissores Glow** voltados para baixo.
- **Marcação:** "Ω-00" no módulo principal e faixa de aviso no anel de propulsão.

### D. Materiais

| Material | Hex | Rough | Metal | Onde |
|---|---|---|---|---|
| aço claro | B8C0CC | 0,35 | 0,9 | armação, braços |
| grafite | 2E3440 | 0,5 | 0,7 | módulos |
| navy | 1C2640 | 0,4 | 0,5 | painéis |
| vidro | AEEBFF | 0,05 | 0 | cúpula, Spirit |
| cérebro | FF3CA8 / 3CF0FF | 0,3 | 0 | emissivo parcial |

### E. Glow e Spirit
- **Foco 1:** o **cérebro** (pulso magenta e ciano).
- **Foco 2:** o **anel de propulsão** (ciano para baixo).
- **Secundário:**
  - LEDs de status;
  - ponta do soldador;
  - lente do scanner;
  - anel holográfico da coroa.
- **Spirit:** a cúpula de vidro e o anel holográfico.

### F. Marcas de identidade
- "Ω-00".
- **Rachadura na cúpula**, remendada com placa parafusada, no lado esquerdo.
- **Um braço é diferente**: de outra cor, um reaproveitamento.

### G. Rig e FX
- **Ossos:**
  - root, base, trunk1–4, collar, dome, brain;
  - 6 braços × 6 ossos + garras;
  - crown, dish_L, dish_R.
- **Âncoras:** `brain`, `thruster` (base), `welder`, `scanner`, `crown_holo`.

### H. VFX
- **Ambiente:**
  - **exclusivo** `data_stream`: `vfx_data_bits` subindo do tronco até a cúpula, Rate 3 (low 1);
  - **exclusivo** `thruster_glow`: beam cônico ciano para baixo + `vfx_hex_grid` no chão, em disco girando;
  - `core_pulse` magenta no cérebro;
  - faíscas no soldador a cada 4 s.
  - Orçamento normal: 8 emissores, 10 beams, 1 luz.
- **Ação "Override":**
  1. Antecipação 0,6 s: os braços recolhem e o cérebro pulsa rápido.
  2. Impacto 0,08 s: **onda de glitch** radial (`vfx_glitch_4x4` em anel) + `vfx_scanline` varrendo de cima para baixo + faíscas dos 6 braços.
  3. Dissipação 1,5 s: bits caindo.
  - Low: onda + scanline.

### I. Animações

| Clipe | Dur | Loop | Notas |
|---|---|---|---|
| Idle | 4,5 | sim | paira; os braços ondulam em defasagem; o cérebro pulsa; a coroa gira os pratos |
| Fly | 2,4 | sim | inclina à frente, braços para trás |
| Happy | 2,5 | não | os 6 braços giram em leque |
| Override | 2,8 | não | fx em 0,6 |

### J. Aceitação e proibições
- **Lê como IA-chefe:** cúpula com cérebro + braços.
- Irmão visual do MechaTitan (mesma linguagem de painéis).
- **Proibido:**
  - água-viva fofa;
  - topo rosa amorfo;
  - braços de tubo liso sem segmentos;
  - olhos de desenho.
