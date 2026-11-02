---
area: modelos
tipo: ficha-de-remake
resumo: Remake do Seraph (Legendary, SkyKingdom) — serafim guardião de armadura azul-real e ouro com sol art déco no peito, máscara de porcelana com um olho-sol, 6 asas de lâminas de mármore, halo e lança dourada.
termos: seraph serafim skykingdom legendary anjo armadura azul ouro sol art deco mascara olho sol seis asas halo lanca remake
---
# Seraph

**SkyKingdom · Legendary · gait `fly` · altura base 5,8 (ponta das asas) · envergadura 6,0 · corpo a 0,8**

![[Recursos/Pets lendarios e miticos/Seraph_alvo-2d.webp|300]] ![[Recursos/Pets lendarios e miticos/Seraph_render-atual.webp|300]]

## Em uma frase
Um guardião celestial sem rosto humano: armadura azul-real com um sol dourado art déco no peito, máscara de porcelana lisa com uma única fenda de luz, 6 asas de lâminas de mármore com pontas azuis abertas em leque, halo de ouro atrás da cabeça e uma lança dourada vertical.

## O que mudar em relação ao render atual
- **Leitura de longe:** o render ficou pálido e "fino" (defeito antigo da v2/v3). No alvo o **torso azul-real saturado** contrasta forte com as asas brancas e o ouro. Saturar o azul e alargar o torso (1,6 nos ombros).
- **Asas em leque simétrico:** no alvo as 6 asas formam um hexágono limpo em volta do corpo, com as **pontas azuis**. No render estão embaralhadas e brancas demais.
- **Olho-sol** maior, fenda com halo (pedido da rodada E), Glow amarelo forte.
- **Volutas douradas** dos ombros maiores e mais visíveis, como no alvo.
- **Cauda de lâminas** azuis (sem pernas) bem definida embaixo.

## Silhueta e proporções
- 3 formas-chave: **3 pares de asas em leque hexagonal**, **torso em V de armadura com ombreiras em voluta**, **halo com raios** + lança vertical.
- Torso 1,6 nos ombros, cintura 0,8; sem pernas (quadril vira cauda de lâminas); cabeça 0,55.
- Pose: pairando ereto, asas superiores em V alto, inferiores cruzadas sob o corpo, lança vertical na mão direita.

## Anatomia e construção
- Núcleo de torso atlético e braços musculosos; quadril vira saia de 8 lâminas longas.
- **Armadura:** peitoral com **sol art déco em relevo** (raios escalonados) e placas em escama abaixo, ombreiras em voluta dupla (3 camadas), braçais com caneluras, manoplas de ouro articuladas.
- **Máscara:** porcelana oval lisa, fenda horizontal única, coroa de 5 raios dourados na testa.
- **Asas:** ombro de ouro tipo relojoaria, 3 fileiras de lâminas (coberteiras, médias, primárias de 1,6–2,4), mármore com filete de ouro e **pontas azul-real**.
- **Halo:** anel de ouro com 12 raios e runas, preso ao dorso por haste fina.
- **Lança:** haste dourada com faixas azuis e ponta de cristal de luz (5,4).

## Paleta (3 tons + destaque)
| Papel | Hex | Onde |
| --- | --- | --- |
| Claro | `F2EEE4` mármore | asas, máscara |
| Médio | `2A4CC0` azul-real vivo | armadura, pontas das asas, cauda |
| Escuro | `1A2E66` | frestas, sombra da armadura |
| Metal | `E8B83A` ouro-sol | sol do peito, volutas, manoplas, halo, lança |
| Destaque (Glow) | `FFE58A` | olho-sol, ponta da lança, runas do halo |

## Olhos
Uma única fenda horizontal Glow `FFE58A` com halo suave em volta, na máscara lisa. É o foco 1 e deve ler a 64 px.

## Detalhes-assinatura
- Uma lâmina da asa superior esquerda partida.
- Faixa de tecido azul rasgada pendendo da cintura, só à direita.

## Efeitos e aura (Legendary)
- Ambiente: **exclusivo `feather_fall`** (penas de luz caindo das asas, 0,8/s); `halo_glow` dourado no halo; `sparkle` sol na ponta da lança. 5 emissores + 2 beams + 1 luz.
- Ação **Judgement**: as 6 asas abrem e a lança sobe → coluna de luz vertical descendo, halo dourado expandindo e 16 penas → dissipa.

## Animação
Idle 4,0 s (asas respiram em defasagem por par, halo gira lento) · Fly 1,6 s (asas médias batem) · Happy 2,5 s (6 asas abrem em estrela e giro) · Judgement 2,4 s (fx em 0,5 s).

## Proibições e aceitação
- Sem rosto humano, sem asas de penas macias (usar lâminas), sem armadura lisa sem friso, sem branco puro sem azul.
- A 64 px: estrela branca de asas com centro azul e ponto dourado.

## Referências a reusar
`Seraph_alvo-2d` (meta), `Seraph_render-atual` (rig das 6 asas), seção 2 de `fichas-originais/ficha-L4-SkyKingdom.md`.
