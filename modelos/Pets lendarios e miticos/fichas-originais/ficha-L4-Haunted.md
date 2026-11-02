# Ficha — Haunted (área 7): HeadlessHorse · Banshee · LichKing

Lido junto com `2026-10-21_plano-leva4-areas4-7.md` (R1–R10, método, portões, técnica, VFX comum).

**Paleta da área:**

| Cor | Hex | Uso / variações |
|---|---|---|
| roxo-assombrado (Config) | 965AC8 | |
| preto-ferro | 1A1820 | |
| ferro escuro | 3A3842 | aresta gasta 6A6878 |
| prata-velha | 9A9AA6 | highlight C8C8D2 |
| osso | D9CFB4 | AO 8A7A5A, rachaduras 6A5A40 |
| tecido-roxo | 3B1F4F | borda 5A3A72 |
| ferrugem | 7A4A2A | só nas bordas |
| espectro Glow | 7CFFB0 | |
| arcano Glow | C98BFF | |

O **Spirit** é ectoplasma translúcido.

**Linguagem hard-surface do tema:**
- **armadura gótica de ferro forjado**: bordas recortadas em arco ogival, lóbulos e dentes; fluting (nervuras em relevo); filete de prata elevado; camadas sobrepostas;
- **osso com anatomia real**: epífises largas, haste curva, crânio com arcada, zigomático e órbitas fundas;
- **tecido como lâminas rígidas de pano endurecido**: borda rasgada em tiras, nunca pano mole.

**Texturas de VFX da área (portão C):**
- `vfx_ghost_flame_8x8`: chama espectral verde cartoon, 64 frames;
- `vfx_ecto_wisp_4x4`: fiapo de ectoplasma, 16 frames;
- `vfx_soul_orb`: orbe com rosto vago, 256²;
- `vfx_rune_circle`: círculo de runas para Beam/decal, 1024², alfa;
- `vfx_rune_glyph`: atlas 4×4 com 16 runas;
- `vfx_fog_4x4`: névoa baixa, 16 frames;
- `vfx_sound_ring`: anel de onda sonora distorcida, 512².

---

## 1. HeadlessHorse — Legendary · gait `ground`
### A. Conceito
O **cavalo de guerra do cavaleiro sem cabeça**: corcel enorme protegido por **barda gótica de cavaleiro** (ferro forjado com filigrana de prata), cuja cabeça foi substituída por uma **chama espectral verde** que sai de uma gola de ferro. Entre as placas da barda aparece um **corpo esquelético** (costelas, vértebras).
Pose: de pé, parado em guarda, com uma pata dianteira levemente erguida (impaciente). A chama inclina para trás.
Personalidade: furioso e leal.

### B. Silhueta e proporções
- Altura **5,4** (topo da chama), comprimento **≤ 6,6**, largura ~2,4.
- **3 formas-chave:**
  1. **pescoço curto, grosso e arqueado**, cavalo de guerra (frísio), com a chama alta;
  2. tronco em **barril** com peito largo e garupa musculosa;
  3. pernas fortes com **cascos grandes de ferro**.
- **Proporções:**
  - pescoço 25% mais curto que na v1, inclinado à frente;
  - peito com 1,4 de largura e profundidade do barril 1,6;
  - antebraço e gaskin musculosos (Ø 0,4);
  - canelas com Ø 0,22;
  - cascos com Ø 0,45.

### C. Anatomia e construção
- **Núcleo:** cavalo realista, com o corpo interno em **osso** (o frame aparece como **costelas** nas frestas do flanco e **vértebras** na linha do dorso, entre as placas).
- **Barda** (placas derivadas da superfície):
  - **chanfron:** ausente, não há cabeça;
  - **crinet** (pescoço): 6 lâminas sobrepostas que afunilam, cada uma com borda recortada em arco e fluting central;
  - **peitoral:** placa grande com nervura central, **caveira de cavalo entalhada em relevo** e 2 asas laterais recortadas;
  - **flancos:** 2 placas por lado (com borda de lóbulos e filete de prata), abertas embaixo, mostrando as costelas;
  - **garupa:** placa dupla em escudo, com fluting radial.
  - Desgaste: ferrugem e lascas **só nas bordas**, e um amassado.
