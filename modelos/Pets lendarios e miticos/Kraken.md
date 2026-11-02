---
area: modelos
tipo: ficha-de-remake
resumo: Remake do Kraken (Legendary, CoralReef) — polvo colossal roxo-magenta com carapaça de placas, cracas e coral incrustados, olhos âmbar enormes e ventosas que brilham em ciano.
termos: kraken polvo coralreef legendary roxo magenta carapaca cracas coral ventosas ciano olhos ambar remake
---
# Kraken

**CoralReef · Legendary · gait `swim` · altura base 4,8 (corpo flutua a 1,4) · largura ≤ 5,6 com os tentáculos**

![[Recursos/Pets lendarios e miticos/Kraken_alvo-2d.webp|300]] ![[Recursos/Pets lendarios e miticos/Kraken_render-atual.webp|300]]

## Em uma frase
Um polvo antigo que dorme no fundo do mar há séculos: manto em gota coberto por uma carapaça de placas roxas, cracas e coral grudados, olhos âmbar furiosos sob pálpebras pesadas e tentáculos grossos com ventosas brilhando em ciano. Predador antigo, o oposto rústico do Pearl Seahorse.

## O que mudar em relação ao render atual
- **Cor do tema:** o render é azul-marinho quase preto (lê como mancha). O alvo é **roxo-violeta com reflexos magenta**. Trocar a paleta inteira (ver abaixo). É a mudança principal.
- **Ventosas:** no alvo cada ventosa tem aro ciano Glow com miolo escuro, em 2 fileiras na parte de baixo dos tentáculos, visíveis de frente. No render são rosa-acinzentadas e quase invisíveis.
- **Tentáculos grossos:** Ø 0,45 na base, afunilando; os 2 de ataque erguidos e curvados como ganchos (no alvo terminam em ponta de garra magenta). No render estão finos e embolados.
- **Olhos grandes e de frente:** âmbar-laranja Glow com pupila horizontal e pálpebra-placa pesada. No render estão pequenos e escuros.
- **Dorso dos tentáculos** com placas-escama pequenas seguindo a curva, como no alvo.

## Silhueta e proporções
- 3 formas-chave: **manto em gota** alongado para trás e para cima (nunca cilindro), **olhos visíveis de frente**, **coroa de 8 tentáculos em curva** (2 erguidos à frente, 6 curvados para baixo e para os lados).
- Manto 2,2 × 1,7; tentáculos com 2,8–3,4 de comprimento.
- Pose: flutuando, manto inclinado para trás, tentáculos de ataque erguidos em curva ameaçadora.

## Anatomia e construção
- Núcleo orgânico: manto com vinco central suave, cabeça com 2 bulbos oculares, tentáculos com seção oval achatada embaixo.
- **Carapaça:** 5–7 placas irregulares de borda ondulada no manto, com frestas mostrando a pele mais escura (nunca luz em tira).
- **Incrustações:** 3 grupos de cracas (cones com abertura), 2 tufos de coral ramificado laranja-coral, 1 concha espiral no flanco direito, como no alvo.
- **Tentáculos:** curva contínua (spline), dorso com placas-escama decrescentes, embaixo **2 fileiras de ventosas** (Ø 0,18 → 0,04) com aro e centro rebaixado.
- **Bico** de ardósia entre os tentáculos, visível por baixo.

## Paleta (3 tons + destaque)
| Papel | Hex | Onde |
| --- | --- | --- |
| Claro | `B070E0` (reflexo magenta `D060C0` nas arestas) | topo das placas, dorso dos tentáculos |
| Médio | `7A3CB8` | campo das placas e pele |
| Escuro | `3E1E6A` | frestas, ventre, sombra |
| Destaque (Glow) | `3CF0FF` ciano | aros das ventosas, manchas fotóforas |
| Olhos | `FFB020` âmbar com centro `FFE070` | íris |
| Acentos | coral `FF7A6B`, cracas `C8C0B0` / `8A8478`, concha `C8D8C0` | incrustações |

## Olhos
Grandes (Ø 0,45), na frente da cabeça, âmbar Glow com pupila horizontal preta em fenda, pálpebra-placa roxa cobrindo metade (cara de bravo). Precisam ler de frente e em 3/4 a 128 px.

## Detalhes-assinatura
- Cicatriz de 3 riscos (garras) na placa frontal do manto.
- Um tentáculo traseiro mais curto, com a ponta cortada.

## Efeitos e aura (Legendary)
- Ambiente: **exclusivo `bio_motes`** (6 motas ciano flutuando em volta do manto, 1,5/s); `sparkle` nos olhos a cada 5 s; bolhas do sifão a cada 3 s. 4 emissores.
- Ação **Grab**: tentáculos de ataque recuam e os fotóforos acendem em sequência → tentáculos fecham, nuvem de tinta escura com borda azul e anel de água → tinta se dissolve.

## Animação
Idle 4,0 s (tentáculos em onda defasada, manto respira, pálpebras piscam) · Swim 1,6 s (pulso de jato) · Happy 2,5 s (gira com tentáculos em estrela) · Grab 2,2 s (fx em 0,5 s). 8 ossos por tentáculo.

## Proibições e aceitação
- Manto orgânico, nunca cápsula ou tanque. Tentáculos são carne contínua, nunca corrente de esteira.
- Sem parafusos, tiras ciano retas ou segmentos retangulares.
- A 64 px: bola roxa com 2 olhos âmbar e tentáculos com pontos ciano.

## Referências a reusar
`Kraken_alvo-2d` (meta, inclusive a nova paleta roxa), `Kraken_render-atual` (rig de 8 tentáculos e incrustações aproveitáveis), seção 2 de `fichas-originais/ficha-L4-CoralReef.md` (a paleta azul-abissal da ficha fica substituída pela do alvo).
