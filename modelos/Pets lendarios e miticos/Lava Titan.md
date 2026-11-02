---
area: modelos
tipo: ficha-de-remake
resumo: Remake do Lava Titan (Legendary, Volcano) — titã-gorila de crosta de basalto rachada sobre magma, com colunas hexagonais e cristais de obsidiana altos nos ombros. Visual travado pelo luks; o remake é só de valor e brilho.
termos: lava titan titã de lava volcano legendary gorila basalto colunar magma cristais obsidiana travado remake
---
# Lava Titan

**Volcano · Legendary · gait `ground` · altura base 5,6 (topo dos cristais) · largura ≤ 4,4**

![[Recursos/Pets lendarios e miticos/LavaTitan_alvo-2d.webp|300]] ![[Recursos/Pets lendarios e miticos/LavaTitan_render-atual.webp|300]]

## Remake v3 (31/10/2026, régua Steal An Egg)

O visual agora segue a [[Regua Steal An Egg para os 21 pets]], que substitui o "visual travado" abaixo para o que for visual. O v3 manteve cristais altos, estrela, cratera, coluna partida e placa caída, e ficou mais largo, com fendas laranja contínuas e olhos maiores. Arquivos, números e prints em `Recursos/Pets lendarios e miticos/Lava Titan/` ([[entrega]] e [[emissores]]).

## Em uma frase
Um brutamonte calmo de rocha vulcânica: crosta cinza rachada em placas poligonais, magma vivo nas fendas, uma estrela de fogo no peito e uma floresta de cristais pretos pontudos nos ombros.

## Visual travado
O luks gosta do visual **pontudo, com cristais altos**. A forma do render atual fica. O remake mexe em **valor, brilho e olhos**, não na silhueta.

## O que mudar em relação ao render atual
- **Rocha mais clara:** o alvo usa cinza-pedra `7A7472` nos topos das placas; o render está quase preto. Subir os topos para o valor do alvo e manter as laterais escuras (3 tons).
- **Magma mais vivo e mais largo:** as fendas no alvo são uma rede contínua laranja-vermelha com núcleo amarelo, visível no corpo todo. No render são riscos finos e esparsos. Alargar as fendas visíveis (0,06–0,1) e pintar o fundo em magma, sem virar tracejado reto.
- **Estrela do peito** maior e mais brilhante (é o foco 1).
- **Olhos:** 2 fendas em V cor de fornalha (pedido da rodada E), fundas sob a testa de rocha.

## Silhueta e proporções
- 3 formas-chave: **trapézio enorme de ombros e costas** com cristais, **antebraços muito maiores que os braços** com punhos no chão, **pernas curtas e grossas**.
- Ombro = 2× o quadril; antebraço Ø 1,0, braço Ø 0,7; perna Ø 0,8.
- Pose: curvado, nós dos dedos apoiados à frente (gorila), cabeça baixa entre os ombros.

## Anatomia e construção
- Núcleo de gorila em magma escuro, coberto por **placas de crosta poligonais irregulares** (5–7 lados, 0,25–0,6), maiores nas costas e ombros. Não são tijolos.
- **Ombros e costas:** aglomerados de 7–12 colunas hexagonais de alturas variadas + **3–5 cristais de obsidiana altos e pontudos** (a assinatura que o luks aprovou).
- **Peito:** placa dupla com fenda em **estrela de 5 pontas** e a fornalha dentro.
- **Cabeça:** pequena e afundada, mandíbula pesada saliente, testa em aba, 2 chifres curtos de obsidiana.
- **Costas:** cone de cratera entre as escápulas com magma dentro.
- **Mãos:** 4 dedos grossos, nós de basalto colunar. **Pés:** largos, 3 dedos.

## Paleta (3 tons + destaque)
| Papel | Hex | Onde |
| --- | --- | --- |
| Claro | `7A7472` | topo das placas de crosta, topo das colunas |
| Médio | `4A403D` | faces das placas |
| Escuro | `2B2526` | laterais das colunas, fundo entre placas |
| Destaque (Glow) | `FF4A10` → `FF9A1E` → `FFD040` | fendas, estrela do peito, cratera, olhos |
| Acento | `15121A` obsidiana com highlight `4A3A5A` | cristais, chifres, unhas |

## Olhos
Duas fendas em V inclinadas para dentro (cara de bravo calmo), Glow `FFC040` com borda `FF7A1E`, sob a aba da testa.

## Detalhes-assinatura
- Coluna partida no ombro **direito**.
- Placa de crosta caída no antebraço **esquerdo**, mostrando mais magma.

## Efeitos e aura (Legendary)
- Ambiente: **exclusivo `crater_smoke`** (fumaça da cratera, 1,2/s); **exclusivo `magma_drip`** (gotas dos punhos, 0,4/s); `core_pulse` lento de 2,0 s no peito (respiração). 4 emissores + 1 luz (cratera).
- Acento dourado de raridade: brilho mais quente na estrela do peito.
- Ação **Slam**: ergue os punhos e o magma brilha +50% → punhos no chão, anel de choque laranja e 16 lascas de rocha → poeira rolando.

## Animação
Idle 3,5 s (respiração pesada, ombros sobem) · Walk 2,0 s (knuckle-walk) · Happy 2,5 s (bate no peito 3×, a estrela pisca) · Slam 2,2 s (fx em 0,5 s).

## Proibições e aceitação
- Ninguém pode ler "tijolos" ou "pneus". Nada de placas retangulares em fileira nem anéis nos membros.
- Glow nunca em traço reto tracejado.
- A 64 px: cristais pretos no topo + rede laranja + estrela no peito.

## Referências a reusar
`LavaTitan_alvo-2d` (meta de cor), `LavaTitan_render-atual` (forma aprovada, reaproveitar malha e rig), seção 2 de `fichas-originais/ficha-L4-Volcano.md`.
