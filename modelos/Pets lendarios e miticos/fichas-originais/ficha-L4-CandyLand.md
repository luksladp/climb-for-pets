# Ficha — CandyLand (área 6): GingerbreadGolem · SugarPhoenix · SprinkleDragon

Lido junto com `2026-10-21_plano-leva4-areas4-7.md` (R1–R10, método, portões, técnica, VFX comum).

**Paleta da área:**

| Cor | Hex |
|---|---|
| rosa-bala (Config) | FF8CC8 |
| gengibre | B86B33 (assado 7A4220, claro D9965A) |
| glacê | F7F2EA (sombra D8CEC4) |
| menta | 6EE0B8 |
| cereja | D62F4A |
| caramelo | D99A2B (âmbar C9781A) |
| chocolate | 3E2418 (ao leite 6B3F26) |
| rosa Glow | FF5FC0 |
| limão Glow | FFE14A |

**Risco desta área:** doce tende a ficar **inflado/fofo**, e o usuário odeia isso. Antídoto obrigatório: **materiais duros e crocantes** (biscoito assado com quina viva, bala dura vítrea facetada, chocolate temperado com aresta seca, glacê em cordão definido). Nada de goma, marshmallow, bochecha ou olho grande e fofo. Cada doce é um objeto de **confeitaria de alta qualidade**, não um brinquedo.

**Texturas de VFX da área (portão C):**
- `vfx_crumb`: migalha de biscoito, 4 variações num atlas 2×2;
- `vfx_sugar_crystal`: cristal de açúcar facetado, 256²;
- `vfx_sprinkle`: confeitos, 6 cores num atlas 3×2;
- `vfx_candy_smoke_4x4`: fumaça rosa algodão-doce, 16 frames;
- `vfx_sugar_sparkle_4x4`: cintila de açúcar, 16 frames;
- `vfx_candy_trail`: faixa de Trail rosa/branca torcida, 512×128.

---

## 1. GingerbreadGolem — Legendary · gait `ground`
### A. Conceito
Um golem guardião feito de **biscoito de gengibre artesanal grosso, decorado com glacê real** (royal icing), como as casas de biscoito de Natal de confeitaria fina. As placas são **biscoitos cortados com forma própria** (escudo, coração, estrela, homenzinho), montados como armadura e unidos por **caramelo/melado**. Nas costas ele carrega uma **casinha de biscoito com lareira acesa**.
Pose: ereto, pesado, punhos fechados ao lado do corpo.
Personalidade: protetor e bonachão.

### B. Silhueta e proporções
- Altura **5,4**, largura **≤ 4,2**, profundidade ~2,4 (com a casinha).
- **3 formas-chave:**
  1. ombros altos e massivos (ombreiras de 3 biscoitos empilhados);
  2. **cabeça de homem-biscoito** (topo arredondado, contorno de cortador);
  3. casinha nas costas, com a chaminé passando acima do ombro esquerdo.
- **Proporções:**
  - tronco em barril largo (1,9) e cintura menor (1,4);
  - antebraços (Ø 0,7) maiores que os braços (0,5);
  - mãos grandes (palma 0,55);
  - pernas curtas e grossas;
  - pés largos.

### C. Anatomia e construção
- **Núcleo:** golem robusto em **caramelo escuro/melado** (8A4A1E, brilho úmido). É ele que aparece nas juntas: **nunca cinza**.
- **Placas = biscoitos** (R10 + assinatura):
  - cada placa tem espessura **0,18–0,25**, topo **levemente abaulado**, **borda assada mais escura com chanfro vivo** e contorno de cortador de biscoito;
  - formas por região:
    - peitoral: 2 escudos grandes + 1 coração central;
    - abdômen: 3 retângulos de cantos curvos com borda ondulada;
    - ombreiras: 3 biscoitos empilhados em escala decrescente (estrela → círculo → homenzinho no topo);
    - coxas e antebraços: placas em gota;
    - canelas: escudo alongado.
- **Glacê** (R2, variado por placa, em relevo no high-poly, bakeado no normal e pintado de branco):
  - peitoral: **zigue-zague** + pontinhos;
  - coração: contorno duplo;
  - abdômen: ondas/escalope;
  - ombreiras: espirais;
  - coxas: "X" costurado;
  - canelas: linha dupla com pontos.
