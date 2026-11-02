---
area: modelos
tipo: decisao
resumo: Decisão de 31/10/2026 — os 21 pets Lendários e Míticos do Climb for Pets são refeitos no nível de qualidade dos pets do Steal An Egg do repositório, que substitui o alvo 2D e o MechaTitan v3 como régua; define lotes por área, o que conta como pronto e como comparar.
termos: regua steal an egg sae nivel qualidade 21 pets lendarios miticos climb for pets lote area goal remake decisao substitui alvo 2d mechatitan
---
# Régua Steal An Egg para os 21 pets

**Decisão do usuário (luks), 31/10/2026:** os 21 pets Lendários e Míticos das áreas 4–10 ficam no **mesmo nível de qualidade dos pets do Steal An Egg** registrados neste repositório. Essa régua **substitui tudo** o que valia antes para o visual deles.

## Imagens-alvo finais (decisão do usuário, 31/10/2026)

O usuário mandou as **22 imagens finais** dos pets, geradas no ChatGPT com os [[Prompts de imagem de referencia dos 21 pets]], e pediu: **"quero que o resultado seja extremamente parecido com as imagens"**. Elas estão em `Recursos/Pets lendarios e miticos/Alvos finais/`, em 1254×1254 px, com o nome `NN_Nome_Do_Pet.webp`.

- **Cada pet tem que ficar extremamente parecido com a sua imagem-alvo.** Isso é o critério 7 abaixo e vale por cima de tudo: forma, pose, proporções, peças, cores, onde brilha, superfície (blocos, studs, facetas) e rosto vêm da imagem.
- O nível do Steal An Egg (critérios 1 a 6) continua como **piso de qualidade**. Se um critério de 1 a 6 pedir algo diferente da imagem-alvo (por exemplo, outra paleta), **vale a imagem**. O revisor anota o conflito em vez de dar PIOR por ele.
- As imagens substituem como referência de forma a "forma aprovada" do Molten Dragon (`MoltenDragon_forma-chatgpt_2026-10-31.png`) e o v3 do Black Hole Cat.
- **Sugar Phoenix ou Sugar Unicorn:** há duas imagens para o Legendary da CandyLand, `08_Sugar_Phoenix` e `22_Sugar_Unicorn_Alternativa`. O usuário escolhe no começo do lote 3. Até lá, vale a 08.

## O que deixa de valer

- Os **alvos 2D** (`Recursos/Pets lendarios e miticos/<Pet>_alvo-2d.webp`) e o **MechaTitan v3** como meta visual, incluindo as regras R1–R10 do plano da Leva 4 e as "decisões em aberto" sobre o visual na [[00 Remake dos pets lendarios e miticos]].
- O "visual travado" do Lava Titan também entra na régua nova.
- As fichas de cada pet continuam úteis só para o que **não é visual**: nome, espécie, área, raridade, gait, clipes e pontos de efeito.

## O que continua valendo (limites do jogo, não estilo)

- Nome, espécie, área e raridade de cada pet, como estão no jogo.
- Limites técnicos: até 20 000 triângulos por malha, texturas até 1024², pivô no chão, 1 unidade = 1 stud.
- Escala no jogo por raridade (Legendary ×1,6, Mythic ×2,0) e o orçamento de VFX por raridade da nota de índice.
- Clipes mínimos: Idle, Walk/Fly/Swim, Happy e 1 especial, em loop sem salto.
- [[Modelo 3D a partir de imagem]] e [[VFX do HTML para o Roblox]] para o como fazer.

## A régua

Referências: [[Steal An Egg pets recentes]] (imagens em `Recursos/Referencias de pets raros/Steal An Egg - pets recentes/`), [[Steal An Egg mutacoes]], [[Raridade comparada entre jogos]].

**Mapa de raridade proposto (decisão reversível):** no Climb for Pets, Legendary e Mythic são o topo do jogo. Por isso:

| Climb for Pets | Degrau do Steal An Egg | Pets de comparação no repositório |
| --- | --- | --- |
| Legendary | Alto (Secret, Eternal) | Graveyard Brute, BloodBloom, Abomination Kong, Pumpkin Golem, Grave Cerberus, Phantom Dragon, Pumpkin Brute |
| Mythic | Topo (Divine) | Voidseer Pumpkin, Bone Emperor, Cursed Monarch |

