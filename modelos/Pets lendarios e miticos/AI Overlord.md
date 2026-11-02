---
area: modelos
tipo: ficha-de-remake
resumo: Remake do AI Overlord (Mythic, CyberCity) — IA chefe final com cérebro magenta em cúpula de vidro, tronco de módulos de servidor, 6 braços mecânicos com garras, coroa de antenas e pratos, pairando sobre anel de propulsão.
termos: ai overlord ia suprema cybercity mythic cerebro cupula vidro servidor seis bracos garras antenas satelite propulsao omega-00 remake
---
# AI Overlord

**CyberCity · Mythic · gait `fly` (paira a 0,6) · altura base 6,4 · largura 5,6 com os braços**

![[Recursos/Pets lendarios e miticos/AIOverlord_alvo-2d.webp|300]] ![[Recursos/Pets lendarios e miticos/AIOverlord_render-atual.webp|300]]

## Em uma frase
O chefe final da CyberCity: um cérebro rosa-magenta brilhante dentro de uma cúpula de vidro com armação de aço, sobre um tronco de módulos de servidor, com 6 braços mecânicos segmentados terminando em garras e ferramentas, uma coroa de antenas e pratos de satélite, e um anel de propulsão com faixa de aviso embaixo.

## O que mudar em relação ao render atual
O render já está perto do alvo. Ajustes:
- **Cérebro mais vivo:** o alvo tem magenta `FF4AD0` saturado com sulcos e linhas de circuito ciano. O render está rosa-claro e lavado.
- **Cúpula:** vidro azul-ciano mais visível (`AEEBFF`, Transparency 0,45) com nervuras de aço grossas, como no alvo.
- **Braços:** segmentos com **anéis azul-navy e aço** alternados e juntas ciano brilhantes; mais grossos na raiz. No render estão finos e cinza.
- **Tronco:** módulos com LEDs ciano curtos e painéis navy, como no alvo.
- **Anel de propulsão** com faixa de aviso e emissores ciano para baixo mais fortes.

## Silhueta e proporções
- 3 formas-chave: **cúpula grande com cérebro luminoso**, **leque de 6 braços**, **coroa de antenas assimétrica**.
- Cúpula Ø 2,2 (35% da altura); tronco afunila de 1,6 para 0,9; braços 2,4–3,0; anel de propulsão Ø 2,0.
- Pose: ereto, braços em leque (2 altos, 2 médios, 2 baixos), cúpula inclinada à frente.

## Construção (hard-surface MT3 puro)
- **Cúpula:** vidro com armação de 8 nervuras de aço e frisos de parafusos.
- **Cérebro:** malha orgânica com sulcos e linhas de circuito em relevo.
- **Colar:** anel de grafite com 6 conectores de onde saem os braços.
- **Tronco:** 4 módulos empilhados com painel chanfrado, grelhas de ventilação, LEDs curtos, número de série, cabos entre módulos.
- **Braços:** 8–10 segmentos em vértebra mecânica afinando; mão com 3 garras finas e 1 sensor; 1 braço com soldador (Glow ciano) e 1 com lente/scanner.
- **Coroa:** 3 antenas de alturas diferentes, 2 pratos de satélite, 1 mastro com anel holográfico.
- **Base:** anel de propulsão com 8 bocais e faixa de aviso.

## Paleta (3 tons + destaque)
| Papel | Hex | Onde |
| --- | --- | --- |
| Claro | `C8D0DC` aço claro | armação, segmentos dos braços |
| Médio | `2A3A8A` azul-navy vivo | painéis, anéis dos braços |
| Escuro | `2E3440` grafite | módulos, colar |
| Destaque (Glow) | `FF4AD0` magenta (cérebro); `3CF0FF` ciano (juntas, LEDs, propulsor) | focos 1 e 2 |
| Vidro (Spirit) | `AEEBFF`, Transparency 0,45 | cúpula, anel holográfico |
| Acento | faixa de aviso `F2C230` + `1A1A1A` | anel de propulsão |

## Olhos
Sem olhos por design: o foco é o **cérebro**. Nada de olhos de desenho.

## Detalhes-assinatura
- "Ω-00" no módulo principal.
- Rachadura na cúpula, remendada com placa parafusada, à esquerda.
- Um braço de outra cor (reaproveitado).

## Efeitos e aura (Mythic)
- Ambiente: **exclusivo `data_stream`** (bits 0/1 subindo do tronco até a cúpula); **exclusivo `thruster_glow`** (cone ciano para baixo + grade hexagonal girando no chão); `core_pulse` magenta no cérebro; faíscas no soldador a cada 4 s; acento rosa Mythic no cérebro. 8 emissores + 10 beams + 1 luz.
- Ação **Override**: braços recolhem e o cérebro pulsa rápido → onda de glitch radial, scanline de cima para baixo e faíscas dos 6 braços → bits caindo.

## Animação
Idle 4,5 s (paira, braços ondulam em defasagem, cérebro pulsa, pratos giram) · Fly 2,4 s (inclina à frente, braços para trás) · Happy 2,5 s (6 braços giram em leque) · Override 2,8 s (fx em 0,6 s).

## Proibições e aceitação
- Lê como IA-chefe (cúpula com cérebro + braços), irmão visual do Mecha Titan.
- Nada de água-viva fofa, topo rosa amorfo, braços de tubo liso ou olhos de desenho.
- A 64 px: bola de vidro com cérebro magenta + 6 braços em leque.

## Referências a reusar
`AIOverlord_alvo-2d` (meta), `AIOverlord_render-atual` (malha e rig quase finais), `MechaTitan_referencia`, seção 2 de `fichas-originais/ficha-L4-CyberCity.md`.
