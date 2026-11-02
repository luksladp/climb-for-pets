# Ficha — SkyKingdom (área 8): SkyWhale · Seraph · SkyEmperor

Lido junto com `2026-10-21_plano-leva4-areas4-7.md`: R1–R10, método R10, portões A/B/C, técnica §3 e VFX §4. Valem igual para as áreas 8–10.

**Versão atual no jogo:** voxel realista v2/v3 (Seraph v3 = anjo azul/dourado com 6 asas; SkyEmperor v2; SkyWhale v2 com 5,12 de altura, limitado pelo comprimento). **Esta leva substitui** por hard-surface no nível do MechaTitan v3. A versão atual fica no jogo até a integração.

**Paleta da área:**
| Papel | Hex |
|---|---|
| céu (Config) | C8E6FF |
| mármore celeste | F2F4F8 (sombra C9D2DE) |
| azul-real | 2A4C9A (escuro 1A2E66) |
| ouro-sol | E8B83A (escuro A87A1E) |
| bronze-nuvem | B89A6A |
| porcelana | EAF2FA |
| Glow sol | FFE58A |
| Glow céu | 9AD8FF |
| Spirit | nuvem/luz translúcida |

**Linguagem da área:** **arquitetura celestial**. Mármore polido com **frisos e molduras de templo** (dentículos, volutas, caneluras), ouro em filetes elevados, porcelana fina. Formas **verticais, simétricas e régias**, com halos e asas em lâminas.
**Risco do tema:** "bolo de noiva" branco sem contraste. Antídoto: o azul-real escuro como valor escuro obrigatório (R3) em ≥ 25% da superfície.

**Texturas de VFX da área (portão C):**
- `vfx_cloud_puff_4x4` (nuvem cartoon, 16 frames);
- `vfx_feather_light` (pena de luz, 256²);
- `vfx_sunray` (raio de sol para Beam, 512×128);
- `vfx_halo_ring` (anel dourado com runas celestiais, 1024², alfa);
- `vfx_wind_streak` (traço de vento, 512×64).

---

## 1. SkyWhale — Legendary · gait `swim` (flutua no ar)
### A. Conceito
Uma **baleia-jubarte navio-celeste**: o corpo é casco de **porcelana e mármore** com placas sobrepostas como um galeão. As nadadeiras peitorais longas são **velas/asas de lâminas douradas**. **Nada em cima das costas** (decisão do usuário, 22/10: sem cidadela, crista, jardim ou objetos): o dorso é liso, coberto pelas lajes de mármore, com no máximo uma barbatana dorsal baixa de jubarte. É uma baleia do céu majestosa e calma.
**Pose:** flutuando, levemente inclinada para cima (10°), nadadeiras abertas em planeio, cauda erguida em curva.

### B. Silhueta e proporções
- Comprimento **7,6** · altura **~3,6** (sem a cidadela) · envergadura das peitorais **6,4** · corpo flutua a 1,2 (pivô no chão).
- **3 formas-chave:**
  1. corpo de jubarte com **ventre sulcado** e cabeça maciça;
  2. **peitorais enormes** (40% do comprimento), em lâminas;
  3. **cauda (fluke) grande** em lâminas, erguida em curva.
- **Proporções:** cabeça 30% do comprimento; maior altura do corpo 2,0 no terço anterior; pedúnculo da cauda Ø 0,5; cauda (fluke) 2,4 de largura.

### C. Anatomia e construção
- **Núcleo:** jubarte real (cabeça larga e achatada no topo, mandíbula saliente, corpo em gota afunilando para a cauda).
- **Ventre:** **sulcos ventrais** como 14 placas longas de porcelana, da mandíbula até o umbigo, com frestas azul-real entre elas.
- **Dorso:** placas de **mármore** em escudo, sobrepostas na direção da cauda, com borda de friso dourado. São maiores no dorso e menores nos flancos.
- **Tubérculos da cabeça** (marca da jubarte): **rosetas douradas** em fileira no rostro (8).
- **Peitorais:**
  - "asa" com 7 lâminas longas de mármore, que afunilam, com borda frontal recortada em **tubérculos-escalope** (como a jubarte real);
  - filete dourado ao longo de cada lâmina;
  - pontas Glow céu.
- **Cauda (fluke):** 2 lobos com borda traseira **serrilhada** e as mesmas lâminas.
- **Cidadela: REMOVIDA** (usuário, 22/10). Dorso liso com lajes de mármore; barbatana dorsal baixa opcional.
- **Olho:** pequeno, sábio, com sobrancelha de friso.

