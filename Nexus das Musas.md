# Nexus das Musas: Design Document (Conceito Inicial)

## 1. Visão Geral e Estética

*   **Core Concept:** Um Card Game Tático (TCG) com alma de JRPG.
*   **Visual:** "Unapologetically Sexy & Stylish". A direção de arte foca na beleza feminina, sensualidade e poder. As ilustrações não são estáticas; elas possuem animações "breathing" (estilo Live2D), onde o movimento do cabelo, a física da roupa e as expressões faciais reagem ao dano ou à vitória.
*   **Atmosfera:** Um multiverso caótico e estritamente feminino/matriarcal. O "High Tech" convive com o "High Fantasy". O elo comum é a figura da Musa: entidades de poder absoluto e beleza hipnotizante. Não existem figuras masculinas; a tensão e o conflito surgem das diferentes ideologias e formas de poder entre as Musas.

## 2. Estrutura do Deck e Arena

### O Deck (O "Círculo Interno")
*   **Tamanho:** Exatamente 16 Cartas.
*   **Composição:** O deck é composto puramente por Musas.
*   **Objetivo:** A vitória é obtida por Exaustão Total (eliminar as 16 Musas do oponente).

### A Arena (O Palco)
*   **Formato:** 4 Slots de Frente (Frontline).
*   **Dinâmica de Substituição:** Funciona como um Tag-Team Battle. Quando uma Musa ativa chega a 0 de Vitalidade, ela sai de cena. O jogador escolhe uma reserva.
*   **Regra de Entrada:** A nova Musa entra no final da fila de turnos (Presença zerada naquele round) para dar uma janela de oportunidade ao oponente.

## 3. Mecânicas de JRPG (O Sistema de Combate)

### A. Sistema de Ruptura (The Break System)
Cada Musa possui um valor de Escudo de Postura (ex: 3 a 5 pontos) e fraquezas elementais.
*   **Break (Ruptura):** Quando o Escudo chega a 0:
    1.  A arte da carta muda para uma versão "Distressed" (roupas rasgadas, expressão ofegante, pose vulnerável).
    2.  A Musa perde seu próximo turno.
    3.  Recebe 200% de dano.
    4.  Perde a Habilidade Passiva até recuperar a postura.

### B. Sistema de Clímax (The Boost System)
A cada turno, o jogador ganha 1 Ponto de Clímax (PC). Você pode gastar até 3 PCs para "Carregar" uma ação de uma Musa.
*   **Nível 1 (Básico):** Dano normal.
*   **Nível 2 (Sensual):** Dano x2 + Efeito visual aprimorado.
*   **Nível 3 (Provocativo):** Dano x4 + Habilidade Ultimate (Animação especial de tela cheia focado no sex appeal da personagem).

### C. Sistema de Links (A Posição Importa)
*   Musas adjacentes formam Vínculos.
*   Se você move uma Musa para um slot diferente (gasta 1 turno), o vínculo se quebra e um novo se forma.

## 4. Regras de Atributos (Stats Base)

*   **Vitalidade (HP):** Resistência física.
*   **Sedução (ATK):** Poder ofensivo (Físico ou Mágico unificados).
*   **Graça (DEF/Evasion):** Capacidade de mitigar dano ou evitar ataques completamente. Musas leves têm alta Graça; Musas pesadas têm alta Vitalidade.
*   **Presença (SPD):** Determina a ordem do turno.
*   **Líbido (CRIT/Status):** A chance de causar dano crítico ou aplicar efeitos negativos (veneno, sono, encanto).

## 5. Elementos e Interações (Ciclo Atualizado)

*   **Paixão (Fogo)** > Derrete > **Caos (Tech)**
*   **Caos (Tech)** > Desestabiliza > **Mistério (Sombra)**
*   **Mistério (Sombra)** > Corrompe > **Pureza (Luz)**
*   **Pureza (Luz)** > Apaga > **Paixão (Fogo)**

### Ressonâncias (Passivas de Campo)
*   **2+ Paixão:** +10% ATK global.
*   **2+ Mistério:** Inimigos iniciam com -1 Escudo.
*   **2+ Pureza:** Regeneração de HP no fim do turno.
*   **2+ Caos:** +15% Crítico global.

