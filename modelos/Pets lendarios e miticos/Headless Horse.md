---
area: modelos
tipo: ficha-de-remake
resumo: Remake do Headless Horse (Legendary, Haunted) — cavalo de guerra sem cabeça em barda gótica de ferro com filetes de prata, chama espectral verde no lugar da cabeça, crina, cauda e cascos em fogo verde.
termos: headless horse cavalo sem cabeca haunted legendary barda gotica ferro prata chama espectral verde caveira remake
---
# Headless Horse

**Haunted · Legendary · gait `ground` · altura base 5,4 (topo da chama) · comprimento ≤ 6,6**

![[Recursos/Pets lendarios e miticos/HeadlessHorse_alvo-2d.webp|300]] ![[Recursos/Pets lendarios e miticos/HeadlessHorse_render-atual.webp|300]]

## Em uma frase
O cavalo de guerra do cavaleiro sem cabeça: corcel enorme coberto por barda gótica de ferro com filetes de prata, uma caveira de cavalo presa no peito e, no lugar da cabeça, uma labareda verde-fantasma saindo de uma gola de pontas. Crina, cauda e cascos também queimam em verde. Furioso e leal. **Ainda não está no jogo** (área Haunted sem `Config`).

## O que mudar em relação ao render atual
- **Fogo verde muito maior:** no alvo a chama do pescoço, a crina, a cauda e os 4 cascos são labaredas cheias e brilhantes (`5CFF9A`) que dominam a silhueta. No render são pequenas e pálidas. É a principal correção.
- **Pernas grossas de cavalo de guerra** (antebraço e gaskin Ø 0,4, cascos Ø 0,45). No render as canelas são finas.
- **Barda mais clara:** ferro azul-ardósia `4A4E5E` com highlight `8A90A6` e filete prata grosso; o render está preto. Bordas recortadas em pontas e lóbulos, como no alvo.
- **Caveira de cavalo no peito** maior e com olhos verdes brilhando (no alvo é um elemento claro e legível).
- **Sela** de couro marrom visível em cima, como no alvo.

## Silhueta e proporções
- 3 formas-chave: **pescoço curto, grosso e arqueado com a chama alta**, **tronco em barril** com peito largo e garupa forte, **pernas fortes com cascos em chamas**.
- Pescoço 25% mais curto que a v1; peito 1,4; barril 1,6 de profundidade.
- Pose: de pé em guarda, uma pata dianteira levemente erguida; chama inclinada para trás.

## Anatomia e construção
- Núcleo de cavalo real com corpo interno de osso: **costelas** aparecem nas frestas do flanco e **vértebras** no dorso.
- **Barda:** crinet de 6 lâminas no pescoço (borda em arco, fluting), peitoral com caveira em relevo e asas laterais recortadas, 2 placas por flanco abertas embaixo, garupa em escudo duplo com fluting radial. Ferrugem e lascas só nas bordas.
- **Gola:** anel gótico com 6 pontas para cima, de onde sai a chama.
- **Sela:** couro em placas com arções altos, estribos, manta roxa rasgada em lâminas.
- **Pernas:** joelho e jarrete ósseos, caneleiras de ferro na frente, cascos de ferro com ferradura e topo em osso.
- **Crina (7) e cauda (6):** lâminas de fogo espectral longas, núcleo Glow e camada externa Spirit.

## Paleta (3 tons + destaque)
| Papel | Hex | Onde |
| --- | --- | --- |
| Claro | `9A9AA6` prata-velha (highlight `C8C8D2`) | filetes, entalhes, pontas da gola |
| Médio | `4A4E5E` ferro | placas da barda |
| Escuro | `2A2A36` (nunca mais escuro em área grande) | frestas, fundo do fluting |
| Osso | `D9CFB4` com AO `8A7A5A` | costelas, caveira, topo dos cascos |
| Destaque (Glow) | `5CFF9A` núcleo `C8FFE0` | chama, crina, cauda, cascos, olhos da caveira |
| Acento | couro `5A3420`, manta `3B1F4F` | sela |

## Olhos
Sem olhos por design (não tem cabeça). O ponto de leitura de "rosto" é a **chama** + os **olhos verdes da caveira do peito**.

## Detalhes-assinatura
- Flecha quebrada cravada na placa do flanco esquerdo.
- Uma ponta da gola torta.

## Efeitos e aura (Legendary)
- Ambiente: **exclusivo `ghost_flame`** (chama verde no pescoço, Rate 6, inclinando para trás); **exclusivo `hoof_embers`** (brasa verde por casco); fiapos de ectoplasma saindo da crina. 6 emissores + 1 luz verde.
- Ação **Rear**: recua e a chama encolhe → patas descem, anel de fogo verde no chão e rajada de brasas → fiapos.

## Animação
Idle 3,5 s (raspa a pata, chama tremula, cauda balança) · Walk 1,6 s (passo de 4 tempos, crina flui) · Happy 2,5 s (empina, a chama explode para cima) · Rear 2,2 s (fx em 0,5 s).

## Proibições e aceitação
- Proporção de cavalo de guerra (nunca lhama ou girafa). Sem tubos retos nas pernas.
- Barda com recorte e filete prata visíveis; nada de placa lisa ou ferro chapado.
- A chama lê como fogo, nunca gema facetada.
- A 64 px: cavalo escuro-azulado com fogo verde em cima, atrás e nos pés.

## Referências a reusar
`HeadlessHorse_alvo-2d` (meta), `HeadlessHorse_render-atual` (rig e barda aproveitáveis), seção 1 de `fichas-originais/ficha-L4-Haunted.md`.
