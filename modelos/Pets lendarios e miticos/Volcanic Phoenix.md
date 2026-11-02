---
area: modelos
tipo: ficha-de-remake
resumo: Remake da Volcanic Phoenix (Legendary, Volcano) — ave de rapina de vitral de obsidiana com coração-brasa no peito e asas e cauda que terminam em chamas laranja-amarelas.
termos: volcanic phoenix fenix vulcanica volcano legendary obsidiana brasa vitral asas chamas remake
---
# Volcanic Phoenix

**Volcano · Legendary · gait `fly` · altura base 4,8 (corpo flutua a partir de 1,2) · envergadura 6,2**

![[Recursos/Pets lendarios e miticos/VolcanicPhoenix_alvo-2d.webp|300]] ![[Recursos/Pets lendarios e miticos/VolcanicPhoenix_render-atual.webp|300]]

Alvo 2D à esquerda, render atual à direita.

## Em uma frase
Uma águia forjada em vidro vulcânico: penas-lâmina preto-violeta com miolo de brasa, um losango de fogo no peito e asas e cauda que viram chama na ponta. Elegante e aérea, o oposto do Lava Titan. Personalidade orgulhosa e vigilante.

## O que mudar em relação ao render atual
- **Cauda:** hoje são poucas penas finas. No alvo é um **leque cheio de 5–7 plumas de fogo** longas e curvas, com degradê vermelho → laranja → amarelo, que ocupa quase um terço da silhueta. É a maior perda do render.
- **Pontas das asas:** o alvo tem os 25–30% finais de cada primária em laranja-amarelo vivo, com a borda quase branca. No render a transição é curta e apagada.
- **Peito:** o alvo mostra uma **treliça de losangos de brasa** (3 fileiras) em volta do losango central. No render são poucas manchas.
- **Corpo e pernas:** tórax maior e mais fundo (quilha), coxas emplumadas grossas e garras de ouro grandes. No render as pernas são palitos.
- **Olho:** aumentar 1,7× (pedido da rodada E), amarelo com pupila escura e aro de ouro.

## Silhueta e proporções
- 3 formas-chave: **V alto das asas** (pontas acima da cabeça, ~55°), **tórax em quilha** (gota invertida, peito projetado 0,5 à frente do pescoço), **leque de cauda em chamas** descendo a 30°.
- Tórax = 35% da altura do corpo; pescoço curto em S; cabeça 0,9 de comprimento, bico 0,35.
- Pose de repouso: pairando, cabeça erguida em perfil de águia, garras recolhidas mas visíveis.

## Anatomia e construção
- **Núcleo:** ave de rapina real, tórax oval profundo (1,1 × 1,3), pescoço em gota.
- **Peito:** 5 fileiras de penas-escama de obsidiana em gota (0,32 → 0,18), sobrepostas 30%, cada uma com borda chanfrada e miolo rebaixado. As 3 fileiras centrais têm o miolo em brasa (Glow), formando a treliça de losangos do alvo.
- **Asas:** 3 fileiras de coberteiras, 6 secundárias e **7 primárias** (1,6 → 2,2), lâminas de 2 faces com nervura central em V, afunilando. Ombro emplumado grosso (Ø 0,45) encaixado no tórax.
- **Cabeça:** bico curvo de ouro velho em 2 placas, sobrancelha pesada de obsidiana, **crista de 5 penas-lâmina** para trás com pontas em brasa.
- **Cauda:** 5 penas longas (2,0) em leque + 2 plumas de chama soltas (Glow/Spirit) que ondulam. Pontas em gota incandescente.
- **Patas:** coxas emplumadas, tarso com escamas de basalto e 4 garras de ouro curvas.

## Paleta (3 tons + destaque)
| Papel | Hex | Onde |
| --- | --- | --- |
| Escuro | `2A2236` (obsidiana com reflexo violeta; nunca abaixo disto nas áreas grandes) | penas, sobrancelha |
| Médio | `4A3A5E` (borda violeta das penas) | moldura das penas, dorso |
| Claro | `C9962E` ouro velho | bico, garras, filete da raiz das asas |
| Destaque (Glow) | `FF7A1E` → `FFC040` → `FFE9A0` na ponta | coração, pontas de asa, cauda, olhos |

## Materiais
Obsidiana-vidro (rough 0,2, sem metal), basalto fosco no tarso, ouro velho (rough 0,35, metal 0,9), e uma faixa de **brasa pintada** (`7A2A10` → `FF6E28`) na Color fazendo a transição entre obsidiana e Glow.

## Olhos
Amêndoa amarela Glow (`FFC040`), pupila escura vertical, aro de ouro e sobrancelha pesada por cima. Tamanho 1,7× o atual; legível a 128 px.

## Detalhes-assinatura
- Asa **esquerda** com 1 primária quebrada pela metade.
- Arranhão claro no bico de ouro.

## Efeitos e aura (Legendary)
- Ambiente: `core_pulse` laranja no losango do peito (1,4 s); **exclusivo `ember_fall`**: penas incandescentes caindo da cauda a 0,6/s, apagando para cinza; `aura` de brasa leve sob as asas; `trail` de faíscas nas pontas das asas só em movimento. 5 emissores + 2 trails.
- Acento dourado de raridade: no filete das garras.
- Ação **Flare**: asas fecham e o núcleo carrega (0,4 s) → abre com anel de brasas e 24 brasas radiais → penas caem e fumaça sobe (1,2 s).

## Animação
Idle 3,0 s (paira, batida lenta a cada 1,5 s, cabeça vira, cauda ondula com atraso) · Fly 1,2 s (corpo inclinado 15°) · Happy 2,2 s (giro de barril + grito) · Flare 2,0 s (fx em 0,4 s). As plumas da cauda devem ter 2 ossos cada para ondular.

## Proibições e aceitação
- Penas leem como lâminas de vidro com nervura, nunca cartas retangulares ou losangos chapados.
- Laranja não pode cobrir o corpo todo; Glow ≤ 25% da superfície.
- Ícone a 64 px: o V das asas com pontas laranja e o losango do peito precisam aparecer.

## Referências a reusar
`VolcanicPhoenix_alvo-2d` (meta), `VolcanicPhoenix_render-atual` (rig e base de malha aproveitáveis), seção 1 de `fichas-originais/ficha-L4-Volcano.md`.
