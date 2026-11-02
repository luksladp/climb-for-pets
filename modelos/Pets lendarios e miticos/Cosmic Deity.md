---
area: modelos
tipo: ficha-de-remake
resumo: Remake da Cosmic Deity (Mythic, Cosmos) — divindade de 4 braços sentada em lótus, armadura dourada com joias violeta, manto de espaço estrelado, coroa-eclipse atrás da cabeça, planeta e estrela nas mãos e anéis orbitando.
termos: cosmic deity divindade cosmica cosmos mythic quatro bracos lotus eclipse coroa solar planeta estrela aneis manto galaxia remake
---
# Cosmic Deity

**Cosmos · Mythic · gait `fly` (paira a 0,4) · altura base 6,8 (topo da coroa) · largura 5,4**

![[Recursos/Pets lendarios e miticos/CosmicDeity_alvo-2d.webp|300]] ![[Recursos/Pets lendarios e miticos/CosmicDeity_render-atual.webp|300]]

## Em uma frase
A criadora de galáxias: figura serena de pele prateada-lilás, 4 braços (2 em mudra de meditação no peito, 2 erguidos segurando um planeta com anel e uma estrela), armadura dourada com joias violeta, manto de espaço estrelado azul-noite, sentada em lótus sobre uma flor-galáxia, com uma coroa-eclipse de raios dourados atrás da cabeça e anéis orbitando o corpo.

## O que mudar em relação ao render atual
- **Imponência:** o render está estreito e pálido. O alvo é **largo** (manto aberto dos 2 lados, braços em leque) e rico em ouro. Largura ≥ 5.
- **Manto** azul-noite estrelado com borda dourada e pendentes de losango, aberto como capa, como no alvo.
- **Base:** flor de lótus de lâminas lilás translúcidas sobre um disco de galáxia (o alvo mostra lótus, a ficha dizia só disco). Seguir o alvo.
- **Coroa-eclipse** grande e nítida: disco escuro de espaço com aro de raios dourados.
- **Anéis orbitais** prata e ouro cruzando o corpo, soltos.

## Decisão em aberto: rosto ou máscara
- Ficha: máscara de prata lisa com 3 pontos de luz, **sem rosto humano**.
- Alvo 2D: rosto sereno estilizado, **olhos fechados**, pele prateada, marca na testa.
- **Recomendo seguir o alvo** com rosto simplificado de estátua (sem boca detalhada, olhos fechados em arco, marca Glow na testa). Lê como divindade a 64 px e cumpre a regra de olhos legíveis (os olhos fechados + a marca da testa). Confirmar com o luks no portão A.

## Silhueta e proporções
- 3 formas-chave: **coroa-eclipse** (Ø 2,0) atrás da cabeça, **4 braços com planeta e estrela**, **anéis orbitais inclinados** + lótus embaixo.
- Torso largo (1,8 nos ombros), pernas cruzadas sob o manto, mãos grandes, cabeça pequena (0,6) em relação à coroa (escala divina).
- Pose: pairando em lótus, braços em leque, coroa no alto.

## Anatomia e construção
- Núcleo humanoide atlético sentado (R10).
- **Armadura:** peitoral dourado com joia violeta central e constelação em relevo, ombreiras em lua crescente de ouro em camadas, braceletes e manoplas com joias, cinto com fivela-planeta.
- **Manto:** 8 lâminas grandes de tecido rígido, fora azul-noite estrelado, forro violeta, borda dourada com losangos pendentes.
- **Cabeça:** rosto de estátua sereno (ou máscara, ver decisão), marca Glow na testa.
- **Coroa-eclipse:** disco Ø 1,2 com espaço/nebulosa, coroa de 16 raios dourados alternados, presa por haste.
- **Braços de cima:** planeta com anel (Ø 0,7) e estrela de 4 pontas (cristal Glow). **Braços do meio:** mãos juntas no peito.
- **Anéis:** 2 anéis de lâminas finas (prata e ouro), Ø 4,8 e 4,0, ±20°, girando opostos, com pequenas esferas.
- **Base:** lótus de lâminas Spirit lilás sobre disco de galáxia.

## Paleta (3 tons + destaque)
| Papel | Hex | Onde |
| --- | --- | --- |
| Claro | `D8D8EC` pele/porcelana prateada | pele, máscara |
| Médio | `2A3466` azul-noite estrelado | manto |
| Escuro | `4A2A8A` forro violeta / `161A40` sombra | forro, frestas |
| Metal | `E8C25A` ouro-estelar | armadura, coroa, anéis |
| Destaque (Glow) | `FFF2C8` estrela e coroa; `B88CFF` joias e lótus | focos 1 e 2 |

## Olhos
Se rosto: olhos fechados em arco serenos + marca Glow `FFF2C8` na testa (o ponto de leitura). Se máscara: 3 pontos Glow em triângulo. Em ambos, legível a 128 px.

## Detalhes-assinatura
- Um raio da coroa-eclipse quebrado.
- O planeta tem uma lua pequena que orbita só ele.

## Efeitos e aura (Mythic)
- Ambiente: **exclusivo `eclipse_corona`** (halo + 16 beams curtos pulsando na coroa); **exclusivo `galaxy_base`** (disco de galáxia girando sob a lótus + estrelas subindo); `orbit_ring` nos 2 anéis; `sparkle` na estrela com acento rosa Mythic. 8 emissores + 12 beams + 1 luz.
- Ação **Creation**: os 4 braços se juntam acima da cabeça e estrelas são sugadas → nasce uma galáxia (flash, disco de nebulosa expandindo, 24 estrelas, anéis expandem) → nebulosa se dissolve.

## Animação
Idle 5,0 s (paira, anéis giram opostos, braços de cima balançam planeta e estrela, manto ondula) · Fly 2,6 s (mantém o lótus, inclina à frente) · Happy 3,0 s (4 braços abrem, coroa gira) · Creation 3,2 s (fx em 0,7 s).

## Proibições e aceitação
- Imponente e larga (≥ 5). Distinta do Seraph e do Lich King: sentada, 4 braços, cósmica.
- Sem manto de pano mole, sem preto sem borda, anéis soltos (nunca presos rígidos ao corpo).
- A 64 px: figura dourada com disco de raios atrás + braços erguidos + base roxa.

## Referências a reusar
`CosmicDeity_alvo-2d` (meta, inclusive a lótus), `CosmicDeity_render-atual` (rig de 4 braços), seção 3 de `fichas-originais/ficha-L4-Cosmos.md`.
