---
area: modelos
tipo: decisao
resumo: Decisão de 31/10/2026 (aprovada pelo usuário) para chegar mais rápido a pets aprovados na régua Steal An Egg — rodar até aprovar com regra de platô, uma rodada num comando só (rodada.py), kit único de render e ícone (render_pet.py), checagem automática antes do revisor (checar.py), variantes em paralelo, banca de 3 revisores (banca.py), âncoras, um nível de revisão e uma branch por lote; com os números do lote 1 que motivaram cada mudança.
termos: processo rapido rodada velocidade revisor banca maioria ancoras plato variantes paralelo kit render icone padrao checagem automatica checar rodada.py render_pet.py banca.py forma mudou regra pior lote branch unica pr blender hook tempo por rodada
---
# Processo rápido de rodada

**Decisão do usuário (luks), 31/10/2026:** aprovou o plano "remakes dos pets mais rápidos". A prioridade é **velocidade com a mesma qualidade**: a régua, os 6 critérios, o "na dúvida, PIOR", o revisor que não fez o pet e o aviso "render do Blender (não é o jogo)" continuam iguais. O que muda é como a rodada é feita e julgada.

Vale para os 21 pets da [[Regua Steal An Egg para os 21 pets]], a partir das rodadas que começarem depois que esta nota estiver na `main`.

## Por que (números do lote 1 Volcano, rodadas 1 a 17)

Fonte: [[Lote 1 Volcano - pets lendarios e miticos]], commits das rodadas e threads do lote.

- **Espera, não trabalho.** Umas 12h45 de relógio para 17 rodadas, mas só umas 3h30 de trabalho. As threads pararam no limite de 80 turnos (rodada 3) e ficaram **8h53 paradas** depois da rodada 9, esperando autorização de mais rodadas.
- **Turnos demais por rodada.** Cerca de 25 turnos por rodada (montar, rig, 6 renders, ícone, folha, commit, mensagens).
- **Onde caem os PIOR** (93 PIOR em 41 vereditos, rodadas 6 a 17 e conferências): critério 1 nível 38%, 6 ícone 23%, 2 coerência 18%, 4 rosto 15%, 3 escada 4%, 5 paleta 2%. Ícone e coerência (41%) dependem mais de padronização do que de arte.
- **Revisores oscilam.** Rodada 8 → 9 do Lava Titan: mesmo modelo, outro revisor, de 1 para 2 PIOR. No ícone, a rodada 8 pediu "cabeça grande" e a 9 "pet inteiro com margem". Phoenix: 1 PIOR na thread (rodada 17) e 2 PIOR na conferência 2 com o mesmo modelo.
- **Cada pet com seu render.** Três scripts de câmera, luz e ícone diferentes; o halo e a margem do ícone do Titan vinham do `icone.py` dele.
- **Critério 1 sem mudar a forma.** A Phoenix teve PIOR no critério 1 em todos os vereditos contados, sempre por "um material só", e as correções mexiam em tom e tamanho de placa.

## As regras

### 1. Rodar até aprovar (autorização permanente)

As threads de pet não param por contagem de rodadas. Seguem até APROVADO, com a **regra de platô**: se o mesmo critério ficar PIOR por **3 rodadas seguidas**, a rodada seguinte troca de abordagem naquela parte (variantes de forma bem diferentes, folha de conceitos 2D, imagem → malha; ver regra 8), em vez de parar. A thread só para por motivo real (ferramenta faltando, decisão que é do usuário) e, mesmo assim, segue com a opção recomendada enquanto espera o card. Um lote não passa de 30 rodadas sem um relato ao usuário com o placar.

### 2. Uma rodada num comando

```
python .framework/rodada.py --pet "<Pet>" --rodada N [--variantes A B C] [--pior 1,6] [--modo rapido|final] [--efeitos]
python .framework/rodada.py --pet "<Pet>" --rodada N --aplicar B      # guarda a variante escolhida
```

Faz o build de cada variante (em paralelo, cada uma com a própria cópia de `fonte/`), o render padrão, a checagem e a folha, e escreve `jogos/.rodadas/<Pet>/rodadaN/resumo.md` (pasta fora do Git). Cada pet tem um `rodada.json` na pasta dele dizendo como montar (comandos de build, GLB, efeitos). O build lê `VARIANTE` (A, B, C) no ambiente para escolher a forma de cada variante e `OUT` para a pasta de saída.

### 3. Kit único de render e ícone

`python .framework/render_pet.py --glb <pet.glb> --saida <pasta> [--modo rapido|final]` renderiza qualquer pet a partir do GLB com a mesma câmera, luz (só sóis: chave, preenchimento, recorte quente e recorte frio), ambiente e fundo transparente. A frente é achada pelos olhos. Pose: 1º quadro do Idle.