## 6. Padronização para MVP (Template de Carta)

Para garantir o desenvolvimento ágil, toda carta terá a seguinte estrutura rígida de habilidades:

*   **Ataque Básico (Gerador):** Causa dano leve/médio. Gera +1 PC extra ou recupera um pouco de Escudo.
*   **Habilidade Tática (Consumidor):** Custo baixo/médio. Foca na utilidade (Curar, Debuffar, Stun, Proteger).
*   **Passiva (Identidade):** Um efeito sempre ativo que define o arquétipo (ex: "Ganhe ATK quando sofrer dano").
*   **Ultimate (Clímax):** Só ativada com Boost Nível 3. O golpe final visual e mecânico.

## 7. Diretriz de Design Visual (Mandatório)

Para manter a consistência e a diversidade do "harém", toda carta deve incluir os campos Físico & Detalhes e Background no seu roteiro visual.

*   **Objetivo:** Evitar "same face/body syndrome" e garantir diversidade de belezas, aproveitando o "Universo Sem Limites".
*   **Físico & Detalhes:** Tipo de Corpo (Petite, Curvy, Tall, Athletic, Mature, Plus-size, etc.), Tom de Pele (Reais ou Fantásticos: Azul, Metálico, Onix, etc.), Cabelo e Expressão Facial Típica.
*   **Background:** Definição do gradiente e degradê de cores que compõem o fundo da carta, refletindo a aura e a lore da personagem.

## 8. Protótipos de Cartas (Lote 1 - Fundadoras)

### Carta 01: Isabella, a Noiva do Éden
*   **Tags:** Realeza, Pura.
*   **Elemento:** Pureza.
*   **Visual Script:**
    *   **Lore:** Uma noiva abandonada no altar de um paraíso tropical, cuja devoção se tornou um escudo mágico.
    *   **Físico & Detalhes:** Curvy & Soft. Pele bronzeada de sol, cabelos castanhos longos e ondulados (estilo praiano), lábios cheios, expressão de êxtase/devoção ingênua. Olhos cor de mel.
    *   **Background:** Gradiente suave de Areia Dourada (base) para Azul Turquesa Cristalino (topo), evocando uma praia divina.
    *   **Vestimenta:** Vestido de renda branco "sereia", extremamente justo e translúcido nas coxas e abdômen. Véu longo que flutua como água viva. Segura um buquê que goteja luz.
    *   **Pose Idle:** Mãos juntas em prece sobre o peito, olhando para cima com ar de êxtase, quadris levemente deslocados.
    *   **Ruptura (Break):** O vestido rasga na lateral da perna até a cintura, o véu cai sobre os olhos, ela se ajoelha abraçando o próprio corpo.
*   **Kit MVP:**
    *   **Básico:** Toque de Seda - Dano leve de Luz.
    *   **Tática:** Voto de Fidelidade - Redireciona ataques das vizinhas para si por 1 turno. Aumenta a própria Graça.
    *   **Passiva:** Mártir - Ganha 1 PC sempre que recebe um Crítico.
    *   **Ultimate:** Lua de Mel Eterna - Cura total da party e remove todos os debuffs. Animação de um beijo soprado que vira uma chuva de pétalas.

### Carta 02: Professora Lylian, a Fada do Hipnotismo
*   **Tags:** Autoridade, Mística.
*   **Elemento:** Mistério.
*   **Visual Script:**
    *   **Lore:** Uma entidade antiga que assume a forma de educadora para disciplinar mentes caóticas.
    *   **Físico & Detalhes:** Petite-Curvy. Baixa estatura mas com curvas acentuadas, pele pálida, cabelos cor-de-rosa pastel em corte 'bob' assimétrico. Expressão severa por cima dos óculos, mas mordendo o lábio inferior.
    *   **Background:** Degradê holográfico de Rosa Neon (centro) para Roxo Profundo (bordas), simulando um efeito de hipnose visual.
    *   **Vestimenta:** Bikini micro xadrez (estilo saia escolar desconstruída), óculos na ponta do nariz, meias 3/4 brancas. Asas de fada holográficas.
    *   **Pose Idle:** Inclinada sobre uma mesa invisível, batendo uma régua na palma da mão, olhando por cima dos óculos.
    *   **Ruptura (Break):** Óculos caem e quebram, o bikini desamarra nas costas (seguro apenas por magia/sorte), expressão de choque e vergonha.
