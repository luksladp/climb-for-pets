---
area: modelos
tipo: ficha-de-remake
resumo: Mecha Titan (Legendary, CyberCity) — robô humanoide de placas grossas cinza-aço e navy, visor ciano, reator no peito, "07" num ombro e faixa de aviso no outro. É a referência de qualidade da leva; falta só o alvo 2D.
termos: mecha titan mechatitan v3 cybercity legendary robo humanoide aco navy visor ciano reator 07 faixa de aviso referencia de qualidade remake
---
# Mecha Titan

**CyberCity · Legendary · gait `ground` · medidas: as do pacote v3 aprovado (não estão nas fichas; conferir no `.blend`)**

![[Recursos/Pets lendarios e miticos/MechaTitan_referencia.webp|360]]

Render do Mecha Titan v3. **Não há alvo 2D ainda.**

## Em uma frase
Um robô heroico e robusto, primeiro produto da fabricante da CyberCity: cabeça quadrada com visor ciano largo e duas aletas-antena, ombreiras grandes em camadas, peitoral navy em V com reator redondo ciano, abdômen segmentado e pernas grossas com pés largos e chatos.

## Papel no projeto
- O **Mecha Titan v3 é a régua de qualidade** de todos os outros 20 pets (regras R1–R10 saíram da análise dele). O modelo está aprovado.
- O remake dele é pequeno: **(1)** gerar o **alvo 2D** no mesmo estilo dos outros (prompt 1 do `LEIA-ME_referencias-e-prompts.md`, anexando o render e dizendo "keep this design"); **(2)** ajustar a pintura para combinar com os alvos 2D da CyberCity (Quantum Cat e AI Overlord), que são mais claros e saturados que o render v3.

## O que ajustar no 3D (depois do alvo 2D)
- **Placas mais claras:** o v3 é cinza médio `6A707C`. Os irmãos usam aço claro `B8C0CC`–`E0E6F0`. Subir o valor das placas grandes para ler como da mesma linha.
- **Navy mais saturado** no peitoral (`24306A`), igual ao Quantum Cat.
- **Visor** com 2 faixas horizontais ciano (como no render) e um pouco mais de Glow: é o "rosto" e precisa ler a 64 px.
- Nada muda em forma, rig ou clipes.

## Silhueta e proporções
- 3 formas-chave: **ombreiras largas** (as massas dominantes), **peitoral em V com reator**, **pés largos e chatos**.
- Cabeça quadrada pequena em relação aos ombros; braços longos com mãos de 3 dedos + polegar; pernas grossas em camadas.
- Pose: em pé, postura heroica, braços levemente afastados.

## Construção (hard-surface MT3 puro)
- Caixas articuladas com chanfro de máquina, placa dentro de placa, parafusos, rebites e linhas de painel **permitidos** (é robô).
- Ombreiras em 3 camadas sobrepostas; peitoral em V navy com reator circular ciano; abdômen em 3–4 segmentos; cintura com 2 luzes magenta pequenas.
- Braços e pernas em cascas sobrepostas com juntas visíveis, mãos com dedos articulados, pés largos com sola grossa.

## Paleta (3 tons + destaque)
| Papel | Hex | Onde |
| --- | --- | --- |
| Claro | `B8C0CC` (aresta `E0E6F0`) | placas grandes, arestas |
| Médio | `6A707C` | cascas dos membros |
| Escuro | `24306A` navy / `2E3440` grafite | peitoral, juntas |
| Destaque (Glow) | `3CF0FF` ciano; `FF5AD0` magenta | visor, reator / luzes da cintura |
| Acento | faixa de aviso `F2C230` + `1A1A1A` | ombro direito |

## Olhos
Sem olhos de desenho: o **visor** é o rosto. Faixa larga ciano com 2 linhas.

## Detalhes-assinatura
- "07" estampado num ombro.
- Faixa de aviso amarela e preta em chevron no outro ombro.

## Efeitos e aura (Legendary)
- Ambiente: `core_pulse` ciano no reator; faíscas curtas nas juntas dos ombros a cada 5 s; `ring_glow` fino no visor. Até 6 emissores.
- Ação sugerida **Power Up**: agacha e o reator carrega → anel ciano no chão e faíscas → vapor das juntas. Confirmar com o que já existe no pacote do v3 antes de mudar.

## Animação
Usar os clipes do pacote v3 aprovado (Idle, Walk, Happy e especial). Não refazer.

## Proibições (da direção de arte)
Argila com adesivos, papel-alumínio amassado, brinquedo inflado, membros em tubo, fileiras de peças idênticas, preto sobre preto.

## Referências a reusar
`MechaTitan_referencia` (modelo aprovado), `QuantumCat_alvo-2d` e `AIOverlord_alvo-2d` (cor da linha CyberCity), prompt 1 de `referencias-pets-lendarios-miticos/LEIA-ME_referencias-e-prompts.md`, cabeçalho de `fichas-originais/ficha-L4-CyberCity.md`.
