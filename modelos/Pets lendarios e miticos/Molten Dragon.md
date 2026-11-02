---
area: modelos
tipo: ficha-de-remake
resumo: Remake do Molten Dragon (Mythic, Volcano) — dragão imperial de obsidiana com filigrana de ouro, rachaduras de magma e asas abertas de membrana de lava. Existe um conceito v2 mais claro e robusto.
termos: molten dragon dragao derretido volcano mythic obsidiana ouro magma asas lava coroa conceito v2 remake
---
# Molten Dragon

**Volcano · Mythic · gait `ground` · altura base 6,4 (topo dos chifres) · comprimento ≤ 9,0**

![[Recursos/Pets lendarios e miticos/MoltenDragon_alvo-2d.webp|300]] ![[Recursos/Pets lendarios e miticos/MoltenDragon_render-atual.webp|300]]

![[Recursos/Pets lendarios e miticos/MoltenDragon_conceito-v2.webp|420]]

Acima: alvo 2D, render atual e conceito v2.

## Em uma frase
O monarca da Volcano: dragão robusto de placas de obsidiana roxo-escuro com fendas de magma, asas abertas cuja membrana é lava, chifres de coroa com anéis de ouro e uma fornalha na garganta. É a peça mais luxuosa da área.

## O que mudar em relação ao render atual
É o pet com **maior distância entre alvo e render**.
- **Pescoço de girafa:** o render tem pescoço longo, fino e reto. O alvo tem pescoço **curto, grosso na base e em S**, com a cabeça na altura do ombro + 1,5.
- **Asas:** o render quase não tem asas. O alvo tem **asas abertas e erguidas** com membrana de **lava laranja-vermelha** e dedos de obsidiana. Elas são metade da silhueta.
- **Preto sobre preto:** subir o valor da obsidiana para roxo-escuro `3A2E4A` com highlight `5A4A70` nas arestas.
- **Rachaduras de magma** contínuas e largas no corpo todo (como no alvo), não só manchas.
- **Olhos:** amêndoa amarela (pedido da rodada E), Glow, bem marcada.

## Decisão em aberto: alvo 2D ou conceito v2?
O `MoltenDragon_conceito-v2` mostra outra leitura: corpo **lilás-acinzentado mais claro**, perfil de quadrúpede baixo e pesado (quase anquilossauro), **anéis de ouro** nas coxas e no dorso, faixa de magma na barriga, cauda em machado de lâmina dupla e asas fechadas em manto.
- **Recomendo** usar o **alvo 2D como forma** (asas abertas, dragão clássico, leitura de Mythic a 64 px) e o **conceito v2 como valor e ornamento** (lilás mais claro em vez de preto, anéis de ouro nas coxas, cauda em machado). Isso resolve o preto sobre preto sem perder as asas.
- Confirmar com o luks no portão A da thread do pet.

## Silhueta e proporções
- 3 formas-chave: **asas abertas em V** com membrana de lava, **pescoço em S com cabeça coroada**, **cauda longa com lâmina dupla** (machado).
- Pescoço 22–25% do comprimento (antes 28%), cauda 40%. Tórax profundo (2,2), largura 2,8. Patas dianteiras mais robustas, pegada Ø 0,7.
- Pose: em 4 patas, peito estufado, cabeça olhando à frente e para baixo, asas meio abertas para cima.

## Anatomia e construção
- Núcleo de dragão musculoso, afunilando até a cauda.
- **Dorso:** 13 espinhos-lâmina de obsidiana + 2 fileiras de escamas-placa em gota com **filete de ouro** na borda (R2).
- **Flancos:** escamas menores sem ouro. **Barriga:** 14 placas de basalto com fresta de magma.
- **Peito:** placa-escudo com filigrana de ouro em espiral, emoldurando a fornalha.
- **Cabeça:** focinho anguloso, sobrancelha pesada, 2 fileiras de dentes, narinas em fenda, **4 chifres** (2 grandes de 1,2 varrendo para trás com anéis de ouro, 2 pequenos), **coroa de 3 lâminas de ouro** com joia de magma.
- **Asas:** 4 dedos + polegar de obsidiana com garra de ouro; membrana em placas finas de lava (laranja `FF6E28` com veios amarelos `FFC040` seguindo os dedos), rachada como vitral.
- **Patas:** coxa e ombro musculosos, 4 garras de obsidiana com base de ouro.

## Paleta (3 tons + destaque)
| Papel | Hex | Onde |
| --- | --- | --- |
| Claro | `6A5A82` (highlight lilás; no conceito v2 até `8A7AA0`) | arestas e topos das escamas |
| Médio | `3A2E4A` | campo das escamas |
| Escuro | `221A2C` | frestas, barriga, sombra |
| Destaque (Glow) | `FF6E28` → `FFC040` | rachaduras, membrana, garganta, joia da coroa, olhos |
| Metal | `C9962E` ouro velho, bordas gastas `E0B85A` | filigrana, anéis, coroa, garras |

## Olhos
Amêndoa amarela `FFD040` Glow, pupila em fenda, sob sobrancelha de placa. A 128 px tem que ler como "dragão bravo olhando para você".

## Detalhes-assinatura
- Chifre grande esquerdo com 2 anéis de ouro, o direito com 1 (troféu).
- Uma escama dorsal do pescoço trocada por placa de ouro (cicatriz remendada).

## Efeitos e aura (Mythic)
- Ambiente: `aura` de chamas subindo de 4 pontos do dorso; **exclusivo `nostril_smoke`** (2 baforadas a cada 4 s); `sparkle` dourado na coroa; `core_pulse` na fornalha; acento rosa Mythic na joia da coroa. 7 emissores + 1 luz (garganta).
- Ação **Breath**: cabeça sobe e brasas são sugadas → cone de fogo (3 emissores escalonados) → fumaça e brasas caindo.

## Animação
Idle 4,0 s (respiração, baforada em 2,0 s, cauda varre, asas respiram) · Walk 1,8 s · Happy 3,0 s (abre as asas por completo e ruge para cima) · Breath 2,4 s (fx em 0,6 s).

## Proibições e aceitação
- Pescoço sem cara de girafa; pernas com músculo, nunca cascas de mecha.
- Membrana nunca opaca e chapada; veios visíveis.
- Sem mancha clara de bake no dorso. Sem preto sobre preto.
- A 64 px: asas laranja + silhueta de dragão + chifres.

## Referências a reusar
`MoltenDragon_alvo-2d` (forma), `MoltenDragon_conceito-v2` (valor e anéis), seção 3 de `fichas-originais/ficha-L4-Volcano.md`. O render atual serve só para o rig de 4 patas e cauda.