**Ícone padrão do lote (decisão do usuário, 31/10/2026):** vista 3/4 de frente (30°), **pet inteiro ocupando 88% do lado maior** do quadro de 128 px, centrado, fundo transparente, luz de recorte no render e **nenhum halo ou contorno pintado depois**. Não muda entre rodadas nem entre pets. O `comparar.py` usa a mesma ocupação de 88% para os ícones do SAE na faixa de 128 px.

As vistas com efeitos ainda saem do script de cada pet (`efeitos` no `rodada.json`).

![[Recursos/Pets lendarios e miticos/Processo rapido/kit_render_rodada17.png]]

### 4. Checagem automática antes do revisor

`python .framework/checar.py` (o `rodada.py` já roda) mede em segundos e **barra a rodada** antes de gastar revisor:

| Item | Bloqueia quando |
| --- | --- |
| Triângulos por malha, texturas, clipes | passa de 20 000, de 1024² ou faltam Idle, Walk/Fly/Swim, Happy e 1 especial |
| Ícone | não é 128×128 transparente, ocupa fora de 84–92% ou encosta na borda |
| Halo no ícone | mais de 3% de pixels semitransparentes fora da silhueta |
| Famílias de cor e material | abaixo da mediana do SAE do degrau **e** o critério 1 deu PIOR (sem PIOR no 1, só avisa) |
| A forma mudou | houve PIOR e nenhuma malha se deslocou ≥ 0,3% da altura nem a silhueta mudou (IoU < 0,99): a correção trocou só cor, tom ou brilho |

O "visível no fundo escuro" só avisa (comparado com a faixa do SAE do degrau). **Passar na checagem não aprova nada**; quem aprova é o revisor.

### 5. Variantes na mesma rodada

Para cada parte PIOR, fazer **2 ou 3 formas diferentes** (regra do usuário de corrigir um PIOR) como variantes A, B, C da mesma rodada. O `rodada.py` monta a **folha de variantes** (uma linha por variante, ao lado do SAE do degrau e do lote). O revisor escolhe a melhor e dá o veredito dela; quem fez o pet guarda a escolhida com `--aplicar` e registra na entrega o motivo, as formas testadas e a escolhida.

### 6. Render rápido para iterar, final para entregar

| Modo | Resolução | Amostras | Tempo medido (4 imagens, CPU de 4 núcleos) |
| --- | --- | --- | --- |
| `rapido` | 512 | 16 + denoise | ~20 s por pet |
| `final` | 1024 | 64 + denoise | ~250 s por pet |

Variantes e rodadas intermediárias em `rapido`. A folha que vai para o PR do lote e a da conferência final em `final`, com efeitos.

### 7. Revisão estável

- **Banca de 3 revisores em paralelo** por rodada, cada um com só a folha, a régua, esta nota e as âncoras, sem a opinião de quem fez o pet. Consolidar com `python .framework/banca.py --vereditos r1.md r2.md r3.md`: maioria por critério; sem maioria vale PIOR; INCONCLUSIVO pede folha nova.
- **Critério travado:** se a checagem mostrar que a parte de um critério não mudou (mesmas malhas, mesma silhueta, mesmo ícone), o critério fica com o resultado da rodada anterior (`banca.py --travar ... --anterior ...`). Foi o caso da rodada 9 do Titan, em que só o ícone mudou.
- **Um nível só:** a folha de cada rodada já traz o lote no mesmo render, então ela vale como conferência. Não há mais revisor de thread e revisor de conferência com vereditos diferentes; a conferência do lote é a última rodada dos três pets, em modo final.
- **Âncoras:** exemplos reais do lote 1, com a folha e a frase do veredito, para o revisor calibrar o que é IGUAL e o que é PIOR (seção abaixo).

Pedido ao revisor (texto fixo, igual para os três da banca):

> Você é revisor independente. Abra (Read) a folha `<caminho>` e leia a régua `12 Modelos e pets/Pets lendarios e miticos/Regua Steal An Egg para os 21 pets.md` e as âncoras da nota `Processo rapido de rodada.md`. Para cada critério de 1 a 7 (o 7 é a fidelidade à imagem-alvo, só IGUAL ou PIOR), responda numa tabela `| Critério | Veredito | Comparado com | O que se vê na folha |` com MELHOR, IGUAL, PIOR ou INCONCLUSIVO, citando um pet SAE pelo nome e algo visível. Na dúvida, PIOR. Se for folha de variantes, diga primeiro qual variante é a melhor e por quê, e dê o veredito dela. Diga onde o SAE ainda é melhor e a correção que falta (de forma, não só de cor).

### 8. Critério 1 pela forma e pelo material

