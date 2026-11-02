---
area: modelos
tipo: ficha-de-remake
resumo: Remake da Sky Whale (Legendary, SkyKingdom) — jubarte do céu com casco de placas de mármore com filete de ouro, ventre azul-real sulcado, tubérculos dourados e nadadeiras longas em lâminas; nada nas costas.
termos: sky whale baleia do ceu skykingdom legendary jubarte marmore ouro azul real nuvens sem cidadela royal skywhale remake
---
# Sky Whale

**SkyKingdom · Legendary · gait `swim` (flutua no ar) · comprimento base 7,6 · altura ~3,6 · corpo a 1,2**

![[Recursos/Pets lendarios e miticos/SkyWhale_alvo-2d.webp|300]] ![[Recursos/Pets lendarios e miticos/SkyWhale_render-atual.webp|300]]

## Em uma frase
Uma jubarte majestosa e calma navegando nas nuvens: dorso de lajes de mármore branco com molduras de ouro, ventre azul-real com sulcos, fileira de rosetas douradas no rostro, nadadeiras peitorais enormes em lâminas e uma cauda grande em leque. **Nada em cima das costas.**

## Regra fixa do luks (22/10)
**Sem cidadela, crista, jardim, halo ou qualquer objeto nas costas.** No máximo uma barbatana dorsal baixa de jubarte. Vale também para o remake.

## O que mudar em relação ao render atual
- **Comprimento e elegância:** o render ficou curto e atarracado (corpo em bloco, cauda pequena e reta). O alvo é **longo, em gota afunilada**, com a cauda erguida em curva e o fluke largo (2,4).
- **Peitorais** mais longas (40% do comprimento, envergadura 6,4) e com lâminas separadas e afiladas, como no alvo.
- **Ventre azul-real** com sulcos bem marcados (14 placas) indo da mandíbula até o meio do corpo.
- **Nuvens** cartoon sob a barriga e atrás da cauda (Spirit), como no alvo.
- **Olho:** pequeno e sábio, âmbar com aro de ouro e sobrancelha de friso (faltava na auditoria de olhos).

## Silhueta e proporções
- 3 formas-chave: **corpo de jubarte com ventre sulcado** e cabeça maciça, **peitorais enormes em lâminas**, **fluke grande erguido**.
- Cabeça 30% do comprimento; maior altura 2,0 no terço anterior; pedúnculo Ø 0,5.
- Pose: flutuando, inclinada 10° para cima, peitorais em planeio.

## Anatomia e construção
- Núcleo de jubarte real (cabeça larga e achatada, mandíbula saliente, gota afunilando).
- **Dorso:** placas de mármore em escudo sobrepostas para trás, borda de friso dourado; maiores no dorso, menores nos flancos.
- **Ventre:** 14 placas longas de porcelana azul (sulcos) com frestas mais escuras.
- **Rostro:** 8 rosetas douradas em fileira (tubérculos).
- **Peitorais:** 7 lâminas longas de mármore afilando, borda frontal com escalope, filete dourado, pontas azul-real.
- **Fluke:** 2 lobos com borda serrilhada, mesmas lâminas.

## Paleta (3 tons + destaque)
| Papel | Hex | Onde |
| --- | --- | --- |
| Claro | `F2F0E8` mármore (veios `D8D4CC`) | dorso, peitorais, fluke |
| Médio | `2A5ACC` azul-real vivo | ventre, faixa lateral, lado de baixo das lâminas |
| Escuro | `1A2E66` | frestas dos sulcos, sombra |
| Metal | `E8B83A` ouro-sol | molduras, rosetas, olho |
| Destaque (Glow) | `9AD8FF` céu; `FFE58A` sol | sulcos do ventre, espiráculo, pontas das peitorais |

Azul-real em ≥ 25% da superfície (antídoto contra "bolo de noiva" branco).

## Olhos
Pequeno, âmbar `FFB830` com pupila escura e aro de ouro, sob sobrancelha de friso. Deve aparecer a 128 px na lateral da cabeça.

## Detalhes-assinatura
Cicatriz de arpão: 3 placas do flanco esquerdo trincadas e remendadas com grampos de ouro.

## Efeitos e aura (Legendary)
- Ambiente: **exclusivo `cloud_wake`** (nuvens cartoon atrás do fluke, 1,2/s); **exclusivo `blow_spray`** (jato de nuvem pelo espiráculo a cada 6 s); `core_pulse` céu nos sulcos. 4 emissores + 1 luz.
- Ação **Song**: cabeça sobe e os sulcos escurecem → 3 anéis sonoros dourados à frente e raios de sol do espiráculo → penas de luz caindo.

## Animação
Idle 5,0 s (ondulação lenta, peitorais remam, sobe e desce 0,2) · Swim 3,0 s · Happy 3,0 s (rolamento de 360°) · Song 2,8 s (fx em 0,6 s).

## Proibições e aceitação
- Lê como jubarte (sulcos, peitorais longas, tubérculos), nunca dirigível ou baleia genérica.
- Sem casco de barco literal, hélice, janela de avião ou mármore sem contraste.
- A 64 px: gota branca com barriga azul + 2 asas longas.

## Trabalho relacionado
A pasta do projeto tem os modelos **Royal Skywhale v2–v4** (`royal-skywhale-v4.glb` e previews), com placas hexagonais de mármore e ouro. Eles servem de referência de acabamento de placa com moldura de ouro, mas **têm um halo em cima da cabeça**, que viola a regra "nada nas costas". Não copiar o halo.

## Referências a reusar
`SkyWhale_alvo-2d` (meta), `SkyWhale_render-atual` (rig), `royal-skywhale-v4-preview.jpg` (acabamento das placas), seção 1 de `fichas-originais/ficha-L4-SkyKingdom.md`.