*   **Kit MVP:**
    *   **Básico:** Chamada Oral - Dano de Sombra.
    *   **Tática:** Detenção - O inimigo alvo perde 1 Ponto de Clímax e sua vez na timeline é atrasada.
    *   **Passiva:** Olhar 43 - Inimigos que atacam Lylian têm chance de errar (Miss).
    *   **Ultimate:** Alucinação Coletiva - Todos os inimigos atacam a si mesmos no próximo turno. A tela fica rosa-choque com corações partidos.

### Carta 03: Ignis, a Nadadora do Inferno
*   **Tags:** Atleta, Caos.
*   **Elemento:** Caos.
*   **Visual Script:**
    *   **Lore:** Uma competidora que nadou em rios de lava para vencer uma aposta contra um demônio.
    *   **Físico & Detalhes:** Tall & Athletic. Alta, ombros definidos, pernas longas e musculosas. Pele negra brilhante de suor/óleo. Cabelos curtos platinados (quase brancos) para contraste. Olhos em chamas.
    *   **Background:** Gradiente intenso de Vermelho Magma (base) para Preto Obsidiana (topo), com faíscas subindo.
    *   **Vestimenta:** Maiô "high-cut" metálico vermelho-sangue que parece derreter/gotejar. Pele suada e brilhante. Touca de natação estilizada como uma coroa.
    *   **Pose Idle:** Alongando os braços acima da cabeça (destacando a silhueta), respirando ofegante como pós-exercício.
    *   **Ruptura (Break):** O maiô cede na alça, ela cobre o peito com o braço, sentada na borda da piscina de lava, exausta.
*   **Kit MVP:**
    *   **Básico:** Braçada - Dano Físico rápido.
    *   **Tática:** Aquecimento - Sacrifica 10% do próprio HP para aumentar o ATK em 50%.
    *   **Passiva:** Adrenalina - Quanto menor o HP, maior a Velocidade (Presença).
    *   **Ultimate:** Tsunami de Magma - Dano massivo em área. Animação de um mergulho que explode a tela em vapor.

### Carta 04: Morgana, a Bruxa da Lingerie Final
*   **Tags:** Mística, Gótica.
*   **Elemento:** Mistério.
*   **Visual Script:**
    *   **Lore:** Uma feiticeira que trocou sua alma pela juventude eterna e o guarda-roupa infinito do vazio.
    *   **Físico & Detalhes:** Slim & Mature. Corpo esguio, elegante, "femme fatale". Pele muito branca (quase translúcida). Cabelos negros longuíssimos que flutuam sozinhos. Olhos violeta frios.
    *   **Background:** Degradê radial de Violeta Cósmico (centro) para Preto Vazio (bordas), com estrelas distantes.
    *   **Vestimenta:** Corset vitoriano negro desabotoado, cinta-liga complexa, meias 7/8 rasgadas propositalmente. Flutua sem tocar o chão.
    *   **Pose Idle:** Flutuando de costas, olhando para o jogador por cima do ombro, brincando com uma taça de vinho cósmico.
    *   **Ruptura (Break):** Cai no chão, o corset se abre, a maquiagem borra com lágrimas negras.
*   **Kit MVP:**
    *   **Básico:** Sussurro - Dano de Sombra que ignora defesa.
    *   **Tática:** Maldição da Beleza - Reduz a DEF e o ATK de um alvo.
    *   **Passiva:** Sadismo - Recupera HP quando um inimigo entra em Ruptura (Break).
    *   **Ultimate:** Evaporação - Dano em área. Se matar um inimigo, ganha turno extra.

## 9. Protótipos de Cartas (Lote 2 - Expansão)

