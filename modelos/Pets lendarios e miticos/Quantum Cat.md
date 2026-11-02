---
area: modelos
tipo: ficha-de-remake
resumo: Remake do Quantum Cat (Legendary, CyberCity) — gato-mecha de infiltração de placas de aço claro e navy, visor ciano em V, cauda segmentada que se desfaz em cubos ciano e magenta com anel de portal.
termos: quantum cat gato quantico cybercity legendary mecha gato aco navy visor ciano cubos voxel glitch portal QC-07 remake
---
# Quantum Cat

**CyberCity · Legendary · gait `ground` · comprimento base 5,6 · altura 3,4 (ponta da cauda) · largura 1,4**

![[Recursos/Pets lendarios e miticos/QuantumCat_alvo-2d.webp|300]] ![[Recursos/Pets lendarios e miticos/QuantumCat_render-atual.webp|300]]

## Em uma frase
Um gato-robô de infiltração da mesma fabricante do Mecha Titan: chassi de placas de aço claro e navy sobre juntas de pistão, visor ciano em V no lugar dos olhos, orelhas em lâmina, e uma cauda longa que se fragmenta em cubos ciano e magenta flutuando dentro de um anel de portal.

## O que mudar em relação ao render atual
O render foi refeito 3 vezes e já está perto do alvo. Ajustes:
- **Pose de espreita** do alvo: cabeça baixa, uma pata dianteira erguida, dorso arqueado. O render está mais rígido.
- **Contraste:** o alvo tem placas brancas-azuladas `E0E6F0` bem claras e navy `24306A` saturado no dorso e na cabeça. Subir o branco das placas.
- **Linhas de luz ciano** nas laterais das placas (curtas, como no alvo), sem virar neon espalhado.
- **Patas** com garras visíveis e articulação digitígrada mais marcada.
- **Marcação:** o alvo e o render usam **"QC-07"** (a ficha dizia "Q-02"). Manter "QC-07", que liga ao "07" do Mecha Titan.

## Silhueta e proporções
- 3 formas-chave: **corpo felino alongado e magro** com dorso arqueado, **orelhas grandes em lâmina**, **cauda longa em S que se desfaz em cubos**.
- Cabeça pequena (0,9) com focinho curto em cunha; pernas longas e finas digitígradas; patas de 4 dedos em garra.

## Anatomia e construção
- Núcleo de gato real (R10): peito estreito, cintura fina, coxas fortes.
- **Placas:** capacete craniano, placa de focinho, colar segmentado, dorso em 7 placas sobrepostas com fenda central de luz, ombros, coxas e canelas com placa frontal.
- **Juntas expostas** com pistões e cabos (grafite e magenta) em cotovelo, joelho e jarrete.
- **Cabeça:** visor em V ciano (como olhos de gato), orelhas em lâmina chanfrada, 2 antenas finas, bigodes de 3 hastes por lado.
- **Cauda:** 60% em segmentos de vértebra com placas; os 40% finais se desfazem em ~30 cubos decrescentes, ciano e magenta, com um anel de portal ciano em volta.

## Paleta (3 tons + destaque)
| Papel | Hex | Onde |
| --- | --- | --- |
| Claro | `E0E6F0` aço claro | placas principais |
| Médio | `24306A` navy | dorso, capacete, faixas |
| Escuro | `2E3440` grafite | juntas, núcleo |
| Destaque (Glow) | `3CF0FF` ciano; `FF5AD0` magenta | visor, linhas laterais, cubos, núcleo do peito |
| Acento | faixa de aviso `F2C230` + `1A1A1A`; cabos `FF3CA8` | coxa direita, juntas |

## Olhos
Sem olhos de desenho: o **visor em V ciano** faz o papel de olhos (decisão de projeto). Ele precisa ler como "gato bravo" a 64 px.

## Detalhes-assinatura
- "QC-07" no ombro e faixa de aviso na coxa direita.
- Uma orelha com a ponta cortada em V (gato de rua).

## Efeitos e aura (Legendary)
- Ambiente: **exclusivo `quantum_ghost`** (a cada 3 s um eco translúcido do corpo pisca 0,3 stud ao lado, em glitch); **exclusivo `portal_ring`** (anel de portal orbitando a cauda); `sparkle` ciano nos cubos. 5 emissores + 8 beams.
- Ação **Blink**: agacha e os cubos se juntam → o corpo some com burst de cubos e glitch e reaparece 2 studs à frente com anel de portal → dissipa (o root volta; deslocamento só visual).

## Animação
Idle 3,5 s (sentado, cauda abana, orelhas giram, cubos orbitam) · Walk 1,4 s (furtivo, ombros em pêndulo) · Happy 2,2 s (espreguiça e dá pounce) · Blink 1,8 s (fx em 0,4 s).

## Proibições e aceitação
- Lê como gato de longe. Nada de cara de cachorro ou raposa, pernas de tubo, olhões fofos ou neon espalhado.
- A 64 px: gato branco e navy + visor ciano + nuvem de cubos na cauda.

## Referências a reusar
`QuantumCat_alvo-2d` (meta), `QuantumCat_render-atual` (malha e rig quase finais), `MechaTitan_referencia` (linguagem de painéis), seção 1 de `fichas-originais/ficha-L4-CyberCity.md`.
