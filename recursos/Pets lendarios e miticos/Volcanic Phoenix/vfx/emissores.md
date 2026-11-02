---
area: modelos
tipo: ficha
resumo: Lista de emissores, trails e luz da Volcanic Phoenix (Legendary) com propriedades de partida e conta do orçamento de VFX da raridade (normal e low).
termos: volcanic phoenix vfx emissores particleemitter flipbook trail pointlight orcamento legendary ember_fall core_pulse flare
---
# Volcanic Phoenix — emissores e orçamento de VFX

Orçamento Legendary (nota `00 Remake dos pets lendarios e miticos`): normal ≤ 6 emissores, ≤ 10 beams, ≤ 1 luz, ≤ 12 partículas vivas; low ≤ 3 emissores, ≤ 6 beams, 0 luz. Todas as folhas são 1024×1024, fundo transparente, geradas com `python .framework/flipbook.py` a partir dos HTML desta pasta. As texturas ainda não têm asset id (subir é ação externa, fica para quando o usuário autorizar).

Valores comuns a todos: `LightEmission = 1`, `LightInfluence = 0`, `Transparency` 1 → 0 → 1, `FlipbookStartRandom = true` onde há mais de uma partícula.

| # | Emissor | Âncora (empty no GLB) | Textura | Layout / Mode / fps | Rate | Lifetime | Vivas | Outras propriedades | Camada | Low |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FlameWing.R | `FX_WingTip.R` | `flame_4x4.png` | Grid4x4 / Loop / 24 | 3 | 0,6 s | 2 | Size 2,0 → 0,8 (rodada 9: chamas maiores); Speed 0,6; Acceleration (0,2,0); LockedToPart | ambiente | não |
| 2 | FlameWing.L | `FX_WingTip.L` | `flame_4x4.png` | idem | 3 | 0,6 s | 2 | idem | ambiente | não |
| 3 | FlameCrest | `FX_Crest` | `flame_4x4.png` | Grid4x4 / Loop / 24 | 2,5 | 0,6 s | 1–2 | Size 1,6 → 0,7 (rodada 9); LockedToPart | ambiente | não |
| 4 | FlameTail | `FX_TailTip` | `flame_4x4.png` | Grid4x4 / Loop / 24 | 3 | 0,6 s | 2 | Size 2,0 → 0,8 (rodada 9); LockedToPart | ambiente | sim |
| 5 | EmberFall (exclusivo) | `FX_TailEmber` | `ember_feather_4x4.png` | Grid4x4 / OneShot / 6 | 0,6 | 3,0 s | 2 | Size 0,5–0,7; Speed 0,4; Acceleration (0,-1,5,0); RotSpeed ±60 | ambiente | sim |
| 6 | FlareBurst | `FX_Core` | `flare_ring_4x4.png` (anel + 24 brasas desenhadas na própria folha) | Grid4x4 / OneShot / 13 | 0 (Emit(1) em 0,4 s do Flare) | 1,2 s | 1 | Size 6; Speed 0; LockedToPart | ação | sim |
| T1 | WingTrail.R | `FX_WingTip.R` + attachment 0,4 abaixo | `trail_flame.png` | — | — | 0,35 s | — | Enabled só em Fly; WidthScale 1 → 0 | movimento | não |
| T2 | WingTrail.L | `FX_WingTip.L` | `trail_flame.png` | — | — | 0,35 s | — | idem | movimento | não |
| B1 | GroundRing (Beam deitado) | 2 attachments no chão, ±3,2 stud sob o corpo | `ground_ring.png` | — | — | — | — | Width0 = Width1 = 6,4 (rodada 8: no nível do anel do Titan); Color FF7A1E (laranja do Titan, rodada 9); FaceCamera false; TextureSpeed 0,15; LightEmission 1; Transparency 0 | ambiente | sim |
| L1 | CoreLight (PointLight) | `FX_Core` | — | — | — | — | — | Color FF6A2A; Brightness 0,8; Range 7; pulsa (tween 1,4 s) junto com a gema Neon | ambiente | desligada |

Rodada 3: as chamas das pontas viraram emissores próprios (pedido do revisor). Para caber em 6 emissores, o pulso do peito deixou de ser emissor (a gema é Neon e a `CoreLight` pulsa por tween), a aura sob as asas e as faíscas soltas saíram, e as brasas radiais do Flare passaram a ser desenhadas na folha `flare_ring_4x4.png`. `core_pulse_4x4.png`, `heat_aura_4x4.png` e `spark_2x2.png` ficam na pasta como alternativas, sem uso.

## Conta do orçamento

- **Emissores:** 6 (5 ambiente + 1 de ação) ≤ 6. Beams: 1 (anel de brasas no chão, rodada 4) ≤ 10. Trails: 2 (só em movimento). Luz: 1 ≤ 1.
- **Partículas vivas, ambiente:** 2 + 2 + 2 + 2 + 2 = 10 ≤ 12. **Durante o Flare:** + 1 = 11 ≤ 12.
- **Low:** FlameTail, EmberFall e FlareBurst = 3 emissores, 1 beam (anel), 0 luz, trails desligados.

## Sequência do Flare (2,0 s)

0–0,4 s asas fecham e a CoreLight acelera → 0,4 s estouro (FlareBurst, impacto de ~0,08 s) → 0,4–2,0 s asas abrem, fumaça do fim do FlareRing sobe e a pose volta ao Idle.
