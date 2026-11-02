---
area: modelos
tipo: ficha-de-remake
resumo: Remake do Lich King (Mythic, Haunted) — rei necromante esqueleto em armadura gótica com ombreiras de caveira, coroa de pontas, capa roxa rasgada e cajado com filactério roxo.
termos: lich king rei lich haunted mythic necromante esqueleto armadura gotica caveira coroa capa roxa cajado filacterio runas remake
---
# Lich King

**Haunted · Mythic · gait `ground` (paira a 0,3) · altura base 6,6 (topo da coroa) · largura ≤ 4,6**

![[Recursos/Pets lendarios e miticos/LichKing_alvo-2d.webp|300]] ![[Recursos/Pets lendarios e miticos/LichKing_render-atual.webp|300]]

## Em uma frase
O rei necromante: esqueleto alto em armadura gótica de placas com filetes dourados, ombreiras enormes com caveiras e espinhos, coroa alta, olhos de chama verde, capa roxa rasgada e um cajado retorcido com um cristal roxo flutuando no topo. Vertical, simétrico e régio. **Ainda não está no jogo** (área Haunted sem `Config`).

## O que mudar em relação ao render atual
- **Proporção:** o render é fino e alto, com crânio pequeno e capa estreita. O alvo é **largo e heroico**: ombreiras grandes (largura ≤ 4,6), crânio 12% maior (0,75), mãos de osso grandes, capa larga (2,6 atrás) que abre dos lados.
- **Filetes dourados:** o alvo usa **ouro velho** `C9A040` nas bordas da armadura (a ficha dizia prata). Seguir o alvo: dá contraste e leitura de rei.
- **Armadura mais clara:** aço azul-ardósia `4A5064` com highlight `8A94AA`; o render está preto.
- **Coroa** dourada com pontas altas em volta do crânio, visível a 64 px.
- **Cajado** retorcido com crânio pequeno e garras segurando o filactério; cristal roxo maior e mais brilhante.
- **Chamas verdes nos olhos** fortes (no render quase somem).

## Silhueta e proporções
- 3 formas-chave: **coroa alta sobre o crânio**, **ombreiras góticas enormes com caveira e espinhos**, **cajado acima da coroa** com o filactério.
- Tórax em V com cintura; pernas longas com grevas; mãos de osso grandes (palma 0,45).
- Pose: ereto, mão direita no cajado, mão esquerda aberta em gesto de feitiço.

## Anatomia e construção
- Núcleo de esqueleto humano visível nas juntas (cotovelo, joelho, cintura).
- **Armadura** derivada da superfície: peitoral com fluting em V e runa central verde, 4 lâminas de tassets recortadas, **ombreiras em 3 camadas** com caveira em relevo e 3 espinhos curvos cada, cotoveleiras e joelheiras em ponta ogival com asa lateral, braçais e grevas só com placa frontal (osso aparece atrás), sabatons de 4 lâminas.
- **Gola alta** em leque recortado atrás do crânio.
- **Crânio:** arcada pesada, maçãs salientes, mandíbula separada com dentes, órbitas fundas com chamas verdes, rachadura na têmpora.
- **Coroa:** 7 pontas góticas de alturas alternadas, joia roxa central (Mythic), filigrana.
- **Capa:** 6 lâminas de tecido rígido roxo com forro mais escuro e borda dourada, barra rasgada em tiras.
- **Mãos:** falanges marcadas, 3 anéis com joias na esquerda.
- **Cajado:** haste retorcida (6,8), crânio pequeno e 3 garras no topo, filactério facetado flutuando 0,15 acima.
- **Névoa** baixa e larga sob os pés, em lâminas onduladas quase horizontais.

## Paleta (3 tons + destaque)
| Papel | Hex | Onde |
| --- | --- | --- |
| Claro | `C9A040` ouro velho (highlight `E8C870`) | filetes, coroa, bordas da capa, caveiras das ombreiras |
| Médio | `4A5064` aço-ardósia | placas da armadura |
| Escuro | `262838` | fundo do fluting, frestas |
| Osso | `D9CFB4` com AO | crânio, mãos, juntas |
| Capa | `6A2A9A` com forro `3B1F4F` | capa |
| Destaque (Glow) | `C98BFF` filactério; `7CFFB0` olhos e runa | focos 1 e 2 |

## Olhos
Órbitas fundas com chamas verdes `7CFFB0` Glow, núcleo branco, saindo um pouco para cima. Foco 2; legíveis a 128 px sob a coroa.

## Detalhes-assinatura
- Uma ponta da coroa quebrada (2ª à direita).
- Corte de espada na ombreira esquerda (entalhe com metal claro exposto).

## Efeitos e aura (Mythic)
- Ambiente: **exclusivo `rune_circle`** (círculo de runas verde girando no chão, raio 2,2); névoa rolando baixa em 3 pontos; `orbit_ring` roxo pequeno em volta do filactério; `aura` roxa na mão esquerda; acento rosa Mythic na joia da coroa. 7 emissores + 8 beams + 1 luz.
- Ação **Cast**: ergue o cajado e as runas acendem em sequência → flash roxo, halo e 12 runas em espiral para cima → runas apagam uma a uma.

## Animação
Idle 4,0 s (paira, capa ondula, mão esquerda gira a energia, cabeça vira devagar) · Walk 2,2 s (desliza com passos curtos, capa arrasta) · Happy 2,5 s (ergue o cajado e ri, mandíbula bate) · Cast 2,6 s (fx em 0,6 s).

## Proibições e aceitação
- Armadura gótica com recorte e fluting, nunca balde. Sem cilindros completos nos membros.
- Coroa com pontas de alturas diferentes. Mãos grandes. Névoa irregular, nunca pétalas.
- A 64 px: silhueta larga de ombreiras + crânio com olhos verdes + cristal roxo no alto.

## Referências a reusar
`LichKing_alvo-2d` (meta, inclusive os filetes dourados), `LichKing_render-atual` (rig bípede, cajado), seção 3 de `fichas-originais/ficha-L4-Haunted.md`.
