---
area: modelos
tipo: indice
resumo: Índice e regras comuns do remake dos 21 pets Lendários e Míticos das áreas 4–10 do +1 Climb for Pets, com uma ficha de remake por pet e as referências 2D e 3D de cada um.
termos: remake pets lendarios miticos legendary mythic climb for pets volcano coralreef candyland haunted skykingdom cybercity cosmos ficha alvo 2d render
---
# Remake dos pets Lendários e Míticos (áreas 4–10)

> **Atualizado em 31/10/2026:** a meta visual agora é o nível dos pets do Steal An Egg, ver [[Regua Steal An Egg para os 21 pets]]. Alvo 2D, MechaTitan v3, R1–R10 e as decisões visuais em aberto abaixo **não valem mais** como régua; esta nota fica para nome, espécie, área, raridade, técnica e clipes.

Escrito em 30/10/2026 a pedido do luks: "descrição detalhada de cada pet mítico e lendário", para depois refazer cada um numa thread separada. Cada pet tem a sua nota nesta pasta; esta nota reúne o que vale para todos.

**Fora do escopo:** os 9 pets de Meadow, Glacier e Crystal (Lotus Koi, Spirit Deer, Ice Wolf, Frost Mammoth, Diamond Cat, Diamond Stag, Bismuth Lizard, Rainbow Tortoise, Kyawthuite Fox) ficam como estão no Studio.

## De onde veio cada informação

| Fonte | Onde está | Uso |
| --- | --- | --- |
| Fichas L4 por área (forma, paleta, rig, clipes, VFX) | `fichas-originais/ficha-L4-<Área>.md` (cópia do `claude-project-context.zip`) | detalhe de construção; as notas de remake resumem e corrigem |
| Regras R1–R10 do estilo MechaTitan v3 | `fichas-originais/plano-leva4-regras-R1-R10.md` | método de modelagem obrigatório |
| Ícones-alvo 2D (Astra) | `Recursos/Pets lendarios e miticos/<Pet>_alvo-2d.webp` (originais 1024² em `referencias-pets-lendarios-miticos/alvos-2d/` na pasta do projeto) | **o visual que o remake deve atingir** |
| Render atual do Blender (portão C) | `Recursos/Pets lendarios e miticos/<Pet>_render-atual.webp` (originais em `renders-3d/`) | o que existe hoje e o que corrigir |
| Molten Dragon v2 | `Recursos/Pets lendarios e miticos/MoltenDragon_conceito-v2.webp` (original em `pets-v2/`) | conceito alternativo, ver a nota do pet |
| Estado e direção de arte | `00_INSTRUCOES_DO_PROJETO.md` e `01_ESTADO_ATUAL.md` do zip | regras de olhos, contraste e proibições |

As imagens no repositório são cópias reduzidas (640 px) só para consulta rápida. Para gerar ou comparar, use os originais da pasta do projeto.

## Diagnóstico geral: por que refazer

Comparei lado a lado o alvo 2D e o render atual de cada pet. Os problemas se repetem:

1. **Valor escuro demais.** Vários renders leem como mancha escura (Kraken, Molten Dragon, Banshee, Headless Horse, Lich King). O alvo 2D é sempre mais claro e saturado.
2. **Glow tímido.** Fendas de magma, ventosas, chamas e cristais brilham muito menos que no alvo. O alvo usa 2 focos fortes e filetes; o render apaga os dois.
3. **Membros e pescoços finos.** Fênix, Sugar Phoenix, Headless Horse, Lich King e Molten Dragon ficaram com pernas de palito ou pescoço de girafa. O alvo é mais robusto e "chunky".
4. **Silhueta perdida em elementos-chave.** Asas do Molten Dragon fechadas, cauda de chamas da Volcanic Phoenix rala, ectoplasma da Banshee pequeno, capa do Lich King estreita.
5. **Cor do tema desviada.** Kraken azul-marinho em vez de roxo-magenta; Banshee roxa em vez de cinza-turquesa; Sprinkle Dragon rosa manchado em vez de chocolate com glacê.

**Regra do remake:** o **alvo 2D é a meta visual** (cor, proporção, pose, o que brilha). A ficha original continua valendo para construção, rig, clipes e VFX, **exceto onde a nota do pet diz que o alvo 2D manda**. Quando os dois divergem e a escolha muda o pet, a nota marca como "decisão em aberto".

## Estilo comum (vale para os 21)