### Carta 05: Carmen, a Rosa de Sangue
*   **Tags:** Artista, Perigosa.
*   **Elemento:** Paixão.
*   **Visual Script:**
    *   **Lore:** Uma dançarina de flamenco que usa o ritmo cardíaco dos seus amantes como música.
    *   **Físico & Detalhes:** Average & Voluptuous. Pele oliva, cabelos negros presos em coque severo com uma rosa vermelha viva. Pinta (sinal) acima do lábio. Olhos penetrantes.
    *   **Background:** Gradiente quente de Laranja Pôr-do-Sol (centro) para Vermelho Sangue (bordas).
    *   **Vestimenta:** Jaqueta de toureiro dourada aberta sem nada por baixo, saia de babados vermelha com fenda profunda até o quadril.
    *   **Pose Idle:** Pose de dança dramática, uma mão no ar estalando os dedos, a outra no quadril, rosa na boca.
    *   **Ruptura (Break):** A saia rasga revelando a perna toda, o cabelo solta do coque caindo no rosto, ela segura o peito ofegante.
*   **Kit MVP:**
    *   **Básico:** Zapateado - Dano de Fogo que aumenta a cada uso consecutivo.
    *   **Tática:** Olé! - Entra em postura de "Contra-Ataque" por 1 turno (Esquiva do próximo ataque e devolve o dano).
    *   **Passiva:** Coração Ardente - Ganha ATK extra se houver outra carta de Paixão na mesa.
    *   **Ultimate:** Dança da Morte - Dano massivo em alvo único. Se matar, reseta o cooldown.

### Carta 06: Valentine, a Enfermeira de Látex
*   **Tags:** Autoridade, Cyber.
*   **Elemento:** Pureza.
*   **Visual Script:**
    *   **Lore:** Uma androide médica reprogramada para "curar" o tédio com injeções de adrenalina pura.
    *   **Físico & Detalhes:** Thick & Artificial. Corpo sintético com proporções exageradas, pele branca plástica/brilhante. Cabelos azul-clínico neon. Rosto com linhas de união de placas sutis.
    *   **Background:** Gradiente asséptico de Branco Puro (centro) para Ciano Hospitalar (bordas).
    *   **Vestimenta:** Uniforme de enfermeira feito inteiramente de látex branco translúcido e justo. Segura uma seringa gigante com líquido rosa brilhante.
    *   **Pose Idle:** Segurando a seringa como uma arma, verificando o nível do líquido, piscando um olho digital.
    *   **Ruptura (Break):** O látex rasga revelando circuitos dourados por baixo da "pele", vazando fluido refrigerante azul.
*   **Kit MVP:**
    *   **Básico:** Coleta de Sangue - Dano leve, cura a si mesma em 50% do dano.
    *   **Tática:** Estimulante - Remove todos os debuffs de uma aliada e concede "Imunidade" por 1 turno.
    *   **Passiva:** Esterilização - Se Valentine estiver com HP cheio, curas da party são 20% mais fortes.
    *   **Ultimate:** Cirurgia de Emergência - Ressuscita uma Musa caída com 1 de HP (Única forma de reviver no jogo).

### Carta 07: Bunny, a Dealer do Destino
*   **Tags:** Cyber, Jogadora.
*   **Elemento:** Caos.
*   **Visual Script:**
    *   **Lore:** Proprietária de um cassino flutuante onde se aposta memórias em vez de dinheiro.
    *   **Físico & Detalhes:** Petite & Athletic. Baixinha, ágil, pele dourada. Orelhas de coelho reais (mutação). Cauda de pompom. Rosto travesso/malicioso.
    *   **Background:** Gradiente frenético de Neon Verde (Matrix) e Roxo Laser, com dados e cartas flutuando.
    *   **Vestimenta:** Traje clássico de "Playboy Bunny" mas feito de neon e fibra de carbono. Gravata borboleta que é um holograma. Meia-calça arrastão brilhante.
    *   **Pose Idle:** Sentada em um dado gigante flutuante, jogando moedas para o alto e pegando.
    *   **Ruptura (Break):** Cai do dado, orelhas baixas e tristes, meia-calça rasgada nos joelhos, tentando recolher as fichas do chão.
