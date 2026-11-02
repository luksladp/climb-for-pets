---
area: modelos
tipo: ficha-de-remake
resumo: Remake do Gingerbread Golem (Legendary, CandyLand) — golem guardião de biscoito de gengibre grosso decorado com glacê real, juntas de caramelo, lareira no peito e chaminé nas costas.
termos: gingerbread golem golem de biscoito candyland legendary gengibre glace caramelo lareira chamine bengala remake
---
# Gingerbread Golem

**CandyLand · Legendary · gait `ground` · altura base 5,4 · largura ≤ 4,2**

![[Recursos/Pets lendarios e miticos/GingerbreadGolem_alvo-2d.webp|300]] ![[Recursos/Pets lendarios e miticos/GingerbreadGolem_render-atual.webp|300]]

## Em uma frase
Um guardião bonachão montado com biscoitos de gengibre grossos de confeitaria fina: cada placa da armadura é um biscoito cortado (escudo, coração, estrela, homenzinho) decorado com glacê branco, unido por caramelo escuro, com uma lareira acesa atrás do coração do peito e uma casinha de biscoito com chaminé nas costas.

## O que mudar em relação ao render atual
O render está perto do alvo. Ajustes:
- **Biscoito mais claro e alaranjado:** o alvo tem `D98A40` nos topos, com borda assada escura. O render está marrom-chocolate. Subir o valor e saturar.
- **Glacê mais grosso e definido**, com relevo e variando por placa (zigue-zague, espirais, pontinhos). No render está fino.
- **Chaminé/casinha** visível acima do ombro esquerdo, como no alvo (no render some).
- **Porosidade** de biscoito em escala média com pontinhos de açúcar, como no alvo.
- **Olhos** de bala rosa brilhante sob sobrancelha de glacê franzida (já ok; manter e aumentar 10%).

## Silhueta e proporções
- 3 formas-chave: **ombros altos e massivos** (ombreiras de 3 biscoitos empilhados), **cabeça de homem-biscoito** (topo redondo), **chaminé nas costas** passando acima do ombro.
- Tronco em barril (1,9), cintura 1,4; antebraços Ø 0,7 > braços 0,5; mãos grandes; pernas curtas e grossas; pés largos.
- Pose: ereto, pesado, punhos fechados ao lado do corpo.

## Anatomia e construção
- Núcleo de golem em **caramelo escuro úmido** (`8A4A1E`), que aparece nas juntas. Nunca cinza.
- **Placas = biscoitos** de 0,18–0,25 de espessura, topo levemente abaulado, borda assada com chanfro vivo, contorno de cortador:
  - peitoral: 2 escudos + coração central vazado (a lareira);
  - abdômen: 3 retângulos de borda ondulada;
  - ombreiras: estrela → círculo → homenzinho no topo;
  - coxas e antebraços: gotas; canelas: escudo alongado; joelhos com homenzinho de biscoito (como no alvo).
- **Glacê:** relevo variado por placa + cordões grossos escorrendo nas juntas grandes, com gotas penduradas.
- **Botões:** 3 balas duras facetadas no peito (cereja, menta, caramelo). **Cinto:** bengala listrada em hélice (a única listra do pet).
- **Cabeça:** biscoito espesso (0,3), sobrancelha de glacê grossa franzida, boca de glacê em zigue-zague, mandíbula como placa separada.
- **Casinha nas costas:** paredes de biscoito com janelinhas de bala, telhado de telhas de chocolate com neve de glacê, chaminé de biscoito.

## Paleta (3 tons + destaque)
| Papel | Hex | Onde |
| --- | --- | --- |
| Claro | `E0A060` (topo do biscoito) | campo das placas |
| Médio | `B86B33` | corpo do biscoito |
| Escuro | `6A3A1C` (borda assada e caramelo `8A4A1E`) | bordas, juntas |
| Branco | `F7F2EA` glacê | decoração |
| Destaque (Glow) | `FFE14A` → `FF5FC0` lareira; `FF5FC0` olhos | coração do peito, olhos, janelinhas |

## Olhos
Balas duras rosa `FF5FC0` vítreas e Glow, pequenas mas claras, sob sobrancelha de glacê franzida (cara de protetor sério). Legíveis a 128 px.

## Detalhes-assinatura
- Mordida grande no ombro esquerdo (contorno de dentes e migalhas).
- 2 rachaduras de biscoito (abdômen e canela direita) com lascas soltas.

## Efeitos e aura (Legendary)
- Ambiente: **exclusivo `chimney_smoke`** (fumaça rosa algodão-doce saindo da chaminé, 1,0/s); **exclusivo `crumbs`** (migalhas caindo do tronco, 0,3/s); `core_pulse` amarelo-quente na lareira piscando como chama. 4 emissores + 1 luz.
- Ação **Stomp**: ergue o pé direito e a lareira cresce → anel de glacê no chão, 14 migalhas e 8 confeitos → poeira de açúcar.

## Animação
Idle 3,5 s (respira, cabeça inclina, fumaça pulsa) · Walk 2,0 s (pesado, ombros balançando) · Happy 2,5 s (bate as mãos, pulo leve) · Stomp 2,0 s (fx em 0,5 s).

## Proibições e aceitação
- Lê como biscoito decorado, nunca robô de blocos. Nenhuma placa é retângulo genérico.
- Sem bevel redondo grande (inflado), granulado fino ou pastel lavado. Juntas nunca cinza.
- A 64 px: silhueta de homem-biscoito largo + glacê branco + coração brilhando.

## Referências a reusar
`GingerbreadGolem_alvo-2d` (meta de cor e glacê), `GingerbreadGolem_render-atual` (forma e rig aproveitáveis), seção 1 de `fichas-originais/ficha-L4-CandyLand.md`.
