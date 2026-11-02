---
area: modelos
tipo: ficha-de-remake
resumo: Remake do Black Hole Cat (Legendary, Cosmos) — gato egípcio sentado azul-noite com colar e braceletes de ouro e turquesa, buraco negro com disco de acreção cruzando o peito e cauda que termina em cometa de cristal.
termos: black hole cat gato buraco negro cosmos legendary egipcio esfinge ouro turquesa disco de acrecao cometa remake
---
# Black Hole Cat

**Cosmos · Legendary · gait `ground` · altura base 4,8 (orelhas) · largura 1,6 · comprimento 3,0 sentado**

![[Recursos/Pets lendarios e miticos/BlackHoleCat_alvo-2d.webp|300]] ![[Recursos/Pets lendarios e miticos/BlackHoleCat_render-atual.webp|300]]

## Em uma frase
Um gato-esfinge cósmico sentado como estátua egípcia: corpo azul-noite elegante, colar largo de ouro e turquesa com um olho no centro, braceletes nas patas, brinco de anel planetário, e no peito um buraco negro de verdade com disco de acreção laranja-magenta girando na horizontal. A cauda enrola à frente e termina num cristal-cometa violeta.

## O que mudar em relação ao render atual
- **Base de pedestal:** o render tem uma placa/trenó embaixo do gato. Tirar; o alvo é o gato sentado sem base.
- **Disco de acreção maior e mais quente:** no alvo é um anel largo laranja → magenta → violeta que sai da silhueta dos 2 lados. No render está fino.
- **Corpo:** o alvo é **liso e polido** (placas grandes e suaves de azul-noite com highlight azul), não coberto de placas pequenas. Seguir o alvo: placas poucas e grandes com borda fina, nebulosa só em detalhes.
- **Colar egípcio** largo com turquesa e ouro, como no alvo (o render já tem; aumentar o turquesa).
- **Olhos** âmbar-dourados amendoados, maiores (no alvo leem bem; no render somem).

## Decisão menor: cor dos olhos
Ficha: olhos ciano. Alvo: âmbar-dourado. **Recomendo âmbar** (contrasta com o corpo azul e com o disco).

## Silhueta e proporções
- 3 formas-chave: **gato egípcio sentado** (pescoço longo, orelhas grandes), **disco de acreção horizontal** Ø 1,8 cruzando o peito, **cauda enrolada com cometa**.
- Cabeça 0,8; pescoço 0,6; peito estreito e alto; patas dianteiras retas com punho marcado.

## Anatomia e construção
- Núcleo de gato sentado (R10) com ombro e coxa marcados.
- **Placas** grandes de azul-noite polido com borda chanfrada fina e highlight; miolo de nebulosa só nas orelhas e na coxa (pequenas janelas de espaço).
- **Buraco negro:** esfera Ø 0,7 preto absoluto (rough 1), 3 anéis de lâminas finas formando o disco (quente perto, frio longe), preso por 4 garras de ouro.
- **Cabeça:** focinho fino, diadema de constelação na testa com joia turquesa, orelhas altas com anéis de ouro, brinco planetário na esquerda.
- **Colar:** placas de ouro e turquesa com olho central e 7 pontos Glow.
- **Braceletes** de ouro e turquesa nas patas dianteiras; medalhão hexagonal na coxa (como no alvo).
- **Cauda:** segmentada, enrolada, ponta em cristal violeta facetado.

## Paleta (3 tons + destaque)
| Papel | Hex | Onde |
| --- | --- | --- |
| Claro | `5A6AB0` (highlight azul nas arestas) | topo das placas |
| Médio | `2A3466` azul-noite | corpo |
| Escuro | `181E40` | sombra, frestas |
| Metal | `E8C25A` ouro-estelar; `2AC8B8` turquesa | colar, braceletes, anéis |
| Destaque (Glow) | disco `FFB040` → `FF4AC0` → `9A6AFF`; olhos `FFC040`; cometa `B88CFF` | focos 1 e 2 |
| Buraco | `000000` | esfera |

## Olhos
Amêndoa âmbar-dourada `FFC040` Glow com pupila vertical em fenda, delineado escuro egípcio. Legíveis a 128 px.

## Detalhes-assinatura
- Uma placa do flanco "sugada", esticada em direção ao buraco negro.
- Brinco só na orelha esquerda.

## Efeitos e aura (Legendary)
- Ambiente: **exclusivo `accretion`** (disco girando no buraco); **exclusivo `infall`** (estrelas sugadas em espiral para o centro, 2/s); anel de distorção sutil; rastro de cometa na cauda. 5 emissores + 4 beams.
- Ação **Devour**: o disco acelera e puxa partículas de 4 studs → implosão com flash branco e anel de distorção → estrelas voltam a orbitar.

## Animação
Idle 4,0 s (sentado, ponta da cauda mexe, orelhas giram, disco gira) · Walk 1,6 s (elegante, altivo) · Happy 2,2 s (se lambe e o disco pisca) · Devour 2,4 s (fx em 0,6 s).

## Proibições e aceitação
- Buraco negro legível de lado e de frente, sempre fora da silhueta.
- Lê como gato egípcio. Sem preto chapado sem borda, pontinhos de estrela pelo corpo todo ou cara fofa.
- A 64 px: gato azul sentado + anel laranja-magenta no peito + colar dourado.

## Referências a reusar
`BlackHoleCat_alvo-2d` (meta), `BlackHoleCat_render-atual` (malha e rig, tirar a base), seção 1 de `fichas-originais/ficha-L4-Cosmos.md`.