- **Cordões de glacê grosso** escorrendo sobre as juntas grandes (ombro, quadril, joelho), com **gotas penduradas** de comprimentos variados (ilhas rígidas).
- **Cabeça:**
  - biscoito espesso (0,3) em contorno de homem-biscoito;
  - **sobrancelha de glacê grossa e franzida**;
  - olhos de **bala dura vítrea** (Glow) pequenos;
  - boca de glacê em zigue-zague;
  - **mandíbula** como placa separada de biscoito.
- **Botões:** 3 balas duras facetadas no peito (cereja, menta, caramelo).
- **Cinto:** bengala doce com listra em hélice, a única listra do pet.
- **Casinha das costas:**
  - 2 paredes de biscoito com janelinhas de bala (Glow amarelo);
  - telhado de **telhas de chocolate** sobrepostas, com neve de glacê escorrendo pela beira;
  - chaminé de biscoito com tijolinhos de glacê.
- **Mãos:** 3 dedos grossos de biscoito com ponta abaulada e glacê nas pontas, e o polegar.
- **Pés:** biscoito largo, com sola de glacê.

### D. Materiais

| Material | Hex | Rough | Metal | Onde |
|---|---|---|---|---|
| biscoito | B86B33, borda 7A4220, topo D9965A | 0,75 | 0 | placas; porosidade bakeada **em escala média** (nunca granulado fino) |
| glacê | F7F2EA | 0,4 | 0 | decoração |
| caramelo/melado | 8A4A1E | 0,25 | 0 | juntas, aparência úmida |
| bala dura | D62F4A / 6EE0B8 / D99A2B | 0,08 | 0 | botões, olhos |
| chocolate | 3E2418 | 0,35 | 0 | telhado |

### E. Glow
- **Foco 1:** a **lareira**: o coração do peito é vazado como janela, mostrando um **fogo de lareira** (FFE14A → FF5FC0) dentro do peito.
- **Foco 2:** os **olhos de bala**.
- **Secundário:** as janelinhas da casinha e a boca da chaminé.

### F. Marcas de identidade
- Uma **mordida** grande no ombro esquerdo (contorno de dentes, com migalhas na borda).
- 2 **rachaduras** de biscoito (no abdômen e na canela direita), com lascas pequenas soltas na borda.

### G. Rig e FX
- **Ossos:**
  - padrão bípede do MechaTitan (root, pelvis, spine, chest, neck, head, jaw, clavicle, upperarm, forearm, hand, fingers, thumb, thigh, shin, foot);
  - extras: `house`, `chimney`.
- **Âncoras:**
  - `core` (chest, na lareira);
  - `chimney` (boca da chaminé);
  - `fist_L` e `fist_R`.

### H. VFX
- **Ambiente:**
  - **exclusivo** `chimney_smoke`: `vfx_candy_smoke_4x4` rosa saindo da chaminé, 1,0/s (low 0,4), subindo e crescendo;
  - **exclusivo** `crumbs`: 1 emissor no tronco soltando `vfx_crumb` a 0,3/s, caindo (o biscoito esfarela);
  - `core_pulse` amarelo-quente na lareira, piscando como chama (1,1 s);
  - orçamento normal: 4 emissores e 1 luz (lareira).
- **Ação "Stomp":**
  - antecipação 0,5 s: ergue o pé direito e a lareira cresce;
  - impacto em 0,06 s: **anel de glacê** no chão (`fx_ring_soft` branco, Size 1→6) + 14 migalhas em arco + 8 confeitos;
  - dissipação 1,0 s: poeira de açúcar (`sugar_sparkle`);
  - low: anel + 6 migalhas.

### I. Animações

| Clipe | Duração | Loop | Notas |
|---|---|---|---|
| Idle | 3,5 s | sim | respiração; a cabeça inclina; a fumaça da chaminé pulsa |
| Walk | 2,0 s | sim | pesado, ombros balançando |
| Happy | 2,5 s | não | bate as mãos e o glacê "espirra" (pulo leve) |
| Stomp | 2,0 s | não | marcador fx em 0,5 s |

