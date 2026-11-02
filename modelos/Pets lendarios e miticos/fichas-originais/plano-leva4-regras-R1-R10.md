# Plano mestre — Leva4: Legendary/Mythic das áreas 4–7 (12 pets)

Autor: opus-climb. Data: 2026-10-21. Status: **PLANO, aguardando aprovação do usuário**. Nada disparado.

Fichas por área, com 3 pets cada:
- `2026-10-21_ficha-L4-Volcano.md`
- `2026-10-21_ficha-L4-CoralReef.md`
- `2026-10-21_ficha-L4-CandyLand.md`
- `2026-10-21_ficha-L4-Haunted.md`

## 0. Pedido e decisões
- **Usuário:** os 12 L/M das áreas 4–7, no **mesmo nível de acabamento do MechaTitan v3**, com comparação lado a lado com ele. Cada pet tem **estilo e efeitos próprios**, com especificação extensa e individual.
- A rodada 1 (2026-10-21, 4 bots em paralelo, ~1 h por área) foi **reprovada por mim antes de chegar ao usuário**. As criaturas viraram "robôs de blocos": caixas e anéis arredondados empilhados num esqueleto. A v1 fica em `opus-blender/.../leva4-skin/areas4-7/<Área>/<Pet>/` como referência do que NÃO fazer. As correções da rodada 1 foram interrompidas.
- Nesta etapa o opus-blender só gera arquivos. Integração no Studio fica comigo depois, com o runtime skinado do MechaTitan v3 (ainda pendente).

## 1. Por que o MechaTitan v3 funciona (regras de qualidade, R1–R10)
Analisei hero, turntable e closes do v3 (`piloto/MechaTitan_v3/review_model/final/`). O que dá a sensação de "acabado":

| # | Regra | Como aparece no v3 | Como traduzir para criatura |
|---|---|---|---|
| R1 | **Hierarquia de formas** grande → média → pequena | ombreiras e peitoral em V (grandes), cascas dos membros (médias), dedos, grelhas e parafusos (pequenas) | 2–3 massas dominantes (tórax, ombro/asa, cabeça), placas médias nos membros, detalhe pequeno nas pontas e bordas |
| R2 | **Placa dentro de placa** | toda chapa tem moldura chanfrada + painel interno rebaixado ou elevado | toda escama, placa ou pena tem **borda chanfrada + campo interno** (crista, nervura, rebaixo ou textura de material) |
| R3 | **3 valores de material com contraste claro** | aço claro / grafite escuro / navy de friso | cada pet tem **claro / médio / escuro** bem separados (tabela de materiais na ficha) + 1 cor de acento |
| R4 | **No máximo 2 focos luminosos primários** | visor + núcleo; o resto do neon são frestas finas | cada pet tem **2 focos de Glow** definidos e o resto do Glow é linha fina secundária. Nada de Glow espalhado por tudo |
| R5 | **Marcas de identidade assimétricas** | "07" numa ombreira, faixa de aviso na outra | cada pet tem 1–2 marcas que contam história (cicatriz, mordida, runa, coroa torta, craca de um lado só) |
| R6 | **Chanfro vivo e consistente** | arestas duras, chanfro 0,03–0,05, highlight na aresta | igual: nada de bevel redondo grande ("inflado") nem aresta crua sem chanfro |
| R7 | **Pintura limpa** | cor sólida por chapa, gradiente suave, highlight de aresta, AO nas frestas, desgaste só nas bordas | igual, com o desgaste do material (lasca de rocha, glacê rachado, nácar gasto, ferrugem) **só nas bordas expostas** |
| R8 | **Profundidade real** | tórax com ~1,9 de profundidade, peças sobrepostas em 2–3 camadas | nenhuma vista lateral "tábua": as camadas sobrepostas criam sombra própria |
| R9 | **Silhueta legível a 30 studs** | ombros largos, cabeça marcante, pés largos | a ficha define as **3 formas-chave** que precisam ler de longe |
| R10 | **Forma segue a função** | robô = caixas articuladas, por isso funciona | criatura = **anatomia primeiro** (massa muscular, afunilamento, curva); placas DERIVADAS da superfície |