- **Gola do pescoço:** anel gótico de ferro com 6 pontas para cima (a única forma de anel, por ser uma gola) e, de dentro dela, a chama.
- **Sela:** couro escuro em placas, com arções altos; estribos de ferro pendentes; manta de tecido rasgado sob a sela, em lâminas.
- **Pernas:** músculo de cavalo, com joelho e jarrete ósseos marcados, **caneleiras de ferro** só na frente, e **cascos de ferro** com ferradura de cravos e topo em osso.
- **Crina e cauda:** **lâminas de fogo espectral** longas e variadas (crina com 7, cauda com 6), inclinadas para trás como se ele corresse.

### D. Materiais

| Material | Hex | Rough | Metal | Onde |
|---|---|---|---|---|
| ferro escuro | 3A3842, arestas 6A6878 | 0,45 | 0,85 | barda |
| prata-velha | 9A9AA6 | 0,3 | 0,95 | filetes, entalhes |
| osso | D9CFB4 + AO | 0,6 | 0 | costelas, vértebras, topo dos cascos |
| couro | 2A1A14 | 0,7 | 0 | sela |
| tecido-roxo | 3B1F4F | 0,85 | 0 | manta |

### E. Glow e Spirit
- **Foco 1:** a **chama do pescoço**: 3 camadas de lâminas curvas recortadas (núcleo Glow alto e estreito, camada média Spirit, pontas externas finas assimétricas), altura 1,3.
- **Foco 2:** os **4 cascos**: um anel fino de chama Glow na base de cada um.
- **Secundário:**
  - núcleo Glow das lâminas da crina e da cauda;
  - o entalhe da caveira do peitoral (olhos da caveira).
- **Spirit:** camada externa da chama, crina e cauda (Transparency 0,4).

### F. Marcas de identidade
- **Uma flecha quebrada** cravada na placa do flanco esquerdo.
- A gola tem **uma ponta torta**.

### G. Rig e FX
- **Ossos:**
  - root, pelvis, spine1–3, chest;
  - neck1–3, flame1–2;
  - 4 pernas × (upper, lower, pastern, hoof);
  - tail1–5, mane1–3, saddle.
- **Âncoras:**
  - `flame` (flame1);
  - `hoof_FL`, `hoof_FR`, `hoof_BL`, `hoof_BR`;
  - `core` (chest).

### H. VFX
- **Ambiente:**
  - **exclusivo** `ghost_flame`: emissor em `flame` com `vfx_ghost_flame_8x8` a Rate 6 (low 3), vida 0,6 s, subindo e inclinando para trás;
  - **exclusivo** `hoof_embers`: por casco, 1 brasa verde a 0,5/s (low: só nas patas da frente);
  - `ecto_wisp` sutil saindo da crina;
  - orçamento normal: 6 emissores e 1 luz (chama, verde).
- **Ação "Rear"** (empinar):
  - antecipação 0,5 s: recua e a chama encolhe;
  - impacto em 0,06 s: as patas descem, **anel de fogo verde no chão** (`fx_ring_soft` verde, Size 1→7) e rajada de brasas dos cascos;
  - dissipação 1,2 s: fiapos de ectoplasma;
  - low: anel + 8 brasas.

### I. Animações

| Clipe | Duração | Loop | Notas |
|---|---|---|---|
| Idle | 3,5 s | sim | a pata raspa o chão; a chama tremula; a cauda balança |
| Walk | 1,6 s | sim | passo de cavalo (4 tempos); a crina flui |
| Happy | 2,5 s | não | **empina** e relincha (a chama explode para cima) |
| Rear | 2,2 s | não | marcador fx em 0,5 s, quando as patas tocam o chão |

### J. Aceitação e proibições
- Proporção de **cavalo de guerra** (nunca lhama ou girafa).
- A barda tem borda recortada e filete de prata visíveis.
- A chama lê como **fogo**, nunca como "gema facetada".
- **Proibido:**
  - tubos retos nas pernas;
  - placas lisas sem recorte;
  - ferro chapado sem desgaste.

---