- **Cartoon Roblox de placas grossas facetadas**, no nível do MechaTitan v3 (`MechaTitan_referencia.webp`): hierarquia grande → média → pequena, placa dentro de placa (moldura chanfrada + miolo), chanfro vivo 0,03–0,05, profundidade real em camadas.
- **Anatomia primeiro (R10)** nos pets orgânicos: núcleo com músculo e afunilamento, placas derivadas da superfície e sobrepostas 25–35% no sentido do fluxo. Nada de tubo de raio constante, anel em volta do membro, parafuso ou LED reto fora da CyberCity.
- **3 tons + destaque:** cada pet tem claro, médio e escuro bem separados e um destaque (Glow ou metal). Nenhum material principal abaixo de `3A3A44` em valor; roughness ≥ 0,25 nos principais. Nada de preto sobre preto, nada de vinil brilhante.
- **Legível a 64–128 px:** testar o ícone de inventário em 64 e 128 px, fundo claro e escuro. A silhueta e os 2 focos de Glow precisam sobreviver. Se um detalhe some em 64 px, ele é secundário.
- **Olhos legíveis a 128 px** em todo pet que tem olhos. Sem olhos de propósito: Headless Horse (sem cabeça), AI Overlord (cérebro) e Quantum Cat (visor).
- **Máximo 2 focos de Glow primários**; o resto é filete fino. Glow em no máximo ~25% da superfície.
- **Marcas de identidade assimétricas (R5):** 1–2 por pet, contam história (cicatriz, peça quebrada, remendo).
- **Anti-padrões proibidos:** argila com adesivos, papel-alumínio amassado, cabeça grudada, membros em tubo, fileiras de peças idênticas, brinquedo inflado.

## Efeitos por raridade

| | Legendary | Mythic |
| --- | --- | --- |
| Escala no jogo (`Config.RaritySizeScale`) | ×1,6 | ×2,0 |
| Acento de raridade (só num detalhe pequeno) | dourado `FFC828` (255,200,40) | rosa `FF50C8` (255,80,200) |
| Orçamento de VFX normal | ≤ 6 emissores, ≤ 10 beams, ≤ 1 luz | ≤ 8 emissores, ≤ 12 beams, ≤ 1 luz |
| Orçamento low | ≤ 3 emissores, ≤ 6 beams, 0 luz | ≤ 4 emissores, ≤ 6 beams, 0 luz |
| Partículas vivas (normal) | ≤ 12 | ≤ 16 |
| Elemento de prestígio | 1 efeito ambiente exclusivo | coroa ou peça régia + 1 efeito ambiente exclusivo + efeito de chão ou órbita |

Cada pet tem **camada ambiente** (sempre ligada no plot, reaproveitando os presets `ring_glow`, `halo_glow`, `orbit_ring`, `core_pulse`, `aura`, `sparkle`, `trail`) e **camada de ação** (só no clipe especial: antecipação → impacto de 0,05–0,1 s → dissipação). Sem VFX no servidor, sem Bloom permanente. A animação de chocar ovo não muda.

## Técnica comum (resumo da ficha)

- Objetos: `<Pet>_Body` (skinado, ≤ 18.000 tris), `<Pet>_Glow` (Neon, ≤ 3.000), `<Pet>_Spirit` (translúcido, ≤ 3.000, só quando pedido).
- ≤ 4 influências por osso; texturas 2048² Color/Normal/Roughness/Metalness, cobertura de UV ≥ 55%.
- 1 unidade = 1 stud, Z para cima, frente +Y, pivô no chão. Alturas das notas são **base** (o jogo aplica a escala de raridade).
- Clipes mínimos: Idle, Walk/Fly/Swim, Happy e 1 especial, em loop sem salto; âncoras `FX_*` para os efeitos.
- Portões: A (blockout cinza + silhueta + lineup com o MechaTitan) → B (modelo final e pintura, com compare_MT3) → C (animação, VFX e export). Mostrar ao luks em cada portão.

## Os 21 pets