**Causa da falha da rodada 1:** aplicaram ao corpo orgânico o método do robô (tubo de raio constante + caixas em volta). As regras R1–R9 estavam no briefing, mas sem R10 o resultado vira máquina. **R10 é obrigatória.**

### Método de construção obrigatório (R10 em detalhe)
1. **Núcleo anatômico:** loft com perfis diferentes por anel (oval, gota, D), raio variável, massa onde tem músculo (peito, ombro, coxa, antebraço) e afunilamento nas extremidades. Nenhum membro com raio quase constante.
2. **Placas derivadas da superfície:** selecione a região de faces do núcleo → duplique → offset na normal → solidify com espessura **afunilando para a borda** → recorte o contorno (escama, lâmina, fragmento) → chanfro 0,03–0,05.
3. **Sobreposição em fileiras** (telha): cada peça cobre 25–35% da próxima, na direção do fluxo (da cabeça para a cauda, do ombro para a mão).
4. **Variação controlada:** tamanho e rotação com ±8–15% de aleatoriedade (seed fixa). Nada de fileira de peças idênticas.
5. **Proibido em todo pet não robótico:**
   - anel ou cilindro completo em volta do membro;
   - parafuso ou rebite;
   - tira de LED reta;
   - bocal, visor ou painel com chanfro de máquina;
   - grade retangular.

## 2. Pipeline em 3 portões, com aprovação do usuário em cada um
O usuário aprova em etapas. Na rodada 1 o defeito estava na anatomia e só apareceu depois de 1 h de detalhe e textura, então o pipeline ganha um portão barato no início.

| Portão | O que o bot entrega | Duração estimada | Quem aprova |
|---|---|---|---|
| **A — Blockout** | núcleo anatômico + massas principais + placas grandes, **em cinza, sem textura**, com rig básico só para posar. 4 vistas + silhueta + 3/4 + **lineup com o MechaTitan v3** na mesma escala | ~15–25 min por pet | eu filtro e o usuário aprova a silhueta e a proporção |
| **B — Modelo final** | detalhe completo, high-poly, bake, pintura 2048, Glow/Spirit, rig com pesos, âncoras FX. Hero, turntable, closes e **compare_MT3** (mesma câmera, luz e escala que o MechaTitan v3) | ~40–60 min por pet | eu filtro e o usuário aprova |
| **C — Animação + texturas de VFX** | clipes da ficha, verify (loop, deslize do pé, erro), export FBX/GLB/clips.json/manifest e PNGs/flipbooks de VFX próprios | ~40–60 min por pet | eu filtro e o usuário aprova; depois eu integro no Studio |

Paralelismo: 4 bots, um por área, cada um fazendo os 3 pets **em sequência** e reaproveitando o kit da área. Nenhum usa `Blender_MCP` (o Blender aberto é do usuário): só `blender -b -P`.

**Revisão (regra do usuário, 2026-10-21):** **toda entrega é mostrada ao usuário assim que chega, mesmo que eu ache ruim**, junto com a minha avaliação contra o MechaTitan v3 e a ficha. **Nenhuma correção é disparada antes de o usuário ver e concordar.**

## 3. Regras técnicas comuns (todas as fichas)
- **Topologia:**
  - 1 objeto skinado `<Pet>_Body`: núcleo manifold com 1 ilha + placas como ilhas do MESMO objeto, com peso rígido 100% no osso dono;
  - `<Pet>_Glow` (Neon), ≤ 3.000 tris;
  - `<Pet>_Spirit` (translúcido, Transparency no manifesto), ≤ 3.000 tris, só quando a ficha pede.