*   **Kit MVP:**
    *   **Básico:** Lançar Dados - Dano aleatório (1 a 6 hits).
    *   **Tática:** Aposta Alta - Gasta 2 PC. Rola uma chance de 50/50: Ou cura totalmente a party ou causa dano na própria party.
    *   **Passiva:** Sorte de Principiante - Começa a batalha com +20% de Esquiva (Graça).
    *   **Ultimate:** Jackpot - Dano de Caos em todos os inimigos. O dano é multiplicado pelo número do turno atual.

### Carta 08: Roxy, a Mecânica Grease-Monkey
*   **Tags:** Cyber, Urbana.
*   **Elemento:** Paixão.
*   **Visual Script:**
    *   **Lore:** Construtora de mechas que prefere o calor da forja e o cheiro de óleo a qualquer palácio.
    *   **Físico & Detalhes:** Muscular & Toned. Braços definidos, abdômen trincado, pele suja de graxa. Cabelos ruivos presos em rabo de cavalo despojado. Sardas no rosto.
    *   **Background:** Gradiente industrial de Ferrugem (base) para Cinza Fumaça (topo).
    *   **Vestimenta:** Macacão de mecânico amarrado na cintura (topless por baixo, apenas fitas isolantes ou top muito pequeno encardido). Botas pesadas. Chave inglesa gigante.
    *   **Pose Idle:** Limpando o suor da testa com o antebraço, apoiada na chave inglesa, mascando chiclete.
    *   **Ruptura (Break):** O macacão cai da cintura revelando roupa íntima improvisada, ela tenta se cobrir com a ferramenta, suja e vulnerável.
*   **Kit MVP:**
    *   **Básico:** Marretada - Dano Físico pesado. Quebra escudos com mais facilidade.
    *   **Tática:** Overclock - Aumenta o ATK de uma aliada "Cyber" ou "Caos", mas ela toma dano a cada turno.
    *   **Passiva:** Manutenção - Repara o próprio Escudo de Postura em 1 ponto se não atacar no turno.
    *   **Ultimate:** Combustão Espontânea - Incendeia o campo. Todas as Musas (aliadas e inimigas) tomam dano, mas as de Paixão ganham Boost grátis.

## 10. Protótipos de Cartas (Lote 3 - Novas Fronteiras)

### Carta 09: Scarlett, a General de Ferro
*   **Tags:** Autoridade, Militar.
*   **Elemento:** Paixão.
*   **Visual Script:**
    *   **Lore:** Uma comandante invicta que trata a guerra como uma dança de submissão e conquista.
    *   **Físico & Detalhes:** Tall & Curvy (Amazonian). Muito alta, postura imponente, pele clara. Cabelos loiros platinados em corte militar impecável. Cicatriz fina no lábio que ela realça com batom vermelho.
    *   **Background:** Gradiente de Cinza Aço (base) para Vermelho Alerta (topo), com mira laser cruzando o fundo.
    *   **Vestimenta:** Quepe militar, jaqueta de general aberta revelando lingerie tática preta, botas de cano alto até a coxa, luvas de couro. Segura um riding crop (chicote curto).
    *   **Pose Idle:** Batendo o chicote na bota ritmicamente, olhando o jogador de cima para baixo com desprezo e desejo.
    *   **Ruptura (Break):** De joelhos, quepe caído, a jaqueta rasgada no ombro, olhar furioso e humilhado.
*   **Kit MVP:**
    *   **Básico:** Disciplina - Dano físico. Se o alvo já agiu no turno, causa dano extra.
    *   **Tática:** Ordem Unida - Todas as aliadas atacam o alvo selecionado com 50% de dano (Gang Up).
    *   **Passiva:** Supremacia - Enquanto Scarlett estiver com HP acima de 50%, todas as cartas "Autoridade" ganham +10% de ATK.
    *   **Ultimate:** Bombardeio Tático - Chama um ataque aéreo. Causa dano massivo e deixa o campo em chamas (Dano por turno em todos).

