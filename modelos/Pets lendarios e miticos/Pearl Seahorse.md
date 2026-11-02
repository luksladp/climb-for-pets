---
area: modelos
tipo: ficha-de-remake
resumo: Remake do Pearl Seahorse (Legendary, CoralReef) — cavalo-marinho joia art nouveau de nácar iridescente com filetes de ouro, coroa com pérolas e uma pérola grande engastada no peito.
termos: pearl seahorse cavalo marinho perola coralreef legendary nacar iridescente ouro coroa joia art nouveau remake
---
# Pearl Seahorse

**CoralReef · Legendary · gait `swim` · altura base 4,8 (corpo de 1,0 a 4,8) · largura ≤ 1,6**

![[Recursos/Pets lendarios e miticos/PearlSeahorse_alvo-2d.webp|300]] ![[Recursos/Pets lendarios e miticos/PearlSeahorse_render-atual.webp|300]]

## Em uma frase
Um cavalo-marinho tratado como joia: placas de madrepérola que mudam de rosa para azul, molduras de ouro em curvas art nouveau, uma pérola enorme presa no peito por garras de ouro e uma coroa. É o pet mais delicado e elegante do jogo. Personalidade aristocrática e serena.

## O que mudar em relação ao render atual
- **Iridescência:** o render é branco-acinzentado e chapado. O alvo tem nácar com **manchas grandes de rosa, lilás, azul-gelo e menta** em cada placa. Pintar as manchas grandes (não ruído fino).
- **Ouro mais presente:** filete de ouro contínuo em toda placa e volutas grossas segurando a pérola, como no alvo.
- **Barbatanas:** no alvo são leques turquesa vivos (`5FE0F0`) na nuca e nas costas; no render quase somem. Aumentar e saturar.
- **Cauda em espiral** mais grossa e com o caracol bem fechado (1,5 volta), legível de frente.
- **Olho** maior, azul-turquesa com aro de ouro.

## Decisão em aberto: coroa de ouro ou de coral
- A ficha pede **coronet de coral ramificado** (é o que está no render, em vermelho).
- O alvo 2D mostra **coroa de ouro com pérolas** nas pontas.
- **Recomendo a coroa de ouro com pérolas do alvo**, com 1 ramo de coral pequeno saindo de um lado como marca de identidade. Lê melhor como "Legendary joia" e combina com a pérola do peito.

## Silhueta e proporções
- 3 formas-chave: **S vertical** (cabeça a 90° do pescoço, barriga saliente à frente, costas arqueadas), **focinho tubular longo**, **cauda em espiral**.
- Cabeça 0,9 (focinho 0,55); tronco 1,3 de largura e 1,6 de profundidade na barriga; cauda Ø 0,5 → 0,08.
- Pose: ereto, levemente inclinado à frente, focinho para baixo.

## Anatomia e construção
- Núcleo com seção em D (barriga redonda à frente, quilha atrás).
- **Placas por segmento:** 11 no tronco e ~30 na cauda, 4 placas por segmento (dorsal, 2 laterais, ventral), contorno de escudo curvo, sobrepostas, seguindo a curva. Junções com crista de ouro e espinho curto.
- **Barriga:** placas ventrais maiores, como peitoral de nácar, com a pérola.
- **Focinho:** 3 cristas orgânicas irregulares, boca pequena em fenda.
- **Barbatana dorsal:** leque de 12 raios curvos com membrana translúcida turquesa. Peitorais em leque atrás da cabeça.
- **Pérola do peito:** Ø 0,55, rosa-creme, em 4 garras de ouro em voluta.

## Paleta (3 tons + destaque)
| Papel | Hex | Onde |
| --- | --- | --- |
| Claro | `F7F0EC` nácar com manchas `F2C8DC` (rosa), `C8E4F4` (azul), `D8F0E4` (menta) | placas |
| Médio | `D6B46A` ouro-areia | filetes, volutas, coroa, cristas |
| Escuro | `8A6A3A` ouro sombreado + `B89A9A` pele entre placas | frestas e sombras (nunca cinza de máquina) |
| Destaque (Glow) | `FFE6B0` pérola quente; `3CF0FF` bio no aro do olho | pérola, pérolas da coroa, olhos |
| Spirit | `5FE0F0` turquesa, Transparency 0,35 | membranas das barbatanas |

## Olhos
Grande para o corpo mas sério: íris turquesa, pupila escura, brilho branco, aro de ouro e sobrancelha com 3 espinhos. Precisa ler a 128 px de perfil e de 3/4.

## Detalhes-assinatura
- Uma placa lateral do tronco é de coral escuro (coral crescendo sobre ela).
- A voluta de ouro superior da pérola é maior (floreio assimétrico).

## Efeitos e aura (Legendary)
- Ambiente: **exclusivo `pearl_shine`** (pulso pérola a cada 2 s + flash de joia `star4` a cada 4 s); **exclusivo `iridescent_bubbles`** (bolhas iridescentes do focinho, 0,8/s); `sparkle` dourado na coroa. 4 emissores + 1 luz (pérola).
- Ação **Shine**: cauda se enrola e a pérola escurece → flash de pérola com halo de nácar e 12 estrelas → bolhas e brilho caindo.

## Animação
Idle 3,5 s (sobe e desce 0,15, dorsal vibra rápido, cauda abre e fecha) · Swim 2,0 s (ereto, dorsal batendo) · Happy 2,5 s (giro vertical, cauda desenrola) · Shine 2,0 s (fx em 0,5 s).

## Proibições e aceitação
- Lê como cavalo-marinho de verdade (barriga e S claros), nunca "mola de anéis empilhados".
- Sem parafusos, LED reto ou anéis de máquina (proibido na área toda).
- A 64 px: S rosado-perolado + pérola brilhando + coroa.

## Referências a reusar
`PearlSeahorse_alvo-2d` (meta), `PearlSeahorse_render-atual` (malha e rig aproveitáveis), seção 1 de `fichas-originais/ficha-L4-CoralReef.md`.