- **Limites:** corpo ≤ 18.000 tris; ≤ 4 influências por vértice; sem faces degeneradas; 0 non-manifold no núcleo.
- **Texturas:** 2048² Color/Normal (OpenGL)/Roughness/Metalness, padding 16, **cobertura de UV ≥ 55%**, ilhas maiores nas placas-herói (definidas na ficha).
- **Unidades:** 1 unidade = 1 stud, Z para cima, frente +Y, pivô no chão (Z=0) no centro XZ. Voadores e nadadores têm o pivô no chão e o corpo na altura de flutuação da ficha.
- **Escala no jogo:** o runtime multiplica Legendary ×1,6 e Mythic ×2 (`Config.RaritySizeScale`), além do peso. As alturas das fichas são **base**: não compensar.
- **Review:** EEVEE, 16 samples, 768 px (hero 1024), **mesma luz e câmera do `mt3_review2.py`**, para o compare com o MechaTitan ser justo.
- **Shell:** nunca `python -c`, `--python-expr`, `rm -r`, `find -delete` ou `execute_code`. Gravar `.py` e rodar `blender -b -P`.
- **Velocidade:**
  - executar a ficha, sem reprojetar;
  - código em blocos ≤ 150 linhas, `patch` em vez de reescrever;
  - 1 render de autoavaliação + 1 final por portão.
- **Pasta:** `opus-blender/outputs/verification/projetos/leva4-skin/areas4-7-r2/<Área>/<Pet>/` (pasta nova; a v1 fica intocada).

## 4. Sistema de VFX (comum)
**Base existente no jogo** (2026-10-18):
- `Client.PetFX` monta efeitos nas partes `FX_<nome>` de cada pet, a partir de `Shared.PetFXPresets`, que é gerado do `vfx_pet_presets.json` da leva3-vfx.
- Presets prontos: `ring_glow`, `halo_glow`, `orbit_ring`, `core_pulse`, `aura`, `sparkle` e `trail`.
- Texturas enviadas: beam_glow, beam_energy, ring_soft, halo_soft, glow_soft, star4, trail_strip e os flipbooks sparkle, core_pulse e aura_wisp.
- Regras de orçamento: low automático com mais de 12 pets com FX; PointLight só nos 4 mais próximos; nada além de 120 studs; escala de raridade L 1,25 / M 1,5.

**O que esta leva acrescenta:**
1. **Camada ambiente (sempre ligada no plot):** a assinatura visual de cada pet. A maioria **reusa os presets existentes com cor e parâmetros próprios**, e cada pet tem pelo menos 1 elemento exclusivo (textura ou preset novo) listado na ficha.
2. **Camada de ação (só durante o clipe especial):** disparada pelo cliente por marcador de tempo no clipe (`fxEvents` no clips.json: `{t, anchor, burst}`). Segue a VFX_POLICY: antecipação → impacto de 0,05–0,1 s → dissipação. Low = metade.
3. **Texturas novas de VFX**, feitas pelo opus-blender no portão C:
   - PNG RGBA, flipbooks 4×4 ou 8×8, sem texto;
   - testadas em fundo claro e escuro;
   - uma lista por área na ficha, compartilhada pelos 3 pets da área.
4. **Orçamento por pet** (normal / low):
   - Legendary ≤ 6 emissores, ≤ 10 beams, ≤ 1 luz / ≤ 3 emissores, ≤ 6 beams, 0 luz;
   - Mythic ≤ 8 emissores, ≤ 12 beams, ≤ 1 luz / ≤ 4 emissores, ≤ 6 beams, 0 luz.

   Partículas vivas em média: ≤ 12 (L) e ≤ 16 (M) no normal.
5. **Cor:** a do tema do pet (ficha). O acento de raridade entra só num detalhe pequeno: dourado Legendary 255,200,40 e rosa Mythic 255,80,200, conforme `Config.RarityColors` do histórico, **a confirmar no Studio ao vivo**.
6. Nada de VFX servidor. Nada de Bloom/ColorCorrection permanente. A animação de chocar ovo **não** se mexe (decisão do usuário, 2026-10-15).

## 5. Diferenciação (cada pet com estilo próprio)
Dentro da mesma área, os 3 pets têm **estilo de construção, silhueta, gait, focos e VFX diferentes**, para não parecerem um kit trocado de cor:

