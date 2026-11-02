---
area: modelos
tipo: ficha
resumo: Lista de emissores e luz do Molten Dragon v3 (Mythic, Volcano), presos aos ossos FX_ do GLB, dentro do orçamento de VFX do Mythic (≤ 8 emissores, ≤ 1 luz, ≤ 16 partículas vivas).
termos: molten dragon emissores vfx flipbook orcamento mythic particleemitter fx_crown fx_back fx_ground breath aura fumaca
---
# Molten Dragon: emissores e orçamento de VFX

Orçamento do Mythic (nota `00 Remake dos pets lendarios e miticos`): **≤ 8 emissores, ≤ 12 beams, ≤ 1 luz, ≤ 16 partículas vivas** no normal; no low, ≤ 4 emissores e 0 luz.
Cada emissor fica num osso `FX_*` do GLB (no Roblox, `Bone` é um `Attachment`). Texturas em `vfx/` (1024², grade 4×4, fundo transparente), geradas com `python .framework/flipbook.py` a partir dos HTML da mesma pasta. Precisam ser enviadas ao Roblox (upload é ação do usuário) e o `rbxassetid` entra no lugar do nome do arquivo.

Valores comuns: `LightEmission = 1`, `LightInfluence = 0`, `FlipbookLayout = Grid4x4`, `Transparency` 1 → 0 → 1, salvo onde dito.

## Camada ambiente (sempre ligada no plot): 5 emissores + 1 luz

| # | Nome | Osso | Textura / modo | Rate · Lifetime | Vivas | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `Aura_Flame` | `FX_Back` | `chama-aura_4x4` · Loop 24 fps, StartRandom | 2,5/s · 1,2 s | 3 | `Shape = Box` 3,2 × 0,4 × 0,8 ao longo do dorso (os "4 pontos" da ficha num só emissor); Speed 1,5 para cima; Size 1,6 → 2,2 |
| 2 | `Nostril_Smoke` | `FX_Nostril` | `fumaca-narina_4x4` · OneShot 12 fps | `Emit(2)` a cada 4 s (no Idle, em 2,0 s) · 1,4 s | 2 | **exclusivo** do pet; `LightEmission = 0`, `Transparency` 0,65 → 1 (translúcida), Size 0,8 → 1,3, Speed 1,2 para a frente e para cima, para não passar na frente dos olhos (rodada 16) |
| 3 | `Crown_Sparkle` | `FX_Crown` | `brilho-coroa_4x4` · Loop 16 fps, StartRandom | 1,5/s · 1,0 s | 2 | Color dourado `FFD060`; uma de cada 3 com `FF8A30` (laranja-lava; o rosa saiu na rodada 16 por estar fora da paleta) |
| 4 | `Furnace_Pulse` | `FX_Furnace` | `pulso-fornalha_4x4` · Loop 12 fps | 0,8/s · 1,4 s | 2 | Speed 0, `LockedToPart = true`, ZOffset 0,5 |
| 5 | `Ground_EmberRing` | `FX_Ground` | `anel-brasas-chao_4x4` · Loop 8 fps | 0,4/s · 3,0 s | 2 | elemento de chão do Mythic; `Orientation = VelocityPerpendicular`, velocidade (0, 0,01, 0), Size 7 |
| L | `Throat_Light` | `FX_Furnace` | `PointLight` | — | — | `FF7A30`, Brightness 1,5, Range 8; desligada no low |

Ambiente: **5 emissores, 1 luz, ~11 partículas vivas**.

## Camada de ação (só no clipe `Breath`, 2,4 s): 3 emissores

| # | Nome | Osso | Textura / modo | Disparo | Vivas | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| 6 | `Breath_Cone` | `FX_Mouth` | `sopro-fogo_4x4` · OneShot 20 fps | `Emit(3)` em 0,6 s, 0,7 s e 0,8 s | 3 | `SpreadAngle` 18°, Speed 14, Size 1,2 → 3,5, Lifetime 0,8 s |
| 7 | `Breath_Core` | `FX_Mouth` | `pulso-fornalha_4x4` · Loop 24 fps | `Emit(1)` em 0,55 s (antecipação) | 1 | Size 1,5, Lifetime 0,4 s: a boca acende antes do fogo |
| 8 | `Breath_Embers` | `FX_Mouth` | `brasa_4x4` · Random | `Emit(6)` em 1,2 s | 6 | Acceleration (0, −6, 0), Speed 6, Lifetime 1,0 s: brasas caindo na dissipação |

No `Breath`, `Aura_Flame` e `Ground_EmberRing` pausam (`Enabled = false` de 0,5 s a 1,8 s), então o pico é **6 emissores ativos (8 no total, ≤ 8)** e **~14 partículas vivas (≤ 16)**.

## Low (≤ 4 emissores, 0 luz)

Liga só `Aura_Flame` (Rate 1,5), `Crown_Sparkle`, `Furnace_Pulse` e, no `Breath`, `Breath_Cone` no lugar de `Furnace_Pulse`. Sem `Throat_Light`.

## Sem VFX no servidor

Os emissores são criados e disparados no cliente, pelo marcador do clipe (`Breath` em 0,55 / 0,6 / 1,2 s, `Idle` em 2,0 s). Sem Bloom permanente.
