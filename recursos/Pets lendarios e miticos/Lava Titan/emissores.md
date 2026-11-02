---
area: modelos
tipo: ficha-de-vfx
resumo: Lista de emissores e luz do Lava Titan v3 (Legendary, Volcano), com flipbooks, pontos de origem, propriedades de partida e versão low, dentro do orçamento da raridade.
termos: lava titan vfx emissores particleemitter flipbook crater smoke magma drip core pulse slam ring chips orçamento legendary low
---
# Lava Titan v3 — emissores e orçamento

Orçamento Legendary (nota [[00 Remake dos pets lendarios e miticos]]): normal ≤ 6 emissores, ≤ 10 beams, ≤ 1 luz; low ≤ 3 emissores, 0 luz.
**Uso: 6 emissores, 0 beams, 1 luz (normal) · 3 emissores, 0 luz (low).** Dentro do orçamento.

Flipbooks em `vfx/` (1024², fundo transparente, gerados com `python .framework/flipbook.py` a partir dos HTML da mesma pasta). Posições em studs no tamanho base, pivô no chão, eixos do Roblox (X direita do pet, Y para cima, −Z para a frente); no jogo multiplicar pela escala Legendary ×1,6. O brilho fixo das veias e dos olhos é a malha `LavaTitan_Magma` em material Neon (laranja-lava `FF7A1A`), não partícula. Todos os efeitos usam o mesmo laranja-lava (rodada 3: brasas no lugar da fumaça e aura no chão no lugar do pulso do peito).

| # | Emissor | Flipbook | Attachment (osso, posição) | Rate / disparo | Lifetime | Size | Speed | Propriedades | Low |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `crater_embers` | `LavaTitan_crater_embers_4x4.png`, Grid4x4, Loop, 15 fps, StartRandom | chest, (0; 3,6; 1,25) cratera das costas | 1,5/s | 1,2–1,6 s | 0,9 → 1,4 | 1,8 para cima, Spread 15° | LightEmission 1, LightInfluence 0, Brightness 1,5, Transparency 0 → 1 | fica |
| 2 | `magma_drip.R` | `LavaTitan_magma_drip_4x4.png`, Grid4x4, OneShot, 24 fps | hand.R, (2,36; 0,6; −1,3) | 0,4/s | 0,7 s | 0,35 | 0, Acceleration (0; −18; 0) | LightEmission 1, LightInfluence 0, Brightness 2 | sai |
| 3 | `magma_drip.L` | igual ao 2 | hand.L, (−2,36; 0,6; −1,3) | 0,4/s | 0,7 s | 0,35 | igual | igual | sai |
| 4 | `ground_aura` | `LavaTitan_ground_aura_4x4.png`, Grid4x4, Loop, 12 fps | root, (0; 0,05; −0,2) | 1 partícula fixa (Rate 0,4, Lifetime 2,5) | 2,5 s | 7,6 | 0, LockedToPart, Orientation VelocityPerpendicular (deitada no chão) | LightEmission 1, LightInfluence 0, Brightness 1 (abaixo do anel do Molten Dragon, que é Mythic) | fica |
| 5 | `slam_ring` | `LavaTitan_slam_ring_4x4.png`, Grid4x4, OneShot, 30 fps | root, (0; 0,05; −1,6) chão à frente | Emit(1) no quadro 15 do Slam (0,5 s) | 0,55 s | 2 → 7 | 0, Orientation VelocityPerpendicular (deitado no chão) | LightEmission 0,8, LightInfluence 0,2 | fica |
| 6 | `slam_chips` | `LavaTitan_slam_chips_2x2.png`, Grid2x2, Random | root, (0; 0,05; −1,6) | Emit(16) no quadro 15 do Slam | 0,8–1,1 s | 0,25–0,45 | 9–14, Spread 70° para cima, Acceleration (0; −30; 0), RotSpeed ±300 | LightEmission 0, LightInfluence 1 | sai |
| L | `PointLight` cratera | — | chest, (0; 3,7; 1,2) | — | — | Range 8 | — | Color FF7A1E, Brightness 1,5; no Slam sobe para 2,3 (+50%) por 0,3 s | sai |

Ação **Slam** (clipe de 2,2 s): ergue os punhos (quadro 10), punhos no chão no quadro 15 → dispara 5 e 6 e o pico da luz. Poeira está dentro do flipbook do anel (camada cinza que rola para fora), por isso não usa emissor extra.

## Conexoes
[[Lava Titan]] · [[VFX do HTML para o Roblox]] · [[Efeitos reduzidos com identidade]] · [[Regua Steal An Egg para os 21 pets]]