### D. Materiais
| Material | Hex | Rough | Metal | Onde |
|---|---|---|---|---|
| mármore | F2F4F8 | 0,25 | 0 | dorso, peitorais |
| porcelana | EAF2FA | 0,15 | 0 | ventre |
| azul-real | 1A2E66 | 0,4 | 0,1 | frestas, faixa lateral, vão das colunas |
| ouro-sol | E8B83A | 0,25 | 1 | filetes, rosetas, cúpula |

### E. Glow e Spirit
- **Foco 1:** **sulcos do ventre** com luz céu (o "porão iluminado").
- **Foco 2:** **olho** sábio (âmbar com aro de ouro) e **espiráculo** com brilho suave.
- **Secundário:** pontas das peitorais, olho.
- **Spirit:** nuvens macias sob a barriga; rastro de nuvem sob a cauda.

### F. Marcas de identidade
- **Cicatriz de arpão**: 3 placas do flanco esquerdo trincadas e remendadas com **grampos de ouro**.

### G. Rig e FX
- **Ossos:** root, body1–3, head, jaw, pec_L/R (3 cada), tail1–4, fluke (osso `citadel` removido).
- **Âncoras:** `belly` (body2), `fluke`, `blowhole` (topo da cabeça).

### H. VFX
- **Ambiente:**
  - **exclusivo** `cloud_wake`: `vfx_cloud_puff_4x4` atrás da fluke, a 1,2/s (low 0,5);
  - **exclusivo** `blow_spray`: jato de nuvem pelo espiráculo a cada 6 s;
  - `core_pulse` céu nos sulcos do ventre;
  - orçamento normal: 4 emissores, 1 luz.
- **Ação "Song":**
  - antecipação 0,6 s: a cabeça sobe e os sulcos do ventre escurecem;
  - impacto 0,08 s: **3 anéis sonoros** dourados (`fx_ring_soft` + `vfx_halo_ring`) expandindo à frente + raios de sol (`vfx_sunray`, 6 beams curtos) do espiráculo;
  - dissipação 1,5 s: penas de luz caindo;
  - low: 1 anel + 2 raios.

### I. Animações
| Clipe | Dur | Loop | Notas |
|---|---|---|---|
| Idle | 5,0 | sim | ondula vertical lenta; as peitorais remam suave; sobe e desce 0,2 |
| Swim | 3,0 | sim | batida da fluke com o corpo acompanhando |
| Happy | 3,0 | não | rolamento de 360° no eixo longo |
| Song | 2,8 | não | marcador fx em 0,6 |

### J. Aceitação e proibições
- Lê como **jubarte** (sulcos, peitorais longas, tubérculos), não como baleia genérica nem dirigível.
- **Nada em cima das costas** (sem cidadela/prédio/crista/jardim).
- **Proibido:** cascos de barco literais (madeira/velas de pano); hélices; janelas de avião; mármore sem contraste.

---

## 2. Seraph — Legendary · gait `fly`
### A. Conceito
Um **serafim guardião de armadura celestial**: um ser alado sem rosto humano. O rosto é uma **máscara de porcelana lisa com um único olho-sol** em fenda. Veste **armadura de placas de mármore e ouro** (estilo paladino art déco) e tem **6 asas** (2 cobrindo o rosto/peito, 2 abertas para voo, 2 cobrindo os pés), feitas de **lâminas de mármore com filete de ouro**. Tem um **halo** atrás da cabeça e uma **lança de luz** na mão direita. Corrige a v2/v3, "pequeno/fino e difícil de ler de longe".
**Pose:** pairando, ereto, as asas superiores em V alto, as de baixo cruzadas sob o corpo, a lança vertical.

### B. Silhueta e proporções
- Altura **5,8** (até a ponta das asas), envergadura **6,0**, corpo flutua a 0,8.
- **3 formas-chave:**
  1. **3 pares de asas** em leque hexagonal;
  2. torso em V de armadura com **ombreiras em voluta**;
  3. halo com raios.
- **Proporções:** torso largo (1,6 nos ombros), cintura 0,8; o corpo some sob as asas inferiores (sem pernas visíveis, só a cauda de lâminas); cabeça 0,55 com a máscara.

### C. Anatomia e construção
- **Núcleo:** torso atlético, braços musculosos, quadril que se transforma em **cauda de lâminas** (sem pernas).
- **Armadura:**
  - **peitoral** com **sol art déco em relevo** (raios escalonados) e cintura marcada;
  - **ombreiras em voluta dupla** (concha jônica) com 3 camadas;
  - **braçais** só com placa frontal e caneluras;
  - **manoplas** de ouro com dedos articulados;
  - **saia de lâminas** longas (8) que viram a cauda.