**"Mesmo nível de qualidade" quer dizer, para cada pet:**

1. **Lado a lado com os pets de comparação do seu degrau, não destoa:** nem mais simples, nem mais carregado, nem com outro estilo.
2. **Lado a lado com os outros pets já feitos, também não destoa:** mesma densidade de detalhe, mesmo traço e mesmos materiais em todos os 21.
3. **Escada de raridade igual em todas as áreas.** O Legendary tem corpo maior e mais largo, com fissuras ou veias brilhando numa cor forte. O Mythic tem tudo isso e mais coroa, asas ou chifres dourados e uma peça ou chama em volta.
4. **Brilho só onde importa:** corpo fosco, brilho numa única cor forte, e rosto com dois olhos brilhantes bem legíveis (ou um ponto de luz quando o pet não tem rosto).
5. **Paleta da área:** os 3 pets da mesma área se reconhecem pela cor antes da forma.
6. **Legível no tamanho do inventário:** ícone de 128 px com silhueta e olhos reconhecíveis.
7. **Fiel à imagem-alvo** (o critério principal). Na faixa "ALVO x RESULTADO" da folha, a mesma vista de 3/4 lado a lado com a imagem-alvo, o pet é reconhecido **sem hesitar como a mesma criatura** nestas seis coisas:
   - pose e silhueta;
   - proporções (cabeça, corpo, membros, asas, cauda);
   - todas as peças da imagem, no mesmo lugar: coroa, anéis, chifres, espinhos, garras, acessórios;
   - cores e onde brilha;
   - superfície: blocos, studs, facetas, placas;
   - rosto e olhos.

   Só existem dois vereditos aqui. **IGUAL** quando não há nenhuma diferença visível nessas seis coisas. **PIOR** quando há qualquer diferença visível, e o revisor diz qual parte e o que ela tem na imagem. MELHOR não se aplica: ficar diferente da imagem nunca é melhor.

Os pets do Steal An Egg são **referência de nível, não molde**. Nada de copiar a forma, o nome ou o desenho de um pet deles.

Cuidado: muitas imagens do Steal An Egg são ilustrações do site, não renders do jogo (ver a nota de origem). Os renders 3D mais confiáveis são Candy Corn, Hollow Bat, Scarecrow, Pumpkin Golem e Soul Phantom.

## Verificação honesta (obrigatória para cada pet)

**1. Tirar o screenshot.** O preferido é o **Roblox Studio**: importar o GLB num place de teste e tirar o print com `screen_capture`, de frente, a 3/4 e de lado, com a iluminação padrão do jogo. Sem acesso ao Studio, usar um render do Blender, e a folha marca "render do Blender (não é o jogo)". O fundo deve ser neutro e o pet deve ocupar a maior parte do quadro, sem efeitos ligados. Fazer uma segunda folha com os efeitos ligados.

**2. Montar a folha de comparação** (a partir de `jogos/`):

```
python .framework/comparar.py --pet "<Pet>" --raridade legendary|mythic \
    --imagens frente.png tres_quartos.png lado.png --lote <outros pets do lote> \
    --origem studio|blender --saida "Recursos/Pets lendarios e miticos/<Pet>/<Pet>_comparacao.png"
```

A folha põe o pet, os 3 pets do Steal An Egg do degrau e os outros pets do lote no mesmo fundo e na mesma altura, e repete todos em 128 px sobre fundo claro e escuro.

**3. Pedir o veredito a um revisor que não fez o pet.** O revisor recebe só a folha e esta nota, sem a opinião de quem fez o pet. Ele abre a imagem (Read) antes de responder e preenche, para cada critério de 1 a 7 da régua:

| Critério | Veredito | Comparado com | O que se vê na folha |
| --- | --- | --- | --- |
| 1 Nível do degrau | MELHOR / IGUAL / PIOR | nome do pet SAE | detalhe concreto e visível |
| … | | | |

Regras do veredito:

- **APROVADO só se nenhum critério for PIOR** (de 1 a 7). Qualquer PIOR reprova o pet, com a correção que falta.
- **Na dúvida, é PIOR.** IGUAL precisa de um motivo visível tão bom quanto o do SAE. MELHOR precisa apontar o que supera, e onde.
- Toda linha cita um pet SAE específico e algo que se vê na imagem. Frases genéricas como "bom acabamento" não valem.
- Sem a imagem aberta não há veredito. Se a folha estiver cortada, escura ou pequena demais para julgar, a resposta é "INCONCLUSIVO — refazer a folha", nunca APROVADO.
- Diga com franqueza onde o SAE é melhor, mesmo que o pet tenha sido aprovado.
- O veredito vai para a nota do lote junto com a folha. O usuário aprova o lote olhando as folhas, não o veredito.

### Como corrigir um PIOR (regra do usuário, 31/10/2026)

Um PIOR não se corrige mexendo só no que já existe. Quem faz o pet olha o pet inteiro ao lado do SAE citado e escreve por que aquela parte está pior. Toda correção de PIOR **muda a forma** da parte que está pior (cabeça, corpo, asas, proporção, volume, silhueta); trocar só cor, tom, profundidade do laranja ou brilho não conta. Para a parte pior, testar **pelo menos duas formas diferentes** e escolher na folha, sem ficar no estilo atual só porque ele tem menos PIOR. A entrega registra o motivo, as formas testadas e a escolhida. Texto completo na nota [[Lote 1 Volcano - pets lendarios e miticos]].

## Lotes (aprovação do usuário por lote)

Uma área por lote, nesta ordem, 3 pets por lote:

| Lote | Área | Pets |
| --- | --- | --- |
| 1 | Volcano | Volcanic Phoenix (L), Lava Titan (L), Molten Dragon (M) |
| 2 | CoralReef | Pearl Seahorse (L), Kraken (L), Leviathan (M) |
| 3 | CandyLand | Gingerbread Golem (L), Sugar Phoenix (L), Sprinkle Dragon (M) |
| 4 | Haunted | Headless Horse (L), Banshee (L), Lich King (M) |
| 5 | SkyKingdom | Sky Whale (L), Seraph (L), Sky Emperor (M) |
| 6 | CyberCity | Quantum Cat (L), Mecha Titan (L), AI Overlord (M) |
| 7 | Cosmos | Black Hole Cat (L), Celestial Whale (L), Cosmic Deity (M) |

## Pronto para aprovar um lote

Cada pet do lote tem:

- um **GLB** exportado, dentro dos limites, com rig e os 4 clipes;
- **texturas de VFX** (flipbooks) e a lista de emissores, dentro do orçamento da raridade;
- **renders** de frente, 3/4 e lado, mais o ícone de 128 px;
- a **folha de comparação** feita com `comparar.py` a partir de screenshots (ver Verificação honesta), sem efeitos e com efeitos;
- a tabela de veredito do revisor independente, com **APROVADO** (nenhum critério PIOR).

Para o lote todo:

- a **nota do lote** em `jogos/19 Projeto em andamento/` com a folha de comparação e os vereditos;
- arquivos e scripts em `jogos/Recursos/Pets lendarios e miticos/<Pet>/`;
- **um pull request** com tudo isso, e o trabalho para aqui até o usuário aprovar.

## Processo rápido (decisão do usuário, 31/10/2026)

As rodadas seguem a nota [[Processo rapido de rodada]], que vale por cima dos passos acima onde eles diferem:

- **Rodar até APROVADO**, sem parar por contagem de rodadas; se o mesmo critério ficar PIOR por 3 rodadas seguidas, trocar de abordagem naquela parte (regra de platô).
- **Uma rodada num comando:** `python .framework/rodada.py --pet "<Pet>" --rodada N [--variantes A B] [--pior 1,6]` (build, render, checagem e folha).
- **Render e ícone do kit único** (`render_pet.py`): mesma câmera e luz para todos os pets; ícone padrão em 3/4 de frente, pet inteiro ocupando 88% do quadro, sem halo.
- **Checagem automática** (`checar.py`) antes do revisor; uma rodada barrada não vai ao revisor.
- **Banca de 3 revisores** com maioria por critério (`banca.py`) e âncoras; critério cuja parte não mudou fica travado; a folha de cada rodada já traz o lote e vale como conferência.

## Conexoes

[[00 Remake dos pets lendarios e miticos]] · [[Processo rapido de rodada]] · [[Prompts de imagem de referencia dos 21 pets]] · [[Steal An Egg pets recentes]] · [[Raridade comparada entre jogos]] · [[Climb for Pets]]
