# **Nexus das Musas: Project Handover Document (Status Report)**

Este documento serve como ponto de partida para qualquer nova sessão de desenvolvimento. Ele resume o estado atual do projeto, as regras definidas e os próximos passos para a implementação do MVP.

## **1\. Visão Geral do Projeto**

* **Título:** Nexus das Musas.  
* **Gênero:** TCG Tático (Card Game) com mecânicas de JRPG (Turnos, Party de 4).  
* **Identidade Visual:** "Unapologetically Sexy & Stylish". Foco em personagens femininas (Musas) com diversidade estética, roupas detalhadas e animações "breathing" (Live2D). O *fanservice* é integrado à mecânica via sistema de "Ruptura" (roupas rasgadas ao perder escudo).  
* **Plataforma Alvo:** Web / Mobile (MVP).

## **2\. Estado Atual do Desenvolvimento (Concluído)**

### **A. Core Design (Regras Fechadas \- v0.2)**

O sistema de jogo foi totalmente definido e "estressado" via simulações de texto.

* **Deck:** 16 Cartas fixas.  
* **Arena:** 4 Slots de Frente (Tag-Team). Morte permanente na partida (Exaustão).  
* **Economia:**  
  * **PC (Pontos de Clímax):** Usado APENAS para o sistema de *Boost* (Nível 1, 2, 3).  
  * **Habilidades Táticas:** Usam *Cooldown* (CD), não custam PC.  
* **Mecânicas Chave:**  
  * **Break:** Zerar escudo do inimigo causa atordoamento, dano x2 e cancela passivas/status.  
  * **Boost:** Potencializa ataques ou ativa Ultimates (Nível 3).

### **B. Conteúdo Criativo (32 Cartas Finalizadas)**

Dois decks completos foram criados, com Lore, Visual, Atributos e Kits de Habilidade definidos.

* **Deck 1 (Protagonistas):** 16 Cartas focadas em heroísmo, diversidade e sinergia positiva.  
* **Deck 2 (Sindicato das Sombras):** 16 Cartas focadas em controle, temas dark/uniformes e punição.

### **C. Arquivos de Referência (A "Bíblia" do Projeto)**

O projeto está modularizado em 4 arquivos essenciais que **DEVEM** ser carregados no início de um novo chat:

1. nexus\_core\_rules.md: O motor de regras e diretrizes visuais.  
2. nexus\_deck\_1\_protagonists.md: Catálogo das cartas 01 a 16\.  
3. nexus\_deck\_2\_syndicate.md: Catálogo das cartas 17 a 32\.  
4. nexus\_future\_roadmap.md: Planejamento de longo prazo (Evolução 3★-\>5★, Expansões).

## **3\. Próximos Passos (To-Do List para o Próximo Chat)**

O design lógico está **CONCLUÍDO**. A próxima fase é a **IMPLEMENTAÇÃO TÉCNICA**.

### **Passo 1: Estruturação de Dados (JSON)**

* **Ação:** Converter os arquivos .md das cartas em um arquivo cards.json estruturado.  
* **Objetivo:** Criar a base de dados que o código do jogo vai ler.  
* **Estrutura Sugerida:**  
  {  
    "id": "01\_isabella",  
    "name": "Isabella, a Noiva do Éden",  
    "element": "Pureza",  
    "stats": { "hp": 100, "shield": 4, "speed": "Low" },  
    "skills": { ... }  
  }

### **Passo 2: Prototipagem do Motor de Batalha**

* **Ação:** Criar um script (Python ou JS) simples que simule uma batalha automática lendo o JSON.  
* **Objetivo:** Validar se os Cooldowns e Danos funcionam matematicamente sem intervenção humana.

### **Passo 3: Desenvolvimento de Assets (Prompting)**

* **Ação:** Usar os "Roteiros Visuais" dos arquivos de Deck para gerar prompts de IA de Imagem.  
* **Objetivo:** Criar as ilustrações conceituais das 32 cartas.

## **4\. Notas Importantes para a IA/Desenvolvedor**

* **Não altere as regras de Cooldown:** A mudança de "Custo de Mana" para "Cooldown" nas Táticas foi vital para o ritmo. Mantenha isso.  
* **Atenção à Seraphina:** A Ultimate dela requer código específico ("Check if Shield \> 0").  
* **Atenção à Jinx:** O status "Vodu" deve ter um *listener* que o remove se Jinx entrar em estado de Break.