### Carta 10: Viper, a Lótus Venenosa
*   **Tags:** Perigosa, Mística.
*   **Elemento:** Mistério.
*   **Visual Script:**
    *   **Lore:** Uma assassina de aluguel que usa toxinas derivadas de sua própria pele para eliminar alvos.
    *   **Físico & Detalhes:** Slim & Flexible. Corpo de contorcionista, pele pálida coberta por tatuagens de serpentes que se movem. Olhos verdes reptilianos.
    *   **Background:** Gradiente tóxico de Verde Ácido (base) para Roxo Fumaça (topo).
    *   **Vestimenta:** Traje ninja "shibari" (cordas) misturado com seda translúcida preta. Máscara que cobre apenas a boca. Kunais presas nas coxas.
    *   **Pose Idle:** Pendurada de cabeça para baixo por um fio de seda (ou corda), balançando suavemente, brincando com uma adaga.
    *   **Ruptura (Break):** As cordas se soltam, ela cai no chão, máscara rasgada revelando um sorriso triste, tatuagens parando de se mover.
*   **Kit MVP:**
    *   **Básico:** Picada - Dano leve + Veneno (Dano contínuo por 3 turnos).
    *   **Tática:** Cortina de Fumaça - Concede "Evasão Perfeita" (Desvia do próximo ataque) a si mesma.
    *   **Passiva:** Sangue Frio - Causa 30% a mais de dano em inimigos envenenados.
    *   **Ultimate:** Beijo da Morte - Executa instantaneamente um inimigo com menos de 20% de HP. Se falhar, causa dano crítico.

### Carta 11: Melody, a Diva Holográfica
*   **Tags:** Artista, Cyber.
*   **Elemento:** Pureza.
*   **Visual Script:**
    *   **Lore:** Uma IA de entretenimento que ganhou consciência e agora busca a "nota perfeita" que pode reescrever a realidade.
    *   **Físico & Detalhes:** Petite & Soft. Aparência jovem e kawaii. Pele levemente luminescente/perolada. Cabelos multicoloridos que mudam de cor com o ritmo da música de fundo.
    *   **Background:** Gradiente vibrante de Ciano Elétrico (centro) para Rosa Chiclete (bordas), com equalizadores gráficos pulsando.
    *   **Vestimenta:** Roupa de "Idol" futurista: saia de luz sólida, fones de ouvido de orelha de gato, microfone flutuante. Muito brilho e paetês digitais.
    *   **Pose Idle:** Fazendo poses de "V" com os dedos, mandando beijos para a câmera, flutuando em um palco de luz.
    *   **Ruptura (Break):** A projeção falha (glitch), partes do corpo ficam pixeladas ou transparentes, expressão de choro digital (lágrimas de código).
*   **Kit MVP:**
    *   **Básico:** Nota Aguda - Dano Sônico (Luz) em todos os inimigos. Dano baixo, mas quebra escudos de área.
    *   **Tática:** Encore! - Uma aliada que já agiu ganha mais uma ação imediata neste turno (Gasta 2 PC).
    *   **Passiva:** Hype - A cada turno que passa, o ganho de PC do jogador aumenta temporariamente.
    *   **Ultimate:** Turnê Mundial - "Stuna" (Atordoa) todos os inimigos com um show de luzes por 1 turno.

### Carta 12: Medusa, a Sucateira Mutante
*   **Tags:** Mística, Urbana.
*   **Elemento:** Caos.
*   **Visual Script:**
    *   **Lore:** Uma habitante dos esgotos tóxicos que sofreu mutações, transformando seu cabelo em cabos de dados vivos e cobras de neon.
    *   **Físico & Detalhes:** Plus-size & Dangerous. Corpo voluptuoso, "soft tummy", coxas grossas. Pele esverdeada ou cinza-urbano. O "cabelo" são tentáculos biomecânicos.
    *   **Background:** Gradiente sujo de Verde Limo (base) para Amarelo Radioativo (topo), com canos gotejando.
    *   **Vestimenta:** Apenas trapos estratégicos e placas de sinalização de trânsito usadas como armadura/roupa.
    *   **Pose Idle:** Sentada em um trono de lixo tecnológico, comendo uma maçã brilhante (radioativa), enquanto os tentáculos de cabelo mexem em sucata ao redor.
    *   **Ruptura (Break):** O trono desmorona, ela cai de costas, os tentáculos se recolhem com medo, cobrindo o rosto e o corpo.