- **Máscara:** porcelana oval lisa, com uma **fenda horizontal única** (o olho-sol) e uma coroa de 5 raios dourados na testa.
- **Asas:**
  - cada uma tem **ombro de ouro** (articulação mecânica elegante, tipo relojoaria) e **3 fileiras de lâminas** (coberteiras curtas, médias e primárias longas de 1,6–2,4);
  - mármore com **filete de ouro**;
  - as **pontas** azul-real escuras (contraste R3).
- **Halo:** anel de ouro com 12 raios e runas celestiais, preso ao dorso por uma haste fina (mais `vfx_halo_ring` no FX).
- **Lança:** haste de ouro com **ponta de cristal de luz** (Glow), comprimento 5,4.

### D. Materiais
| Material | Hex | Rough | Metal | Onde |
|---|---|---|---|---|
| mármore | F2F4F8 | 0,25 | 0 | armadura base, asas |
| ouro-sol | E8B83A | 0,2 | 1 | volutas, filetes, manoplas, halo |
| azul-real | 2A4C9A / 1A2E66 | 0,35 | 0,2 | tecido sob a armadura, pontas das asas, faixas |
| porcelana | EAF2FA | 0,1 | 0 | máscara |

### E. Glow e Spirit
- **Foco 1:** o **olho-sol** da máscara (fenda FFE58A intensa).
- **Foco 2:** a **ponta da lança**.
- **Secundário:** o sol do peitoral (linhas finas), as runas do halo.
- **Spirit:** penas de luz na borda das primárias (fileira externa translúcida).

### F. Marcas de identidade
- **Uma lâmina de asa partida** (superior esquerda), com a ponta faltando.
- Uma **faixa de tecido azul** rasgada pendendo da cintura, só à direita.

### G. Rig e FX
- **Ossos:** root, pelvis, spine, chest, neck, head; clavicle/upperarm/forearm/hand/fingers ×2; wing_top/mid/low_L/R (3 ossos cada); tail1–4; spear; halo.
- **Âncoras:** `eye`, `spear_tip`, `halo`, `chest`.

### H. VFX
- **Ambiente:**
  - **exclusivo** `feather_fall`: `vfx_feather_light` caindo das asas, 0,8/s (low 0,3);
  - `halo_glow` (preset existente, recolorido ouro) no halo;
  - `sparkle` sol na ponta da lança;
  - orçamento normal: 5 emissores, 2 beams, 1 luz.
- **Ação "Judgement":**
  - antecipação 0,5 s: as 6 asas abrem e a lança sobe;
  - impacto 0,06 s: **coluna de luz** vertical (`vfx_sunray` em 4 beams) descendo da lança + `fx_halo_soft` dourado expandindo + 16 penas;
  - dissipação 1,4 s;
  - low: coluna com 2 beams + halo.

### I. Animações
| Clipe | Dur | Loop | Notas |
|---|---|---|---|
| Idle | 4,0 | sim | paira; as asas respiram em defasagem por par; o halo gira lento |
| Fly | 1,6 | sim | as asas médias batem; as outras ajustam |
| Happy | 2,5 | não | as 6 asas abrem em estrela e há um giro |
| Judgement | 2,4 | não | marcador fx em 0,5 |

### J. Aceitação e proibições
- **Lê de longe a 30 studs** (o defeito da v2/v3): asas grandes e contrastadas, torso largo.
- A máscara é lisa, com 1 fenda.
- **Proibido:** rosto humano; asas de penas macias (usar lâminas); armadura lisa sem friso; branco puro sem azul.

---

## 3. SkyEmperor — Mythic · gait `fly`
### A. Conceito
O **Imperador dos Céus**: um **grifo-leão colossal** de armadura imperial. Corpo de leão (patas traseiras) e de águia (cabeça, patas dianteiras com garras, asas), coberto de **placas de mármore e ouro** em camadas, com **juba de lâminas douradas** em raios solares. Na cabeça, uma **coroa-templo** (arco de colunas). No peito, um **medalhão-sol**. É a peça mais régia do jogo: **trono vivo**.
**Pose:** sentado nas patas traseiras, ereto, uma pata dianteira erguida, as asas meio abertas para cima e para trás.

### B. Silhueta e proporções
- Altura **6,6** (topo da coroa), comprimento 6,0, envergadura (meio aberta) **7,0**.
- **3 formas-chave:**
  1. **juba solar** em raios ao redor da cabeça;
  2. **asas em V largo** acima do corpo;
  3. **postura sentada régia** (tipo estátua de leão de palácio).
