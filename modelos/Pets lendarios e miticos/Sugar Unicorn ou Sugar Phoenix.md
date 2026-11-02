---
area: modelos
tipo: ficha-de-remake
resumo: Remake do Lendário de bala da CandyLand — o modelo existente é a Sugar Phoenix (fênix de vidro de açúcar e bala dura); o nome e a espécie (Sugar Unicorn ou Sugar Phoenix) ainda estão em aberto.
termos: sugar unicorn sugar phoenix unicornio fenix de acucar candyland legendary bala dura vidro de acucar caramelo pirulito nome em aberto remake
---
# Sugar Unicorn ou Sugar Phoenix

**CandyLand · Legendary · nome em aberto**

![[Recursos/Pets lendarios e miticos/SugarPhoenix_alvo-2d.webp|300]] ![[Recursos/Pets lendarios e miticos/SugarPhoenix_render-atual.webp|300]]

## Decisão em aberto: unicórnio ou fênix
- O pet aparece como **Sugar Unicorn** em parte das listas do projeto, mas a tabela de pets e ovos das áreas novas (`planos/2026-10-16_212728-new-pets-eggs.luau`, no zip de contexto) usa `SugarPhoenix` no Lollipop Egg, e o modelo feito, o alvo 2D e o render são de uma **Sugar Phoenix**.
- A mesma tabela já tem um **Choco Unicorn** (Epic) na CandyLand. Um Sugar Unicorn Lendário repetiria a espécie na mesma área e seria o segundo quadrúpede ao lado do Sprinkle Dragon. A fênix completa o trio com um **voador** (Golem bípede, Dragon quadrúpede).
- **Recomendo manter a Sugar Phoenix** (já tem alvo 2D e render do portão C). Contra: a Volcano já tem a Volcanic Phoenix e um Phoenix Chick, então são 2 fênix Lendárias no jogo. Se o luks quiser evitar isso, usar o Sugar Unicorn (descrito no fim desta nota, com prompt de alvo 2D pronto no `LEIA-ME` da pasta de referências) e diferenciá-lo bem do Choco Unicorn.
- A thread de remake deste pet deve começar por essa decisão.

---

## Opção A (recomendada): Sugar Phoenix

**gait `fly` · altura base 4,8 (corpo de 1,2 a 4,8) · envergadura 6,2**

### Em uma frase
Uma fênix de vidro de açúcar soprado e bala dura, translúcida e facetada como escultura de confeitaria de competição: asas de cristais rosa, peito de caramelo âmbar com um coração de rubi, crista de pirulito e cauda de fitas de bala listrada. Radiante e vaidosa.

### O que mudar em relação ao render atual
- **Corpo proporcional às asas:** o render tem tórax fino e pernas de palito. O alvo tem **peito de caramelo em quilha grande** (35% maior que a v1) e coxas emplumadas grossas.
- **Cauda:** o alvo tem **5–7 fitas largas listradas rosa e branco** em curva com cristal rosa na ponta. No render são poucas e finas.
- **Coração de rubi** no peito maior e facetado (foco 1), como no alvo.
- **Penas das asas** mais saturadas, com degradê rosa-choque → rosa-claro e a linha branca de reflexo.

### Silhueta e proporções
- 3 formas-chave: **V alto das asas** (~60°), **peito de caramelo em quilha**, **cauda de fitas** longas (2,2) em curva.
- Tórax 1,2 × 1,4; pescoço em S (0,7); cabeça de ave de rapina com 1,0; coxas e garras de caramelo grossas.

