---
area: modelos
tipo: ficha-de-remake
resumo: Remake do Leviathan (Mythic, CoralReef) — serpente marinha real em espiral, escamas de pérola negra azul com borda turquesa, linha lateral de fotóforos ciano, barriga de nácar e coroa de coral branco.
termos: leviathan leviata serpente marinha coralreef mythic perola negra turquesa fotoforos espiral coroa nacar remake
---
# Leviathan

**CoralReef · Mythic · gait `swim` · altura base 6,4 (topo da coroa) · corpo ~16 em espiral, pegada ≤ 7 × 7**

![[Recursos/Pets lendarios e miticos/Leviathan_alvo-2d.webp|300]] ![[Recursos/Pets lendarios e miticos/Leviathan_render-atual.webp|300]]

## Em uma frase
O rei antigo das profundezas: uma serpente-dragão marinha enrolada em espiral ascendente, escamas azul-pérola-negra com borda turquesa, uma fileira de luzes ciano ao longo do corpo, barriga de nácar e uma coroa de espinhos brancos com pérolas.

## O que mudar em relação ao render atual
O render já está perto do alvo. Ajustes:
- **Valor:** clarear o azul das escamas para `1E3A7A` com highlight `3A6AC0` (o render está escuro). O alvo lê azul-royal, não preto.
- **Fotóforos maiores e mais brilhantes**, pontos de Ø 0,08–0,14 (o alvo tem pontos bem visíveis).
- **Espiral mais cheia e volumosa:** corpo Ø 1,1 no terço anterior; a volta de baixo bem apoiada, como no alvo.
- **Cabeça 50% maior** que na v1 (1,6 de comprimento) e **olho turquesa em amêndoa** (pedido da rodada E).
- **Barbatanas** turquesa claras mais largas e com borda ondulada.

## Silhueta e proporções
- 3 formas-chave: **espiral ascendente** (1,5 volta), **cabeça grande coroada** no topo, **crista dorsal contínua** de barbatanas translúcidas.
- Corpo Ø 1,1 → 0,25 na cauda, seção oval (mais alta que larga), pescoço sem estreitamento brusco.
- Pose: espiral, cabeça erguida no topo olhando à frente e para baixo, boca entreaberta.

## Anatomia e construção
- **Dorso:** escamas-placa em gota (0,35 × 0,28) com borda turquesa elevada, sobrepostas 30%.
- **Flancos:** escamas menores (0,14) em fileiras diagonais. **Barriga:** placas segmentadas de nácar branco-creme, como no alvo.
- **Crista dorsal:** raios de nácar curvos com membrana ondulada translúcida, do crânio até 2/3 do corpo.
- **Cabeça:** crânio de dragão marinho anguloso, sobrancelha de placa, 2 fileiras de dentes de nácar, língua, barbatanas laterais em leque no lugar das orelhas, **2 barbilhões longos (1,2) brancos e curvos**, 2 chifres em espiral de concha.
- **Coroa (marca Mythic):** arco de coral branco ramificado com 5 pérolas e filetes de ouro-areia.
- **Nadadeiras:** 2 pares em forma de nadadeira real. **Cauda:** leque grande assimétrico.

## Paleta (3 tons + destaque)
| Papel | Hex | Onde |
| --- | --- | --- |
| Claro | `F2EEE6` nácar | barriga, crista, dentes, barbilhões, coroa |
| Médio | `1E3A7A` com iridescência `3A6AC0` / `4A3A7A` em manchas | escamas dorsais |
| Escuro | `101C3A` | frestas e flancos baixos |
| Destaque (Glow) | `3CF0FF` fotóforos; `FFE6B0` pérolas da coroa | linha lateral, pérolas, olhos |
| Borda | `28C8DC` turquesa | moldura das escamas, barbatanas (Spirit 0,4) |

## Olhos
Amêndoa turquesa `3CF0FF` Glow com pupila escura, sob sobrancelha de placa. Legível a 128 px mesmo com a cabeça no topo da espiral.

## Detalhes-assinatura
- Falta 1 pérola na coroa (engaste vazio, à esquerda).
- Uma craca grudada no chifre direito.

## Efeitos e aura (Mythic)
- Ambiente: **exclusivo `water_ring`** (anel de água turquesa com cáustica girando em volta da espiral, raio 3, inclinado 10°); **exclusivo `bubble_spiral`** (bolhas subindo em espiral pelo corpo); `sparkle` pérola na coroa (acento rosa Mythic numa pérola); `core_pulse` turquesa. 7 emissores + 8 beams.
- Ação **Roar**: cabeça recua e os fotóforos acendem da cauda para a cabeça → boca abre, o anel de água expande e sai uma onda de bolhas → espuma e motas.

## Animação
Idle 5,0 s (onda subindo pela espiral, barbilhões e barbatanas ondulam) · Swim 2,4 s (serpentina) · Happy 3,0 s (espiral sobe, cabeça gira 360°) · Roar 2,6 s (fx em 0,6 s).

## Proibições e aceitação
- Escamas em gota seguindo a curva, nunca ladrilhos. Nadadeiras com forma de nadadeira, nunca leque de mão.
- Sem painéis de vidro retos nem tiras de LED.
- A 64 px: espiral azul com pontos ciano + cabeça coroada branca.

## Referências a reusar
`Leviathan_alvo-2d` (meta), `Leviathan_render-atual` (forma aprovada, base para polir), seção 3 de `fichas-originais/ficha-L4-CoralReef.md`.
