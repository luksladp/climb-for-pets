---
area: modelos
tipo: ficha-de-remake
resumo: Remake do Sprinkle Dragon (Mythic, CandyLand) — dragão robusto de confeitaria de luxo com escamas de chocolate, placas de bala pastel, glacê escorrendo com confeitos, chifres de bengala e asas de wafer com membrana rosa e menta.
termos: sprinkle dragon dragao de confeito candyland mythic chocolate glace confeitos bengala wafer bala coroa cristal remake
---
# Sprinkle Dragon

**CandyLand · Mythic · gait `ground` · altura base 6,4 (topo dos chifres) · comprimento ≤ 9,0**

![[Recursos/Pets lendarios e miticos/SprinkleDragon_alvo-2d.webp|300]] ![[Recursos/Pets lendarios e miticos/SprinkleDragon_render-atual.webp|300]]

## Em uma frase
O "bolo de casamento" dos dragões: corpo robusto e baixo de escamas de chocolate, com placas de bala pastel nos flancos, um rio de glacê branco escorrendo pelo dorso cheio de confeitos, chifres de bengala listrada e asas de wafer com membrana de bala rosa e menta. Glutão orgulhoso.

## O que mudar em relação ao render atual
O render está longe do alvo:
- **Corpo manchado:** o render mistura rosa e marrom em todo lugar e lê como ruído. O alvo é **chocolate dominante** (marrom `6B3F26`) com **placas pastel organizadas** (rosa `F4A0B8`, menta `A8E0B0`, creme `F0E0C0`) só nos flancos e no peito.
- **Cabeça branca e boca escancarada** no render. No alvo a cabeça é de **chocolate com focinho creme**, boca fechada ou levemente aberta com dentes de açúcar, olho grande e claro.
- **Glacê:** no alvo é uma faixa branca contínua e grossa, do pescoço à cauda, com gotas penduradas e confeitos coloridos **só nela**. No render está quebrado.
- **Asas:** no alvo são abertas, com dedos de wafer/chocolate e membrana rosa (esquerda) e menta (direita). No render estão finas e escuras.
- **Barriga** de wafer quadriculado dourado bem visível.
- **Olhos:** balas verde-menta (pedido da rodada E).

## Silhueta e proporções
- 3 formas-chave: **chifres de bengala grandes**, **corpo robusto com faixa de glacê no dorso**, **asas abertas de wafer**.
- Pescoço curto e grosso (22%), cabeça grande (1,5), patas largas (40% maiores que na v1), tórax 2,8.
- Pose: 4 patas, corpo baixo, peito estufado, cabeça erguida.

## Anatomia e construção
- Núcleo de dragão musculoso, peito fundo (2,2), ancas largas.
- **Escamas de chocolate** em gota no dorso e na cabeça, com quina viva e padrão de tablete em relevo nas maiores.
- **Placas de bala pastel** facetadas nos flancos e ombros, em 3 cores, cada uma com moldura de chocolate (como no alvo).
- **Glacê:** faixa contínua grossa com borda definida e gotas de comprimentos variados; ~80 confeitos em 6 cores **só no glacê**.
- **Barriga:** 12 placas de wafer quadriculado com borda de caramelo.
- **Cabeça:** focinho largo creme, sobrancelha de chocolate pesada, dentes de açúcar, **2 chifres de bengala** (1,3) com listra helicoidal contínua, 2 chifres pequenos de chocolate.
- **Coroa (Mythic):** 5 cristais de açúcar facetados em arco na nuca.
- **Espinhos:** fileira de bala dura cristalina, rosa → menta.
- **Asas:** dedos de wafer/chocolate com garra de açúcar, membrana de bala translúcida (rosa e menta) com veios de glacê.
- **Cauda:** espinhos creme e cristal de açúcar grande na ponta.

## Paleta (3 tons + destaque)
| Papel | Hex | Onde |
| --- | --- | --- |
| Claro | `F7F2EA` glacê e `F0E0C0` creme | glacê, focinho, garras, dentes |
| Médio | `6B3F26` chocolate ao leite | escamas e corpo |
| Escuro | `3E2418` chocolate amargo (sombra `2E1A10` só em frestas) | moldura, sombra |
| Pastel | `F4A0B8` rosa, `A8E0B0` menta, `D9A866` wafer | placas, barriga, membranas |
| Destaque (Glow) | `FF5FC0` + `FFE14A` | coroa de cristais, garganta, cristal da cauda |

## Olhos
Balas verde-menta `6EE0B8` vítreas e Glow, pupila escura, brilho branco, sob sobrancelha de chocolate. Grandes o bastante para ler a 128 px, mas sem cara fofa.

## Detalhes-assinatura
- Ponta de um chifre de bengala mordida.
- Uma gota de glacê longa escorrendo até o joelho dianteiro esquerdo.

## Efeitos e aura (Mythic)
- Ambiente: **exclusivo `sprinkle_rain`** (confeitos caindo do dorso e quicando, 1,5/s); `sparkle` de açúcar na coroa e no cristal da cauda (acento rosa Mythic); `core_pulse` rosa na garganta. 6 emissores + 1 luz.
- Ação **Breath**: cabeça sobe e garganta brilha → jato cônico de cintilas de açúcar, confeitos e fumaça rosa → confeitos caem e quicam.

## Animação
Idle 4,0 s (respira, cauda abana, lambe os lábios) · Walk 1,8 s (gingado robusto) · Happy 3,0 s (sacode o corpo como cachorro, confeitos voam) · Breath 2,4 s (fx em 0,6 s).

## Proibições e aceitação
- Pernas de dragão com músculo, nunca blocos. Listra helicoidal contínua nos chifres (nunca xadrez).
- Confeitos só no glacê. Sem pastel lavado no corpo todo nem listras fora dos chifres.
- A 64 px: dragão marrom + faixa branca no dorso + chifres listrados + asas rosa/menta.

## Referências a reusar
`SprinkleDragon_alvo-2d` (meta, inclusive as placas pastel que a ficha não tinha), seção 3 de `fichas-originais/ficha-L4-CandyLand.md`. O render atual serve só para rig.