## 2. Banshee — Legendary · gait `fly`
### A. Conceito
Um **espectro lamentoso**: uma **mortalha de tecido rasgado endurecido**, com capuz em arco ogival, **máscara de crânio de osso alongada com a boca escancarada no grito** e mãos esqueléticas erguidas. No peito, uma **gaiola-relicário** de ferro prende uma alma. Da cintura para baixo, a mortalha se dissolve em **lâminas de ectoplasma**. É o oposto do cavalo: **sem peso, vertical, etérea**.
Pose: flutuando, inclinada à frente, braços meio erguidos com os dedos abertos (lamento).
Personalidade: trágica.

### B. Silhueta e proporções
- Altura **5,2** (base a 0,8), largura ~3,4 com os braços.
- **3 formas-chave:**
  1. **capuz alto em arco pontudo** com a coroa de espinhos;
  2. **sino da mortalha** abrindo para baixo (largura 2,6 na barra);
  3. braços longos e finos com mangas rasgadas pendentes.
- **Proporções:**
  - ombros mais estreitos que o capuz;
  - máscara com 0,7 de altura (oval vertical);
  - braços com 1,8 de comprimento;
  - mãos com dedos de 0,4.

### C. Anatomia e construção
- **Núcleo:** torso esquelético fino (costelas, coluna) + braços de osso. A mortalha cobre quase tudo.
- **Capuz:** 5–6 lâminas de tecido rígido com **dobras marcadas** (vincos com aresta), **abertura facial em arco ogival** e borda rasgada caindo sobre a testa. A **coroa de ferro com 7 espinhos** fica assentada sobre o capuz.
- **Máscara:**
  - crânio alongado, com testa, **maçãs salientes**, queixo fino e fissuras;
  - **órbitas grandes e fundas**;
  - **boca em fenda vertical bem aberta** (o grito), com a mandíbula descida;
  - osso com rachaduras e AO forte.
- **Mortalha:** 3 camadas de lâminas (curta nos ombros, média até a cintura, longa até a barra), cada lâmina afunilando com a **ponta rasgada em tiras**, comprimentos desiguais e borda prata gasta.
- **Mangas:** largas, pendentes e rasgadas, abrindo do cotovelo.
- **Mãos:** de osso, com 4 dedos longos (falanges marcadas) e unhas pretas.
- **Gaiola-relicário:** no peito, com 6 barras góticas curvas, topo em ogiva e base com 4 pés; a alma fica dentro.
- **Correntes:** algemas de ferro nos punhos, com **5 elos** pendentes cada (rígidos no osso).

### D. Materiais

| Material | Hex | Rough | Metal | Onde |
|---|---|---|---|---|
| tecido-roxo | 3B1F4F, borda 5A3A72, prata gasta | 0,85 | 0 | mortalha, capuz |
| osso | D9CFB4 + AO 8A7A5A | 0,6 | 0 | máscara, mãos |
| ferro escuro | 3A3842 | 0,45 | 0,85 | coroa, gaiola, correntes |
| prata-velha | 9A9AA6 | 0,3 | 0,95 | filetes da gaiola, borda da coroa |

### E. Glow e Spirit
- **Foco 1:** as **órbitas**, com Glow verde intenso, e um brilho fraco dentro da boca.
- **Foco 2:** a **alma na gaiola**: orbe verde-branco com um rosto vago pintado.
- **Secundário:** a joia da coroa (roxa) e as algemas (fio fino).
- **Spirit:** lâminas de ectoplasma da cintura para baixo (Transparency 0,45), afunilando em pontas finas, verde-azuladas.

### F. Marcas de identidade
- A máscara tem uma **rachadura grande** atravessando o olho esquerdo.
- Uma das correntes está **partida** (só 3 elos).

### G. Rig e FX
- **Ossos:**
  - root, body1, body2, chest, neck, head, jaw, hood1, hood2;
  - shroud_F1–2, shroud_B1–2, shroud_L1–2, shroud_R1–2;
  - por lado: upperarm, forearm, hand, fingers, chain1–2;
  - spirit1–2.
- **Âncoras:**
  - `mouth` (jaw);
  - `soul` (chest);
  - `hand_L` e `hand_R`;
  - `hem` (spirit2).

### H. VFX
- **Ambiente:**
  - **exclusivo** `ecto_trail`: `vfx_ecto_wisp_4x4` saindo da barra (`hem`), a 2/s (low 1), descendo e se desfazendo;
  - `core_pulse` verde na alma (pulso lento, 2,2 s);
  - **exclusivo** `soul_flicker`: a alma "bate" na gaiola, com um pequeno flash a cada 5 s;
  - orçamento normal: 4 emissores e 1 luz (alma).