### J. Aceitação e proibições
- Lê como **biscoito decorado**, nunca como "robô de blocos".
- Nenhuma placa é retângulo genérico de canto arredondado.
- O glacê varia por placa.
- As juntas são caramelo, nunca cinza.
- Na cabeça, nada de "orelhas de robô".
- **Proibido:** bevel redondo grande (inflado); granulado fino; cores pastel lavadas.

---

## 2. SugarPhoenix — Legendary · gait `fly`
### A. Conceito
Uma fênix de **vidro de açúcar soprado e bala dura**, translúcida e facetada como cristal de confeitaria (sugar art de competição). A luz atravessa as penas. Contraste da área: o Golem é opaco e crocante, ela é **vítrea e leve**.
Pose: pairando, asas em **V alto a ~60°**, cabeça erguida, cauda de fios de caramelo pendendo em curva.
Personalidade: radiante e vaidosa.

### B. Silhueta e proporções
- Altura **4,8** (corpo de 1,2 a 4,8), envergadura **6,2**, profundidade ≤ 3,4.
- **3 formas-chave:**
  1. V alto das asas;
  2. **peito de caramelo em quilha**, com o tórax 35% maior que na v1;
  3. **cauda de 5 fitas de caramelo puxado** longas (2,2), em curva.
- **Proporções:**
  - tórax: largura 1,2, profundidade 1,4;
  - pescoço em S longo (0,7);
  - cabeça de ave de rapina, com 1,0 de comprimento;
  - **coxas emplumadas e garras de caramelo grossas** (nunca palito).

### C. Anatomia e construção
- **Núcleo:** ave de rapina, com quilha profunda.
- **Peito:** **placa de caramelo âmbar** (C9781A) em escudo, com facetas como pedra lapidada (R2: faceta central plana, bordas chanfradas).
- **Penas do corpo:** escamas de **bala dura** facetadas (crista central em V, 2 faces), em degradê por fileira: cereja no pescoço → rosa no corpo → caramelo no ventre.
- **Asas:**
  - coberteiras em 3 fileiras de penas curtas de bala;
  - 6 secundárias;
  - **7 primárias longas** (1,6 → 2,3);
  - todas **facetadas** (2 faces com crista) e afunilando;
  - as **2 fileiras externas** de primárias e secundárias são Spirit (vidro);
  - **pontas com cristal de açúcar** (Glow).
- **Cabeça:**
  - bico de caramelo duro em 2 placas;
  - sobrancelha facetada;
  - olho pequeno (Glow limão);
  - **crista de 5 lâminas sólidas para trás**, com um **disco de pirulito em espiral em relevo** achatado na ponta das 3 centrais (crista coesa, nunca antena).
- **Cauda:** 5 **fitas de caramelo puxado**. Cada uma é uma lâmina larga (0,3) e fina com torção leve, que afunila e termina numa **gota de bala** (Glow rosa).
- **Patas:** coxas com penas de bala, tarso de caramelo e **4 garras de caramelo** grossas.

### D. Materiais

| Material | Hex | Rough | Metal | Onde |
|---|---|---|---|---|
| bala dura | D62F4A / FF8CC8 / D99A2B | **0,08–0,12** | 0 | penas; na Color, degradê interno (centro saturado, borda clara) + **1 linha branca de reflexo** por pena |
| caramelo âmbar | C9781A | 0,15 | 0 | peito, bico, garras |
| açúcar cristal | F7F2EA | 0,3 | 0 | arestas das facetas, filete fino |

### E. Glow e Spirit
- **Foco 1:** o **coração de caramelo**: brilho atrás da placa do peito, visto pelas facetas (FFE14A).
- **Foco 2:** os **cristais das pontas das asas** (rosa FF5FC0).
- **Secundário:** gotas da cauda, olhos, disco central da crista.
- **Spirit:** as 2 fileiras externas de penas das asas (Transparency 0,3), cor rosa.

### F. Marcas de identidade
- A crista tem **um pirulito lascado** (falta um pedaço da espiral).
- Uma das fitas da cauda tem **um nó** (dobra sobre si).

### G. Rig e FX
- **Ossos:**
  - root, body, chest, neck1, neck2, head, jaw, crest;
  - por asa: shoulder, arm, forearm, hand, prim_a, prim_b, sec;
  - tail1, ribbon1–5 (2 ossos cada);
  - por perna: thigh, tarsus, toes.