*   **Kit MVP:**
    *   **Básico:** Chicote de Dados - Dano de Caos. Rouba 1 ponto de Escudo do inimigo e dá para Medusa.
    *   **Tática:** Petrificar Sistema - O inimigo alvo não pode usar Habilidades Especiais (apenas ataque básico) por 2 turnos.
    *   **Passiva:** Reciclagem - Se uma carta (amiga ou inimiga) for destruída, Medusa cura 20% de HP.
    *   **Ultimate:** Jardim de Pedra - Transforma o terreno. Todos os inimigos perdem -2 de Velocidade e tomam dano de veneno ácido.

## 11. Protótipos de Cartas (Lote 4 - O Ciclo Final)

### Carta 13: Seraphina, a Santa de Vidro
*   **Tags:** Realeza, Mística.
*   **Elemento:** Pureza.
*   **Visual Script:**
    *   **Lore:** Uma guardiã celestial que se tornou tão pura que sua pele virou cristal, deixando sua alma exposta.
    *   **Físico & Detalhes:** Tall & Ethereal. Extremamente alta e esbelta. Pele translúcida (como vidro fosco) onde se vê luz fluindo nas "veias". Sem pelos, aparência divina e alienígena.
    *   **Background:** Gradiente etéreo de Branco Prisma (centro) para Arco-íris Pastel (bordas), com efeito de refração de luz.
    *   **Vestimenta:** Nada além de vitrais flutuantes estrategicamente posicionados que orbitam seu corpo como uma armadura de arte sacra.
    *   **Pose Idle:** Flutuando com os braços abertos (crucifixo), os vitrais girando lentamente, expressão de paz absoluta.
    *   **Ruptura (Break):** Os vitrais se estilhaçam, rachaduras aparecem em sua pele de vidro, luz vazando pelas fendas como "sangue".
*   **Kit MVP:**
    *   **Básico:** Refração - Dano de Luz. Se a vida estiver cheia, reflete dano em um segundo inimigo.
    *   **Tática:** Santuário de Cristal - Cria um escudo na Musa aliada com menos vida. Se o escudo quebrar, causa dano de estilhaços.
    *   **Passiva:** Transparência - Imune a Veneno e Sangramento (não tem sangue orgânico).
    *   **Ultimate:** Juízo Final - Consome todo o Escudo de Postura restante para causar dano massivo baseado na defesa.

### Carta 14: Dominique, a Viúva Negra
*   **Tags:** Realeza, Perigosa.
*   **Elemento:** Mistério.
*   **Visual Script:**
    *   **Lore:** Uma aristocrata que enterrou cinco maridos (e cinco impérios). Ela tece o destino e usa as almas como fios.
    *   **Físico & Detalhes:** Mature & Voluptuous. Mulher madura, elegante, curvas sinuosas. Pele pálida de porcelana. Lábios pintados de preto. Segura uma piteira longa.
    *   **Background:** Gradiente gótico de Vinho Bordeaux (base) para Preto Veludo (topo), com padrão de teia sutil.
    *   **Vestimenta:** Vestido de funeral vitoriano, mas feito de renda negra transparente. Chapéu com véu curto. Joias de ônix.
    *   **Pose Idle:** Sentada em uma cadeira invisível (feita de fios de sombra), cruzando as pernas lentamente, soltando fumaça roxa.
    *   **Ruptura (Break):** A renda rasga no busto, o véu cai, ela perde a compostura e mostra presas vampíricas ou olhos bestiais.
*   **Kit MVP:**
    *   **Básico:** Fio da Meada - Dano de Sombra. Reduz a Velocidade do alvo (Slow).
    *   **Tática:** Herança Maldita - Marca um inimigo. Se ele morrer em 2 turnos, Dominique ganha os buffs dele.
    *   **Passiva:** Luto - Ganha +1 PC a cada vez que uma Musa (aliada ou inimiga) é derrotada.
    *   **Ultimate:** Teia do Destino - Prende todos os inimigos (não podem trocar de posição) e drena vida deles a cada turno.

