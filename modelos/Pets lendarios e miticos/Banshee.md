---
area: modelos
tipo: ficha-de-remake
resumo: Remake da Banshee (Legendary, Haunted, ainda fora do jogo) — espectro de mortalha rasgada cinza-azulada, máscara de crânio gritando, gaiola-lanterna no peito com alma e cauda de ectoplasma turquesa.
termos: banshee espectro fantasma haunted legendary mortalha mascara cranio grito gaiola alma ectoplasma turquesa correntes remake
---
# Banshee

**Haunted · Legendary · gait `fly` · altura base 5,2 (base a 0,8) · largura ~3,4 com os braços**

![[Recursos/Pets lendarios e miticos/Banshee_alvo-2d.webp|300]] ![[Recursos/Pets lendarios e miticos/Banshee_render-atual.webp|300]]

## Em uma frase
Um espectro trágico e sem peso: capuz rasgado com coroa de espinhos, máscara de crânio alongada com a boca escancarada no grito, mãos de osso erguidas com algemas e correntes, uma gaiola-lanterna no peito prendendo uma alma, e da cintura para baixo uma cascata de ectoplasma turquesa. **Ainda não está no jogo** (área Haunted sem `Config`).

## O que mudar em relação ao render atual
- **Cor da mortalha:** o render é roxo-escuro e quase preto. O alvo é **cinza-azulado claro com sombras lilás**, e o ectoplasma turquesa domina a metade de baixo. Seguir o alvo e deixar o roxo da área só no forro e nas bordas.
- **Ectoplasma grande:** no alvo a barra se dissolve em **lâminas de chama turquesa longas** (quase metade da altura) que também saem das mangas. No render são poucas pontas pequenas.
- **Olhos e boca brilhando:** órbitas com Glow turquesa forte e brilho dentro da boca, como no alvo.
- **Gaiola-lanterna** no peito com alma turquesa bem visível e correntes ligando aos punhos.
- **Mangas largas e rasgadas** abrindo do cotovelo (no render estão estreitas).

## Silhueta e proporções
- 3 formas-chave: **capuz alto em arco pontudo com a coroa de espinhos**, **sino da mortalha** abrindo para baixo (2,6 na barra) que vira ectoplasma, **braços longos erguidos** com mangas pendentes.
- Ombros mais estreitos que o capuz; máscara 0,7 de altura (oval vertical); braços 1,8; dedos 0,4.
- Pose: flutuando, inclinada à frente, braços meio erguidos com dedos abertos (lamento).

## Anatomia e construção
- Núcleo: torso esquelético fino e braços de osso, quase todo coberto.
- **Capuz:** 5–6 lâminas de tecido rígido com vincos de aresta, abertura facial em ogiva, borda rasgada; coroa de ferro com 7 espinhos e joia roxa.
- **Máscara:** crânio alongado com maçãs salientes, queixo fino, órbitas grandes e fundas, **boca em fenda vertical bem aberta** (o grito), rachaduras.
- **Mortalha:** 3 camadas de lâminas (ombro, cintura, barra), pontas rasgadas em tiras, comprimentos desiguais, borda prata gasta.
- **Mãos:** osso, 4 dedos longos, unhas pretas; algemas de ferro com correntes ligadas à gaiola (no alvo as correntes cruzam o peito).
- **Gaiola-relicário:** 6 barras góticas curvas, topo em ogiva, alma dentro.
- **Ectoplasma:** lâminas Spirit turquesa afunilando em pontas finas, com núcleo Glow.

## Paleta (3 tons + destaque)
| Papel | Hex | Onde |
| --- | --- | --- |
| Claro | `B8C4CC` (cinza-azulado com reflexo `D0E0E4`) | dobras altas da mortalha |
| Médio | `7A8494` com sombra lilás `6A5A82` | mortalha, capuz |
| Escuro | `3A3848` | interior do capuz, frestas |
| Osso | `D9CFB4` com AO `8A7A5A` | máscara, mãos |
| Destaque (Glow/Spirit) | `5FFFD8` turquesa, núcleo `C8FFF0` | órbitas, boca, alma, ectoplasma (Transparency 0,45) |
| Acento | ferro `3A3842`, prata `9A9AA6`, joia `C98BFF` | coroa, gaiola, algemas |

## Olhos
Órbitas grandes e fundas com Glow turquesa intenso e núcleo branco. São o foco 1 e precisam ler a 64 px dentro do capuz.

## Detalhes-assinatura
- Rachadura grande atravessando o olho esquerdo da máscara.
- Uma corrente partida (só 3 elos).

## Efeitos e aura (Legendary)
- Ambiente: **exclusivo `ecto_trail`** (fiapos de ectoplasma saindo da barra, 2/s); **exclusivo `soul_flicker`** (a alma bate na gaiola com flash a cada 5 s); `core_pulse` turquesa na alma (2,2 s). 4 emissores + 1 luz.
- Ação **Wail**: recua e fecha a boca → grito com 3 anéis de som distorcido em sequência e olhos piscando forte → fiapos em espiral.

## Animação
Idle 4,0 s (sobe e desce 0,2, lâminas ondulam com atraso, correntes balançam) · Fly 2,0 s (mortalha estica para trás) · Happy 2,5 s (gira rindo, cabeça para trás) · Wail 2,4 s (fx em 0,5 s).

## Proibições e aceitação
- Máscara é crânio oval, nunca bloco. Capuz em ogiva, nunca cápsula. Corpo em sino, nunca tubo.
- Nada de pano mole (cloth sim) nem rosto humano bonito.
- O grito lê a 30 studs. A 64 px: capuz cinza + olhos turquesa + cauda turquesa.

## Referências a reusar
`Banshee_alvo-2d` (meta, inclusive a mortalha cinza-azulada), seção 2 de `fichas-originais/ficha-L4-Haunted.md` (a cor de mortalha roxa da ficha fica substituída). Referência externa de leitura: Phantom Banshee do Steal An Egg em `Recursos/Referencias de pets raros/Steal An Egg - pets recentes/` (só estudo, não copiar).