- **Ação "Wail"** (grito):
  - antecipação 0,5 s: recua e a boca fecha;
  - impacto em 0,06 s: a boca escancara e saem **3 anéis de som** (`vfx_sound_ring`) expandindo à frente em sequência (0, 0,12, 0,24 s), com distorção; os olhos piscam forte;
  - dissipação 1,4 s: fiapos de ectoplasma saem em espiral;
  - low: 1 anel + fiapos.

### I. Animações

| Clipe | Duração | Loop | Notas |
|---|---|---|---|
| Idle | 4,0 s | sim | flutua subindo e descendo 0,2; as lâminas da mortalha ondulam com atraso; as correntes balançam |
| Fly | 2,0 s | sim | desliza à frente com a mortalha esticando para trás |
| Happy | 2,5 s | não | gira, rindo (a cabeça inclina para trás) |
| Wail | 2,4 s | não | marcador fx em 0,5 s |

### J. Aceitação e proibições
- A máscara é **crânio oval**, nunca bloco retangular.
- O capuz tem abertura em ogiva, nunca "cápsula".
- O tronco tem forma de sino, nunca tubo.
- As mangas são largas e rasgadas, nunca braceletes tubulares.
- O grito é legível a 30 studs.
- **Proibido:**
  - pano mole/cloth sim;
  - rosto humano bonito;
  - corpo tubular.

---

## 3. LichKing — Mythic · gait `ground` (paira a 0,3)
### A. Conceito
O **rei necromante**: um esqueleto alto vestido com **armadura gótica de placas** (estilo Maximiliano, com fluting), capa de rei rasgada, coroa alta de ferro e prata e um **cajado com filactério** flutuante. **Runas arcanas** brilham no peitoral e no chão sob ele. É a peça mais imponente da área, **vertical e simétrica, régia**, contra o cavalo horizontal e a banshee etérea.
Pose: ereto e majestoso; mão direita no cajado, **mão esquerda aberta em gesto de feitiço** com energia roxa.
Personalidade: frio e soberano.

### B. Silhueta e proporções
- Altura **6,6** (topo da coroa), largura **≤ 4,6** (ombreiras), profundidade ~2,2 com a capa.
- **3 formas-chave:**
  1. **coroa alta de 7 pontas** sobre o crânio;
  2. **ombreiras góticas enormes** com caveira;
  3. cajado alto, passando acima da coroa, com o filactério.
- **Proporções:**
  - tórax em V (armadura com cintura);
  - **crânio 12% maior que na v1** (0,75);
  - mãos de osso grandes (palma 0,45);
  - pernas longas com grevas.

### C. Anatomia e construção
- **Núcleo:** esqueleto humano alto (costelas, coluna, pelve, ossos longos com epífises), visível nas juntas: cotovelo, joelho e cintura.
- **Armadura** (derivada da superfície, R10):
  - **peitoral** com cintura: largo no peito e afunilando, com **fluting em V**, filete de prata elevado na borda e **runa central** (Glow);
  - **fauld/tassets:** 4 lâminas sobrepostas que afunilam, de borda recortada;
  - **ombreiras:** 3 camadas recortadas em borda de lóbulos, **caveira em relevo** e 3 espinhos curvos para cima em cada uma;
  - **couters e poleyns** (cotovelo e joelho): **placa frontal em ponta ogival** com **asa lateral recortada**;
  - **vambraces e grevas:** placas frontais com fluting (nunca tubos completos), com o osso visível atrás;
  - **sabatons:** 4 lâminas segmentadas, com ponta afinada.
- **Gola alta:** de ferro, em **leque recortado** atrás do crânio.
- **Crânio:**
  - arcada pesada e maçãs salientes;
  - **mandíbula separada** com dentes individuais;
  - órbitas fundas com **chamas Glow verdes visíveis**;
  - rachadura na têmpora.