- **Âncoras:**
  - `core` (chest);
  - `tail` (ribbons);
  - `wing_L` e `wing_R` (pontas).

### H. VFX
- **Ambiente:**
  - **exclusivo** `sugar_glints`: `vfx_sugar_sparkle_4x4` em 4 pontos orbitando nas asas (preset `sparkle` recolorido em branco/rosa), simulando luz batendo no vidro;
  - **exclusivo** `candy_trail`: Trail com `vfx_candy_trail` nas 2 pontas de asa, só em movimento;
  - `core_pulse` amarelo, 1,6 s;
  - orçamento normal: 5 emissores e 2 trails.
- **Ação "Sparkle":**
  - antecipação 0,4 s: as asas fecham e a luz interna sobe;
  - impacto em 0,06 s: as asas abrem com **estouro de cristais** (`vfx_sugar_crystal`, 18 radiais girando) + `fx_halo_soft` rosa;
  - dissipação 1,4 s: os cristais caem e se apagam, com cintilas;
  - low: halo + 8 cristais.

### I. Animações

| Clipe | Duração | Loop | Notas |
|---|---|---|---|
| Idle | 3,0 s | sim | paira, batida lenta; as fitas da cauda ondulam com atraso |
| Fly | 1,2 s | sim | batida completa |
| Happy | 2,2 s | não | giro + pose de asas abertas |
| Sparkle | 2,0 s | não | marcador fx em 0,4 s |

### J. Aceitação e proibições
- Lê como **vidro/bala dura**: facetas e reflexo visíveis no close; roughness baixa.
- Corpo proporcional às asas.
- A cauda é de fitas largas (nunca vareta com bolinhas).
- A crista é coesa (nunca antena).
- **Proibido:** penas em losango chapado; aparência de plástico opaco; bolas redondas.

---

## 3. SprinkleDragon — Mythic · gait `ground`
### A. Conceito
Um dragão de **confeitaria de luxo**: escamas de **chocolate temperado** com quina viva e brilho seco; dorso coberto por **glacê real escorrendo**, com confeitos incrustados; chifres de **bengala doce** em hélice; espinhos de **bala dura** cristalina; barriga de **wafer e caramelo**; e uma **coroa de cristais de açúcar** (Mythic). É o "bolo de casamento" dos dragões: excessivo mas organizado.
Pose: em 4 patas, **corpo baixo e robusto** (contra o MoltenDragon, que é alongado), peito estufado e cabeça erguida com a boca entreaberta.
Personalidade: um glutão orgulhoso.

### B. Silhueta e proporções
- Altura **6,4** (topo dos chifres), comprimento **≤ 9,0**, largura do tórax **2,8**.
- **3 formas-chave:**
  1. **chifres de bengala grandes** em espiral;
  2. corpo robusto, com a "cobertura" de glacê no dorso;
  3. cauda terminando em **cristal de açúcar** grande.
- **Proporções:**
  - pescoço curto e grosso (22% do comprimento);
  - patas com coxa larga;
  - **patas ~40% maiores que na v1**;
  - cabeça grande (1,5).

### C. Anatomia e construção
- **Núcleo:** dragão musculoso, com peito profundo (2,2) e ancas largas.
- **Escamas de chocolate:** placas em gota sobrepostas no dorso e nos flancos. O chocolate amargo (3E2418) tem **borda com quina viva** e o campo interno com **padrão de tablete** em relevo (R2: 4 quadrados rebaixados), só nas escamas grandes. Nos flancos, chocolate ao leite e escamas menores.
- **Espinhos:** fileira dupla de **bala dura cristalina** (rosa → menta, em degradê do pescoço à cauda), facetados, de 0,5 a 0,15.
- **Cobertura de glacê:** uma faixa contínua de glacê branco **escorrendo pela linha do dorso**, do pescoço até 2/3 da cauda, com **gotas penduradas** de comprimentos variados nos flancos. É uma ilha grossa, com borda definida. Os **confeitos** ficam incrustados **só no glacê**: 6 cores, ~80 confeitos (cilindros curtos, ilhas pequenas ou bake), nunca no corpo todo.
- **Barriga:** 12 placas de **wafer** (grade de wafer em relevo bakeado), mais largas no peito e estreitando, com bordas de caramelo.
- **Cabeça:**
  - focinho largo e anguloso;
  - **sobrancelha de chocolate pesada**;
  - **dentes de açúcar branco** visíveis;
  - narinas;
  - **2 chifres de bengala** (1,3), com a **listra em hélice contínua** (2 faixas vermelhas torcidas na geometria, como ilhas separadas brancas e vermelhas);
  - 2 chifres pequenos de chocolate.