### Anatomia e construção
- Núcleo de ave de rapina com quilha profunda.
- **Peito:** placa de caramelo âmbar facetada como pedra lapidada + coração de rubi vermelho no centro.
- **Penas do corpo:** escamas de bala dura facetadas (crista em V), degradê cereja no pescoço → rosa → caramelo no ventre.
- **Asas:** 3 fileiras de coberteiras, 6 secundárias, 7 primárias (1,6 → 2,3), todas facetadas; as 2 fileiras externas translúcidas; **pontas com cristal de açúcar rosa** (Glow).
- **Cabeça:** bico de caramelo duro em 2 placas, sobrancelha facetada, **crista de 5 lâminas** com **pirulito em espiral** na ponta central (coesa, nunca antena).
- **Cauda:** fitas de caramelo puxado (0,3 de largura) com listra rosa/branca e leve torção, terminando em gota de bala Glow.

### Paleta (3 tons + destaque)
| Papel | Hex | Onde |
| --- | --- | --- |
| Claro | `FFC8E4` (rosa claro com reflexo branco) | borda das penas, fitas brancas |
| Médio | `FF6EB4` | penas, fitas rosa |
| Escuro | `C93A7A` (e caramelo `C9781A` no peito) | base das penas, sombra |
| Destaque (Glow) | `FF5FC0` cristais; `FFE14A` brilho atrás do peito; `E0203A` rubi | pontas das asas, coração, gotas da cauda |

### Olhos
Pequenos de ave de rapina, Glow limão `FFE14A`, pupila escura, sob sobrancelha facetada. Legíveis a 128 px (já OK na auditoria; manter).

### Detalhes-assinatura
Pirulito da crista lascado; uma fita da cauda com um nó.

### Efeitos e aura (Legendary)
- Ambiente: **exclusivo `sugar_glints`** (cintilas de açúcar orbitando as asas); **exclusivo `candy_trail`** (rastro de bala listrada nas pontas das asas, só em movimento); `core_pulse` amarelo no peito. 5 emissores + 2 trails.
- Ação **Sparkle**: asas fecham e a luz interna sobe → estouro de 18 cristais de açúcar + halo rosa → cristais caem cintilando.

### Animação
Idle 3,0 s (paira, fitas ondulam com atraso) · Fly 1,2 s · Happy 2,2 s (giro + pose de asas abertas) · Sparkle 2,0 s (fx em 0,4 s).

### Proibições e aceitação
- Lê como vidro e bala dura (facetas e reflexo no close). Nada de plástico opaco, bolas redondas ou penas em losango chapado.
- A 64 px: V rosa + peito âmbar com ponto vermelho + fitas listradas.

---

## Opção B: Sugar Unicorn (se o luks preferir)

**gait `ground` · altura base ~5,0 (ponta do chifre) · comprimento ~4,6**

- **Conceito:** unicórnio empinando de leve (uma pata dianteira erguida), feito de **placas facetadas de bala dura rosa-pastel e branca** com filete de glacê creme.
- **Chifre:** espiral de bengala rosa e branca com ponta de cristal Glow (foco 1).
- **Crina e cauda:** algodão-doce em **lâminas rígidas facetadas** rosa, lavanda e menta (nunca pelúcia fofa), com confeitos incrustados só no glacê.
- **Peito e cascos:** gomas facetadas no peito (foco 2, Glow rosa) e cascos de bala de rocha rosa.
- **Olhos:** magenta brilhante com pupila escura e brilho branco, legíveis a 64 px.
- **Paleta:** claro `FFF0F6`, médio `FF9ACC`, escuro `C05A90`, destaque `FF5FC0` + menta `6EE0B8`.
- **Efeitos:** cintilas de açúcar em volta; ação "Rainbow Dash" com rastro de bala listrada.
- **Risco:** inflado/fofo. Manter quina viva e facetas como a Sugar Phoenix.
- Alvo 2D: ainda não existe; usar o **prompt 2** de `referencias-pets-lendarios-miticos/LEIA-ME_referencias-e-prompts.md`.

## Referências a reusar
`SugarPhoenix_alvo-2d` (meta da opção A), `SugarPhoenix_render-atual` (malha e rig), seção 2 de `fichas-originais/ficha-L4-CandyLand.md`, prompt 2 do LEIA-ME para a opção B.