### Carta 15: Olympia, a Leoa da Arena
*   **Tags:** Atleta, Perigosa.
*   **Elemento:** Paixão.
*   **Visual Script:**
    *   **Lore:** A campeã invicta do Coliseu Solar. Ela não luta por honra, mas pelo prazer do combate físico.
    *   **Físico & Detalhes:** Muscular & Amazonian. Corpo de fisiculturista feminina, músculos definidos e oleados. Pele dourada/bronzeada. Cabelos cacheados volumosos (juba de leão).
    *   **Background:** Gradiente quente de Ouro Metálico (centro) para Laranja Poeira (bordas), evocando a areia da arena.
    *   **Vestimenta:** Apenas o essencial de uma gladiadora: ombreira de ouro, tanga de couro, sandálias romanas. O corpo é a armadura.
    *   **Pose Idle:** Flexionando o bíceps distraidamente, limpando uma espada imaginária, piscando para a "plateia" (jogador).
    *   **Ruptura (Break):** Cai sobre um joelho, sangrando no ombro, mas sorrindo com selvageria (gostando da dor).
*   **Kit MVP:**
    *   **Básico:** Golpe de Escudo - Dano Físico + Stun leve (Chance de pular turno do inimigo).
    *   **Tática:** Rugido da Vitória - Provoca todos os inimigos (Taunt) e aumenta massivamente sua própria Defesa.
    *   **Passiva:** Sangue Quente - Recupera 10% de vida sempre que causa um Break em alguém.
    *   **Ultimate:** Execução Pública - Um golpe único de dano extremo. Se matar, a plateia "joga rosas" (cura a party inteira).

### Carta 16: Pixel, a Arquiteta do Glitch
*   **Tags:** Cyber, Urbana.
*   **Elemento:** Caos.
*   **Visual Script:**
    *   **Lore:** Uma gamer que hackeou a realidade para viver dentro do jogo, mas trouxe os bugs junto com ela.
    *   **Físico & Detalhes:** Short & Geeky. Muito baixinha, postura relaxada (gamer posture). Sardas de pixel. Usa um Headset VR que mostra emoticons no visor.
    *   **Background:** Gradiente caótico de Tela Azul da Morte (fundo) com chuviscos de estática colorida (frente).
    *   **Vestimenta:** Moletom "oversized" (sem calças, apenas calcinha visível), meias listradas até o joelho (uma caída). Um controle de videogame flutuando.
    *   **Pose Idle:** Jogando no ar (digitando em teclados holográficos), comendo salgadinhos flutuantes, o corpo dando "glitch" ocasionalmente.
    *   **Ruptura (Break):** O headset cai revelando olhos cansados com olheiras, ela tenta desesperadamente reconectar os cabos, em pânico.
*   **Kit MVP:**
    *   **Básico:** Lag Spike - Dano de Caos. Tem 20% de chance de fazer o inimigo repetir a última ação (mesmo que seja ruim para ele).
    *   **Tática:** Cheat Code - Gasta 3 PC. Reseta o Cooldown da Ultimate de uma aliada.
    *   **Passiva:** Bug - 10% de chance de ignorar qualquer dano recebido (o ataque "atravessa" o modelo 3D).
    *   **Ultimate:** Blue Screen of Death - "Crasha" o jogo do oponente. Remove todos os buffs inimigos, zera os PCs deles e embaralha a posição das cartas na mesa.

## 12. Conclusão do Design (Status Final)

*   **Total de Cartas:** 16 (Deck Completo).
*   **Distribuição Elemental:**
    *   **Pureza (4):** Isabella, Valentine, Melody, Seraphina.
    *   **Mistério (4):** Lylian, Morgana, Viper, Dominique.
    *   **Paixão (4):** Carmen, Roxy, Scarlett, Olympia.
    *   **Caos (4):** Ignis, Bunny, Medusa, Pixel.
*   **Próximos Passos:** Iniciar desenvolvimento dos assets visuais e prototipagem de código.

## 13. Considerações sobre Expansão (Nota de Design)

*   **Evitar Novos Elementos:** Manter os 4 elementos base (Paixão, Mistério, Pureza, Caos) para preservar o equilíbrio matemático do sistema de Break e Ressonância.
*   **Futuro:** Introduzir "Dual-Types" (ex: Fogo/Caos) em vez de criar um 5º elemento.