- **Coroa (Mythic):** 5 **cristais de açúcar** facetados em arco na nuca, o central maior (0,5).
- **Asas fechadas:** dobradas rente ao corpo, com o cotovelo alto. Os dedos são de **chocolate em barra** e a membrana é de **bala dura translúcida** (Spirit), com veios de glacê; garra de chocolate no polegar.
- **Patas:** coxa e ombro musculosos de chocolate, canela afunilando e **dedos separados com garras de açúcar**.
- **Cauda:** termina num **cristal de açúcar facetado** grande (0,7), engastado em chocolate.

### D. Materiais

| Material | Hex | Rough | Metal | Onde |
|---|---|---|---|---|
| chocolate amargo | 3E2418 | 0,3 | 0 | brilho temperado; escamas |
| chocolate ao leite | 6B3F26 | 0,35 | 0 | flancos |
| glacê | F7F2EA | 0,4 | 0 | cobertura |
| wafer | D9A866 | 0,7 | 0 | barriga |
| caramelo | D99A2B | 0,2 | 0 | bordas da barriga |
| bala dura | FF8CC8 → 6EE0B8 | 0,08 | 0 | espinhos |
| bengala | F7F2EA / D62F4A | 0,15 | 0 | chifres |
| açúcar cristal | EAF6FF | 0,1 | 0 | coroa, cauda |

### E. Glow e Spirit
- **Foco 1:** a **coroa de cristais** (luz interna rosa-limão).
- **Foco 2:** a **garganta**: brilho rosa entre as placas de wafer do peito e na boca.
- **Secundário:** o cristal da cauda e os olhos.
- **Spirit:** a membrana das asas (Transparency 0,3), rosa.

### F. Marcas de identidade
- Um chifre de bengala tem a **ponta mordida**.
- **Uma gota de glacê** longa escorre até o joelho dianteiro esquerdo.

### G. Rig e FX
- **Ossos:**
  - root, pelvis, spine1–3, chest, neck1–3, head, jaw;
  - 4 pernas × (upper, lower, foot, toes);
  - tail1–7;
  - por asa: shoulder, arm, forearm, hand, finger1–4.
- **Âncoras:**
  - `mouth` (jaw);
  - `core` (chest);
  - `crown` (head);
  - `tail` (cristal).

### H. VFX
- **Ambiente:**
  - **exclusivo** `sprinkle_rain`: confeitos (`vfx_sprinkle`) caindo devagar do dorso e quicando, a 1,5/s (low 0,6), girando e com vida de 1,8 s;
  - `sparkle` com `sugar_sparkle` na coroa e no cristal da cauda;
  - `core_pulse` rosa na garganta;
  - orçamento normal: 6 emissores e 1 luz.
- **Ação "Breath":** sopro de açúcar.
  - antecipação 0,6 s: ergue a cabeça e a garganta brilha;
  - impacto em 0,08 s: **jato cônico** de cintilas de açúcar + confeitos + fumaça rosa;
  - dissipação 1,4 s: os confeitos caem e quicam;
  - low: 1 emissor do jato + 10 confeitos.

### I. Animações

| Clipe | Duração | Loop | Notas |
|---|---|---|---|
| Idle | 4,0 s | sim | respiração; a cauda abana; lambe os lábios |
| Walk | 1,8 s | sim | quadrúpede robusto, gingado |
| Happy | 3,0 s | não | sacode o corpo como cachorro, os confeitos voam |
| Breath | 2,4 s | não | marcador fx em 0,6 s |

### J. Aceitação e proibições
- Pernas de dragão (músculo + afunilamento), nunca blocos.
- Listra helicoidal contínua nos chifres (nunca xadrez).
- O glacê é uma faixa contínua, com os confeitos só nela.
- Asas dobradas (nunca velas em pé).
- Comprimento ≤ 9.
- **Proibido:** confeitos espalhados no corpo todo; listras zebradas fora dos chifres e do cinto; cores pastel lavadas.
