---
area: modelos
tipo: ficha-de-remake
resumo: Remake do Sky Emperor (Mythic, SkyKingdom) — grifo imperial de placas de mármore, azul-real e ouro, juba solar de lâminas douradas, asas abertas em V, medalhão-sol no peito e coroa-sol sobre a cabeça.
termos: sky emperor imperador do ceu skykingdom mythic grifo marmore azul real ouro juba solar asas medalhao coroa sol remake
---
# Sky Emperor

**SkyKingdom · Mythic · gait `fly` · altura base 6,6 (topo da coroa) · comprimento 6,0 · envergadura 7,0**

![[Recursos/Pets lendarios e miticos/SkyEmperor_alvo-2d.webp|300]] ![[Recursos/Pets lendarios e miticos/SkyEmperor_render-atual.webp|300]]

## Em uma frase
O Imperador dos Céus: um grifo colossal de armadura imperial, com corpo de placas de mármore e azul-real, juba de lâminas douradas em raios de sol em volta da cabeça de águia, asas largas abertas em V com pontas azuis, garras de ouro, medalhão-sol no peito e uma coroa-sol acima da cabeça. A peça mais régia do jogo.

## O que mudar em relação ao render atual
- **Pose e silhueta:** o render está sentado, compacto e com o topo atulhado (coroa em "cartola"). O alvo está **de pé, em posição de ataque**, com asas largas abertas e cauda longa em curva. Seguir o alvo.
- **Coroa:** o alvo usa uma **coroa-sol** leve (aro com estrela de 4 pontas sobre a cabeça) em vez da coroa-templo de colunas. Mais limpa a 64 px. Ver a decisão abaixo.
- **Contraste azul/branco/ouro:** alvo com azul-real saturado nas pernas, barriga e pontas das asas. O render está mais branco.
- **Cauda longa** com placas e espinhos dourados (no alvo é quase de dragão), não só o tufo leonino.
- **Olho azul-céu** Glow bem marcado (pendência C2).

## Decisão em aberto: coroa-templo ou coroa-sol
- Ficha: coroa-templo (arco de 5 colunas jônicas com frontão).
- Alvo 2D: aro dourado com estrela flutuando acima da cabeça.
- **Recomendo a coroa-sol do alvo**: lê melhor de longe e não compete com a juba. A ideia de "templo" pode ficar no medalhão do peito.

## Silhueta e proporções
- 3 formas-chave: **juba solar** em raios em volta da cabeça, **asas em V largo** acima do corpo, **cauda longa curvada** com tufo de lâminas.
- Peito profundo (2,0), patas dianteiras de águia com garras grandes (0,5), traseiras de leão musculosas.
- Pose: de pé nas 4 patas (ou com uma dianteira erguida), peito à frente, asas abertas.

## Anatomia e construção
- Núcleo de grifo real (peito e ombros de águia, ancas de leão).
- **Penas do peito e cabeça:** escamas-pena de mármore em gota com quilha central.
- **Corpo traseiro:** placas de mármore com friso grego em relevo e faixas azul-real.
- **Juba:** 3 anéis de lâminas douradas (24) em raios, comprimentos alternados, com caneluras.
- **Cabeça:** bico de águia de ouro em 2 placas, sobrancelha pesada de mármore.
- **Asas:** 4 fileiras de lâminas de mármore e azul, ombro em voluta de ouro, pontas azul-real.
- **Patas dianteiras:** tarso de escamas de ouro, 4 garras. **Traseiras:** de leão com placa de coxa.
- **Cauda:** segmentos de placas com espinhos dourados e tufo final de 5 lâminas.
- **Medalhão-sol** no peito: disco de ouro com sol art déco e gema central.

## Paleta (3 tons + destaque)
| Papel | Hex | Onde |
| --- | --- | --- |
| Claro | `F2F0E8` mármore | penas, placas |
| Médio | `2A4CC0` azul-real | pernas, barriga, pontas das asas, faixas |
| Escuro | `1A2E66` | frestas, sombra |
| Metal | `E8B83A` / `A87A1E` ouro-sol | juba, bico, garras, coroa, medalhão, espinhos |
| Destaque (Glow) | `FFE58A` sol; `9AD8FF` céu nos olhos | gema da coroa, medalhão, olhos |

## Olhos
Azul-céu `9AD8FF` Glow, pupila escura, sob sobrancelha de mármore pesada; olhar feroz. Legível a 128 px dentro da juba.

## Detalhes-assinatura
- Uma ponta da coroa faltando.
- Garra dianteira direita de ouro maciço (substituta), diferente das outras.

## Efeitos e aura (Mythic)
- Ambiente: **exclusivo `sun_corona`** (12 raios de sol curtos girando em volta da juba); **exclusivo `cloud_throne`** (nuvens rolando sob as patas); `sparkle` na coroa com acento rosa Mythic. 7 emissores + 12 beams + 1 luz.
- Ação **Roar**: a juba recolhe e a coroa escurece → juba abre num flash solar, onda de vento radial e anel dourado no chão → penas e nuvens.

## Animação
Idle 4,5 s (respira, cauda balança, asas ajustam, juba vibra) · Fly 1,8 s (planado, batida ampla) · Happy 3,0 s (ergue-se nas traseiras e abre as asas) · Roar 2,8 s (fx em 0,6 s; o rugido era pendência C2).

## Proibições e aceitação
- Grifo legível (cabeça e garras de águia + ancas de leão). Distinto do Seraph (quadrúpede).
- Sem penas fofas, leão de cara grande ou branco sem contraste.
- A 64 px: asas azuis abertas + bola de raios dourados na cabeça.

## Referências a reusar
`SkyEmperor_alvo-2d` (meta, inclusive pose e coroa-sol), seção 3 de `fichas-originais/ficha-L4-SkyKingdom.md`. Render atual só para rig.