> **Atualizado em 31/10/2026:** com as imagens-alvo finais (régua, critério 7), a forma e o material de cada pet já estão decididos pela imagem. Não se fazem mais conceitos 2D novos: toda variante parte da imagem-alvo, e uma delas, sempre que der, vem de **imagem → malha** a partir dela. O texto abaixo vale só para pets sem imagem-alvo.

Quando o critério 1 der PIOR (ou bater o platô), antes de modelar: uma **folha de conceitos 2D** com 3 conceitos de forma e material ao lado do pet SAE citado, julgada pela banca em minutos. O conceito escolhido vira referência em `Recursos/Pets lendarios e miticos/<Pet>/conceitos/`. Seguindo [[Modelo 3D a partir de imagem]], uma das variantes pode vir de **imagem → malha** (`generate_mesh` do Studio). O teste com o ForgeGUI em 31/10/2026 foi recusado: a geração 3D exige plano pago na conta do usuário, e nenhum crédito foi gasto.

### 9. Blender pronto ao abrir a sessão

O hook `.claude/hooks/blender.sh` (registrado em `.claude/settings.json`) instala `bpy`, `pillow`, `numpy`, `scipy` e `scikit-image` nas sessões na nuvem quando faltam (cerca de 1m45 uma vez por sessão), para nenhuma thread perder tempo nisso.

### 10. Uma branch e um PR por lote; decisões num card só

As threads de um lote fazem push na mesma branch e no mesmo PR do lote (o lote 1 gerou 11 PRs, de #13 a #23). Antes de começar um lote, a thread do lote junta num card só as decisões que são do usuário (por exemplo: reorganizar a forma de um pet, ligar o computer use para prints do Studio).

## Âncoras do revisor (lote 1)

As folhas estão em `Recursos/Pets lendarios e miticos/<Pet>/folhas/` e `Lote 1 Volcano/conferencia2/` (chegam à `main` com o PR #20).

| Critério | IGUAL (exemplo) | PIOR (exemplo) |
| --- | --- | --- |
| 1 Nível | Molten Dragon, conferência 2: "coroa dourada com cristal, asas grandes com bordo dourado, faixas douradas nas pernas; nem mais simples nem mais carregado" que o bone-emperor | Lava Titan, conferência 2: "um só material grafite facetado e liso", contra os 3 materiais do pumpkin-golem |
| 2 Coerência | Volcanic Phoenix, conferência 2: "células poligonais cinza, fissuras laranja finas e olhos amarelos no mesmo traço e densidade do Titan e do Dragon" | Lava Titan, conferência 2: "muitos cacos pequenos e soltos com frestas finas", contra as placas grandes com junta laranja grossa dos outros dois |
| 3 Escada | Lava Titan, conferência 2: "corpo largo e atarracado com ombros e punhos grandes, fissuras laranja, sem coroa nem dourado" | Volcanic Phoenix, conferência 2: "corpo em ovo estreito com pernas finas; a largura vem só das asas" |
| 4 Brilho e rosto | Lava Titan, conferência 2: "corpo fosco, brilho numa família quente; olhos amarelos bravos legíveis de frente e a 3/4" | Lava Titan, rodada 6: "olhos em discos amarelo-pálidos chapados como adesivos; pontas dos espinhos em outro amarelo" |
| 5 Paleta | Molten Dragon, conferência 2: "os três se reconhecem pelo carvão com laranja" | Lava Titan, conferência 1: "na faixa de 128 px é cinza médio, com a cabeça mais clara" |
| 6 Ícone | Lava Titan, conferência 2: "olhos e boca acesa se leem nos dois fundos; silhueta de gorila curvado" | Molten Dragon, conferência 2: "ocupa bem menos o quadro que os SAE; no fundo escuro o corpo carvão se mistura" |

## Medição

Cada `resumo.md` registra os segundos de cada etapa. A nota do lote registra, por rodada: minutos de relógio, turnos gastos e PIOR consolidados, para comparar com o lote 1 (cerca de 11 a 13 min e 25 turnos por rodada).

Teste do kit em 31/10/2026 refazendo a rodada 17 do lote 1: Lava Titan 94 s no total (build 9 s), Molten Dragon com 2 variantes em paralelo 124 s (build 36 s), Volcanic Phoenix com efeitos 234 s (efeitos 183 s, pelo script do pet). A checagem barrou corretamente as três rodadas refeitas sem mudança ("a forma não mudou") e o ícone antigo do Titan (halo 11% da área, ocupação 83%).

## Conexoes

[[Regua Steal An Egg para os 21 pets]] · [[Lote 1 Volcano - pets lendarios e miticos]] · [[Modelo 3D a partir de imagem]] · [[Leitura do pet em miniatura]]