- **Proporções:** peito profundo (2,0), patas dianteiras de águia com garras grandes (0,5), traseiras de leão musculosas, cauda de leão longa com tufo de lâminas.

### C. Anatomia e construção
- **Núcleo:** grifo real (peito e ombros de águia, ancas de leão).
- **Penas do peito e da cabeça:** **escamas-pena de mármore** em gota com quilha central, que diminuem para a cabeça.
- **Corpo traseiro:** **placas de armadura** de mármore com **friso grego** (meandro) em relevo nas bordas, sobrepostas.
- **Juba:** 3 anéis de **lâminas douradas** (24 no total) em raios, alternando comprimentos (0,6/0,9/1,2), com caneluras. **Forma-chave nº 1.**
- **Cabeça:**
  - bico de águia de **ouro** com placa superior e inferior;
  - **sobrancelha de mármore pesada**;
  - olhos Glow céu.
- **Coroa-templo:** arco de 5 colunas jônicas mini, com frontão triangular e uma **gema-sol** central (Mythic).
- **Asas:** o mesmo kit de lâminas do Seraph em versão maior e mais robusta (4 fileiras), com o ombro de ouro em voluta e as pontas azul-real.
- **Patas dianteiras:** escamas de ouro (tarso de águia), 4 garras.
- **Patas traseiras:** de leão, com placa de coxa e pata de 4 dedos com garras retráteis à mostra.
- **Cauda:** leonina, com segmentos de placas e o tufo final em 5 lâminas douradas.
- **Medalhão-sol:** no peito, disco de ouro com sol art déco e uma gema central.

### D. Materiais
| Material | Hex | Rough | Metal | Onde |
|---|---|---|---|---|
| mármore | F2F4F8 | 0,25 | 0 | penas, placas |
| ouro-sol | E8B83A / A87A1E | 0,2 | 1 | juba, bico, garras, coroa, medalhão |
| azul-real | 1A2E66 | 0,35 | 0,2 | frestas, pontas das asas, faixa do ventre |
| bronze-nuvem | B89A6A | 0,4 | 0,6 | segunda cor da armadura (camada de baixo) |

### E. Glow e Spirit
- **Foco 1:** a **gema-sol da coroa** (FFE58A).
- **Foco 2:** o **medalhão do peito**.
- **Secundário:** olhos, o meandro das placas (fio fino), as pontas da juba.
- **Spirit:** penas de luz nas primárias; nuvem rente às patas.

### F. Marcas de identidade
- **Uma coluna da coroa faltando** (a 2ª da direita).
- A **garra dianteira direita** é de **ouro maciço** (substituta), diferente das outras.

### G. Rig e FX
- **Ossos:** root, pelvis, spine1–3, chest, neck1–2, head, jaw(beak), mane; 4 pernas × 4; wing ×2 (shoulder/arm/forearm/hand + 4 fileiras); tail1–6.
- **Âncoras:** `crown`, `medallion`, `mane`, `wing_L/R`.

### H. VFX
- **Ambiente:**
  - **exclusivo** `sun_corona`: `halo_glow` + 12 beams curtos (`vfx_sunray`) em volta da juba, girando lento (low: 6 beams estáticos);
  - **exclusivo** `cloud_throne`: nuvens (`vfx_cloud_puff`) rolando sob as patas, 1/s;
  - `sparkle` na coroa;
  - orçamento normal: 7 emissores, 12 beams, 1 luz.
- **Ação "Roar":**
  - antecipação 0,6 s: a juba recolhe e a coroa escurece;
  - impacto 0,08 s: a juba abre num **flash solar**, onda de vento (`vfx_wind_streak` radial) e anel dourado no chão;
  - dissipação 1,6 s: penas e nuvens;
  - low: flash + anel.

### I. Animações
| Clipe | Dur | Loop | Notas |
|---|---|---|---|
| Idle | 4,5 | sim | sentado; respira; a cauda balança; as asas ajustam; a juba vibra |
| Fly | 1,8 | sim | voo planado com batida ampla |
| Happy | 3,0 | não | ergue-se nas traseiras e abre as asas |
| Roar | 2,8 | não | marcador fx em 0,6 |

### J. Aceitação e proibições
- **Grifo** legível (cabeça e garras de águia + ancas de leão).
- Juba e coroa leem a 30 studs.
- Distinto do Seraph (quadrúpede vs humanoide).
- **Proibido:** penas macias/fofas; leão "fofo" de cara grande; branco sem contraste.