| Área | Pet | Estilo de construção (palavra-chave) | Silhueta | Gait | Focos Glow | VFX exclusivo |
|---|---|---|---|---|---|---|
| Volcano | VolcanicPhoenix | **vitral de obsidiana com brasas** (lâminas finas, elegante) | V aberto das asas | fly | coração-brasa no peito + olhos | rastro de brasas e plumas incandescentes caindo |
| Volcano | LavaTitan | **basalto colunar tectônico** (colunas hexagonais, crosta rachada) | gorila: trapézio gigante, braços até o chão | ground | núcleo-fornalha + boca da cratera nas costas | fumaça da cratera + gotas de magma pingando dos punhos |
| Volcano | MoltenDragon | **obsidiana polida imperial com filigrana de ouro** | dragão alongado, pescoço em S, chifres de coroa | ground | fornalha da garganta + coroa | aura de calor (brasas subindo) + baforada de fumaça pelas narinas |
| CoralReef | PearlSeahorse | **joia art nouveau de nácar e ouro** | S vertical delicado | swim | pérola do peito + coronet | bolhas iridescentes + brilho de pérola pulsando |
| CoralReef | Kraken | **carapaça abissal com cracas e coral** (rústica, pesada) | cúpula + 8 curvas | swim | 2 olhos + manchas fotóforas | motas bioluminescentes + nuvem de tinta na ação |
| CoralReef | Leviathan | **serpente real das profundezas, escamas de pérola negra** | espiral régia | swim | linha lateral de fotóforos + coroa de pérolas | anel de água girando + espiral de bolhas |
| CandyLand | GingerbreadGolem | **biscoito artesanal decorado com glacê real** (espesso, crocante) | golem de ombros altos | ground | olhos de bala + lareira no peito | migalhas caindo + fumaça rosa da chaminé |
| CandyLand | SugarPhoenix | **vidro de açúcar / bala dura** (translúcido, facetado) | ave de V alto | fly | coração de caramelo + pontas das asas | cristais de açúcar cintilando + rastro de bala |
| CandyLand | SprinkleDragon | **confeitaria de luxo: chocolate temperado, glacê, bengala** | dragão robusto e baixo | ground | coroa de cristal + garganta | chuva de confeitos + gota de glacê escorrendo |
| Haunted | HeadlessHorse | **barda gótica de cavaleiro** (ferro forjado e prata) | cavalo de guerra sem cabeça | ground | chama do pescoço + cascos | chama espectral verde (flipbook) + brasas dos cascos |
| Haunted | Banshee | **espectro de mortalha rasgada e máscara de osso** | sino flutuante com capuz | fly | órbitas + alma na gaiola | fiapos de ectoplasma + anéis de som no grito |
| Haunted | LichKing | **rei necromante: placas góticas + osso + runas** | vertical régio com cajado | ground | filactério + órbitas | círculo de runas girando no chão + névoa |

## 6. Dependências e riscos
- **Runtime skinado:** o MechaTitan v3 ainda não está no Studio. Ele precisa ser importado (o usuário importa o FBX) e o runtime de Bone.Transform no cliente precisa ser escrito e testado, antes de integrar qualquer pet desta leva. Os portões A e B não dependem disso; o C só depende para a integração.
- **Tempo:**
  - portões A, B e C ≈ 0,5 + 2,5 + 2,5 h por área, com as 4 áreas em paralelo;
  - mais o tempo de revisão minha e do usuário entre os portões;
  - a rodada 1 levou ~1 h por área sem os portões.
- **Risco principal:** o bot voltar ao método caixa-em-esqueleto. Mitigação: R10 obrigatória, portão A barato e compare_MT3 em todo portão.
- **Riscos de tema** (o tema puxa para um defeito conhecido): doce → inflado; coral → máquina; fantasma → pano mole. Cada ficha tem proibições específicas.

## 7. Critérios de aceitação gerais (checados por mim antes do usuário)
1. **Silhueta:** as 3 formas-chave da ficha legíveis a 30 studs (a silhueta preta confirma).
2. **Anatomia (R10):** nenhum membro de raio constante, nenhum anel em volta de membro e as placas seguem a curva.
3. **Acabamento:** R2, R3, R6 e R7 visíveis no close a 1 stud, no mesmo nível do `texture_closeup` do MT3.
4. **Focos:** exatamente os 2 focos Glow primários da ficha dominam; o resto é secundário.
5. **Marca de identidade** (R5) presente.
6. **Técnica:** números dentro dos limites; stats.json completo; compare_MT3 gerado.
7. **Proibições** da ficha respeitadas.