| Área | Pet | Raridade | Nota | Situação do alvo 2D |
| --- | --- | --- | --- | --- |
| Volcano | Volcanic Phoenix | Legendary | [[Volcanic Phoenix]] | ✅ |
| Volcano | Lava Titan | Legendary | [[Lava Titan]] | ✅ (visual travado pelo luks) |
| Volcano | Molten Dragon | Mythic | [[Molten Dragon]] | ✅ + conceito v2 |
| CoralReef | Pearl Seahorse | Legendary | [[Pearl Seahorse]] | ✅ |
| CoralReef | Kraken | Legendary | [[Kraken]] | ✅ |
| CoralReef | Leviathan | Mythic | [[Leviathan]] | ✅ |
| CandyLand | Gingerbread Golem | Legendary | [[Gingerbread Golem]] | ✅ |
| CandyLand | Sugar Unicorn / Sugar Phoenix | Legendary | [[Sugar Unicorn ou Sugar Phoenix]] | ✅ como Phoenix; nome em aberto |
| CandyLand | Sprinkle Dragon | Mythic | [[Sprinkle Dragon]] | ✅ |
| Haunted | Headless Horse | Legendary | [[Headless Horse]] | ✅ |
| Haunted | Banshee | Legendary | [[Banshee]] | ✅ |
| Haunted | Lich King | Mythic | [[Lich King]] | ✅ |
| SkyKingdom | Sky Whale | Legendary | [[Sky Whale]] | ✅ |
| SkyKingdom | Seraph | Legendary | [[Seraph]] | ✅ |
| SkyKingdom | Sky Emperor | Mythic | [[Sky Emperor]] | ✅ |
| CyberCity | Quantum Cat | Legendary | [[Quantum Cat]] | ✅ |
| CyberCity | Mecha Titan | Legendary | [[Mecha Titan]] | ❌ falta o alvo 2D (prompt pronto) |
| CyberCity | AI Overlord | Mythic | [[AI Overlord]] | ✅ |
| Cosmos | Black Hole Cat | Legendary | [[Black Hole Cat]] | ✅ |
| Cosmos | Celestial Whale | Legendary | [[Celestial Whale]] | ✅ |
| Cosmos | Cosmic Deity | Mythic | [[Cosmic Deity]] | ✅ |

**Situação no jogo (23/10):** áreas 4–7 (Volcano a Haunted) ainda não têm ovos nem pets no `Config`, então Banshee, Headless Horse e Lich King ainda não existem no jogo. Áreas 8–10 usam versões antigas ("realistas" v2/v3) dos Lendários e Míticos. Nenhum modelo da Leva 4 foi importado no Studio.

## Decisões em aberto (resolver no portão A de cada thread)

| Pet | Escolha | Recomendação |
| --- | --- | --- |
| Molten Dragon | alvo 2D (asas abertas, obsidiana escura) ou conceito v2 (lilás claro, anéis de ouro, asas fechadas) | forma do alvo + valor e anéis do v2 |
| Sugar Unicorn / Sugar Phoenix | espécie e nome do Lendário da CandyLand | manter Sugar Phoenix (já existe Choco Unicorn Epic na área) |
| Pearl Seahorse | coroa de ouro com pérolas (alvo) ou de coral (ficha) | ouro com pérolas + 1 ramo de coral |
| Sky Emperor | coroa-sol (alvo) ou coroa-templo de colunas (ficha) | coroa-sol |
| Cosmic Deity | rosto sereno de olhos fechados (alvo) ou máscara lisa (ficha) | rosto de estátua simplificado |
| Black Hole Cat | olhos âmbar (alvo) ou ciano (ficha) | âmbar |

Mudanças de cor que **não** são decisão em aberto (o alvo 2D manda): Kraken passa de azul-abissal para roxo-magenta; Banshee passa de mortalha roxa para cinza-azulada com ectoplasma turquesa; Lich King ganha filetes dourados em vez de prata.

## Ordem sugerida para as threads de remake

1. **Molten Dragon e Kraken** (maior distância entre alvo e render, e o Molten Dragon tem decisão de conceito).
2. **Sprinkle Dragon, Banshee, Lich King, Headless Horse** (cor e proporção erradas).
3. **Volcanic Phoenix, Sugar Phoenix, Pearl Seahorse, Sky Emperor, Cosmic Deity** (ajustes de proporção, glow e decisões pontuais).
4. **Lava Titan, Leviathan, Gingerbread Golem, Sky Whale, Seraph, Quantum Cat, AI Overlord, Black Hole Cat, Celestial Whale** (render já perto do alvo: polimento de valor, glow e olhos).
5. **Mecha Titan:** gerar primeiro o alvo 2D; o 3D é a referência de qualidade e só recebe ajuste de cor para combinar com os alvos.

Relacionadas: [[Referencia visual para pets mais raros]] · [[Raridade visual sem excesso de brilho]] · [[Leitura do pet em miniatura]] · [[Contraste dos pets no cenario]] · [[Steal An Egg pets recentes]].
