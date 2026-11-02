---
area: modelos
tipo: ficha-de-remake
resumo: Remake da Celestial Whale (Legendary, Cosmos) — baleia-azul cósmica de placas azul-noite com borda prata, janelas de nebulosa e galáxia, estrelas de ouro nas juntas e uma estrela presa num giroscópio de anéis acima da cabeça.
termos: celestial whale baleia celestial cosmos legendary baleia azul nebulosa galaxia constelacao prata ouro estrela giroscopio remake
---
# Celestial Whale

**Cosmos · Legendary · gait `swim` (flutua) · comprimento base 8,4 · altura 3,6 · corpo a 1,2**

![[Recursos/Pets lendarios e miticos/CelestialWhale_alvo-2d.webp|300]] ![[Recursos/Pets lendarios e miticos/CelestialWhale_render-atual.webp|300]]

## Em uma frase
Uma baleia-azul longa e serena feita de espaço: casco de placas azul-noite com borda prata, janelas de nebulosa roxa e azul nas nadadeiras e no ventre, estrelas douradas de 4 pontas nas juntas, e uma estrela brilhante presa num giroscópio de anéis prateados acima da cabeça.

## O que mudar em relação ao render atual
- **Nadadeiras e cauda:** no alvo são grandes, largas e cheias de **nebulosa brilhante** (violeta, magenta, azul com pontinhos). No render a cauda é um espeto fino e as nadadeiras somem. É a correção principal.
- **Placas:** o alvo tem placas grandes azul-noite com **borda prata grossa** e highlight azul. O render está cinza-escuro e chapado.
- **Estrelas de ouro** de 4 pontas nas junções (constelação), maiores e mais visíveis.
- **Giroscópio:** o alvo mostra a estrela dentro de **2 anéis prateados** cruzados acima da cabeça (o "planeta que escapou" da ficha virou uma estrela). Manter como no alvo, flutuando sobre a cabeça, solto.
- **Olho** ciano pequeno com aro prata, mais claro.

## Silhueta e proporções
- 3 formas-chave: **corpo longo de baleia-azul** com cabeça em U plana, **nadadeiras e cauda de nebulosa**, **giroscópio com estrela** acima da cabeça.
- Cabeça 25% do comprimento; peitorais 1,2 (aumentar para ~1,8 como no alvo); dorsal pequena a 3/4; fluke 2,6.
- Pose: nadando reta e longa, cauda em leve curva para cima. **Não arquear em U.**

## Anatomia e construção
- Núcleo de baleia-azul real (dorso reto, cabeça larga e plana, afunilamento longo).
- **Dorso e flancos:** placas alongadas no sentido do corpo (6 fileiras), borda prata, miolo azul-noite com highlight.
- **Ventre:** janela de nebulosa longa (60% do comprimento) com pregas ventrais prateadas atravessando; dentro, galáxia em espiral e 2–3 planetas pequenos.
- **Nadadeiras e cauda:** placas com miolo de nebulosa brilhante e borda prata; pontas translúcidas.
- **Constelação externa:** ~20 estrelas douradas de 4 pontas nas juntas, ligadas por filigrana fina.
- **Cabeça:** placa de ouro tipo astrolábio no rostro, olho ciano, barbatanas prata.

## Paleta (3 tons + destaque)
| Papel | Hex | Onde |
| --- | --- | --- |
| Claro | `C8CCE0` prata-lunar | bordas das placas, pregas, giroscópio |
| Médio | `2A3A8A` azul-noite (highlight `4A62C0`) | placas |
| Escuro | `161A40` | frestas, sombra |
| Nebulosa | `7A3CC8` / `D04AB8` / `3A6AE0` | nadadeiras, cauda, ventre |
| Destaque (Glow) | `FFF2C8` estrelas; `B88CFF` galáxia; `6AE8FF` olho | focos 1 e 2 |
| Metal | `E8C25A` ouro-estelar | estrelas, astrolábio |

## Olhos
Pequeno, ciano `6AE8FF` Glow com aro prata e pupila escura. Precisa aparecer a 128 px na lateral da cabeça.

## Detalhes-assinatura
- A estrela/planeta que "escapou" orbita fora do corpo, no giroscópio acima da cabeça.
- Uma estrela da constelação apagada na nadadeira esquerda.

## Efeitos e aura (Legendary)
- Ambiente: **exclusivo `star_wake`** (estrelas cintilando atrás do fluke, 2/s); **exclusivo `nebula_breath`** (nuvem de nebulosa pelo espiráculo a cada 7 s); `orbit_ring` nos anéis do giroscópio; `core_pulse` violeta na galáxia. 5 emissores + 6 beams + 1 luz.
- Ação **Supernova Song**: a galáxia gira rápido → flash de estrela no ventre, 3 anéis violeta e 20 estrelas radiais → dissipa.

## Animação
Idle 5,5 s (ondulação longa, galáxia gira, giroscópio gira) · Swim 3,2 s (batida lenta e ampla) · Happy 3,0 s (rolamento lento) · Song 3,0 s (fx em 0,6 s).

## Proibições e aceitação
- Distinta da Sky Whale: baleia-azul longa e escura, não jubarte de mármore.
- Flutua a 1,2. Sem arquear em U, ventre opaco ou pontinhos aleatórios pelo corpo.
- A 64 px: baleia azul longa + cauda e nadadeiras roxas brilhando + estrela acima.

## Referências a reusar
`CelestialWhale_alvo-2d` (meta), `CelestialWhale_render-atual` (corpo e rig; refazer nadadeiras e cauda), seção 2 de `fichas-originais/ficha-L4-Cosmos.md`.