- **Coroa:** de ferro e prata, com **7 pontas góticas** de alturas alternadas, **joia roxa** central (Mythic) e filigrana.
- **Capa:** 6 lâminas largas de tecido rígido, roxo-escuro com borda prata, rasgadas em tiras na barra; mais larga atrás (2,6).
- **Mãos:** de osso, grandes, com falanges marcadas e **anéis com joias** (3 na esquerda). A direita segura o cajado; a esquerda fica aberta.
- **Cajado:**
  - haste de ferro **retorcida** (torção helicoidal), de 6,8;
  - topo com **crânio pequeno** e 3 garras segurando o **filactério**, um cristal roxo facetado flutuando 0,15 acima das garras.
- **Névoa:** baixa e larga sob os pés (Spirit), em **lâminas onduladas quase horizontais, irregulares** (nunca pétalas radiais).

### D. Materiais

| Material | Hex | Rough | Metal | Onde |
|---|---|---|---|---|
| ferro escuro | 3A3842, arestas 6A6878 | 0,4 | 0,9 | armadura |
| preto-ferro | 1A1820 | 0,5 | 0,85 | fundo das nervuras |
| prata-velha | 9A9AA6 | 0,25 | 0,95 | filetes, coroa, caveiras |
| osso | D9CFB4 + AO | 0,6 | 0 | esqueleto |
| tecido-roxo | 3B1F4F | 0,85 | 0 | capa |
| joia | C98BFF | 0,05 | 0 | coroa, anéis |

### E. Glow e Spirit
- **Foco 1:** o **filactério** (roxo C98BFF intenso).
- **Foco 2:** as **chamas das órbitas** (verde 7CFFB0).
- **Secundário:**
  - a runa do peitoral (verde);
  - a joia da coroa;
  - o brilho na palma esquerda (roxo).
- **Spirit:** a névoa da base (Transparency 0,55), verde-acinzentada.

### F. Marcas de identidade
- **Uma ponta da coroa quebrada**, a 2ª à direita.
- A ombreira esquerda tem **um corte de espada** (entalhe com borda brilhante de metal exposto).

### G. Rig e FX
- **Ossos:**
  - padrão bípede do MechaTitan + jaw, crown;
  - cape_L1–2, cape_C1–2, cape_R1–2;
  - staff, phylactery (filho de staff, com offset).
- **Âncoras:**
  - `eyes` (head);
  - `phylactery`;
  - `core` (chest, runa);
  - `crown`;
  - `hand_L`;
  - `ground` (root, no chão, para o círculo de runas).

### H. VFX
- **Ambiente:**
  - **exclusivo** `rune_circle`: em `ground`, um círculo de runas no chão (`vfx_rune_circle`) como partícula plana deitada (VelocityPerpendicular, vide o contrato do preset), raio 2,2, girando a 0,05 volta/s, verde translúcido. No low fica estático e com menos brilho;
  - `fog`: `vfx_fog_4x4` rolando baixo em 3 pontos;
  - `orbit_ring` pequeno roxo em volta do filactério (raio 0,35);
  - `aura` roxa na mão esquerda (fiapos subindo);
  - orçamento normal: 7 emissores, 8 beams e 1 luz (filactério).
- **Ação "Cast":**
  - antecipação 0,6 s: ergue o cajado, as runas do círculo acendem em sequência e partículas são sugadas para o filactério;
  - impacto em 0,08 s: **flash roxo** + `fx_halo_soft` expandindo do filactério + 12 `vfx_rune_glyph` disparados em espiral para cima;
  - dissipação 1,6 s: as runas apagam uma a uma e a névoa se espalha;
  - low: halo + 6 runas.

### I. Animações

| Clipe | Duração | Loop | Notas |
|---|---|---|---|
| Idle | 4,0 s | sim | paira subindo e descendo 0,1; a capa ondula; a mão esquerda gira lentamente com a energia; a cabeça vira devagar |
| Walk | 2,2 s | sim | **desliza** (passos curtos que não tocam o chão) com a capa arrastando |
| Happy | 2,5 s | não | ergue o cajado e ri (a mandíbula bate) |
| Cast | 2,6 s | não | marcador fx em 0,6 s |

### J. Aceitação e proibições
- A armadura é gótica, com recorte, ogiva e fluting visíveis, nunca "balde".
- Crânio e chamas das órbitas legíveis a 30 studs.
- A névoa é baixa e irregular, nunca flor ou pétalas.
- Altura ≤ 6,6.
- **Proibido:**
  - cilindros completos nas pernas e nos braços;
  - coroa com pontas iguais e lisas;
  - mãos pequenas.
