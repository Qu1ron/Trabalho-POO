# RPG Realm (Versão CMD)

## Sobre o Jogo

RPG Realm é um jogo de batalha em turnos, totalmente em modo texto, desenvolvido em Python. Utilizando a criatividade e a nostalgia dos jogos clássicos de terminal, este projeto foca na lógica de combate e na estratégia. Os jogadores escolhem seus heróis, cada um representado por uma arte ASCII, e se enfrentam em uma batalha de inteligência e gerenciamento de recursos.

## Funcionalidades

-   **Sistema de Combate por Turnos**: Uma mecânica de batalha estratégica e bem balanceada, onde cada ação conta.
-   **Seleção de Personagens**: Escolha entre três classes com atributos e habilidades distintas:
    -   **Guerreiro**: Especialista em defesa e sobrevivência.
    -   **Mago**: Mestre do dano mágico, com alto poder de ataque.
    -   **Arqueiro**: Ágil e rápido, com foco em velocidade e esquiva.
-   **Arte ASCII**: Cada personagem possui uma arte única e detalhada em formato de texto, que é exibida durante os combates para uma maior imersão.
-   **Sistema de Log**: Todas as ações da batalha, incluindo os inputs do jogador, são salvas no arquivo `battle_log.txt` para que a partida possa ser revisada.

## Como Executar o Jogo

Para rodar este jogo, você só precisa ter o Python instalado.

### Requisitos
-   Python 3.x

### Execução
1.  **Obtenha os Arquivos**: Baixe e extraia todos os arquivos do projeto (`.py`) para um mesmo diretório.
2.  **Execute o Jogo**: Abra um terminal ou prompt de comando, navegue até o diretório onde você salvou os arquivos e execute o seguinte comando:
    ```bash
    python main.py
    ```

## Estrutura do Projeto

-   `main.py`: O ponto de entrada do jogo. Responsável por apresentar as classes, gerenciar a seleção de personagens e iniciar a batalha.
-   `classes.py`: Contém as definições de classe para `Personagem`, `Mago`, `Guerreiro` e `Arqueiro`, incluindo seus atributos base e métodos de ação como `ataque`, `damage_cal` e `dodge`.
-   `batalha.py`: Orquestra todo o fluxo do combate. Controla os turnos, a escolha de ações dos jogadores e a resolução de dano e efeitos.
-   `Data.py`: Funciona como um banco de dados do jogo, armazenando o dicionário de `Ataques` e as artes ASCII de cada personagem.
-   `impressao.py`: Um módulo utilitário que redefine a saída padrão do sistema para registrar todos os `print` e `input` do terminal em um arquivo de log.

## Distribuição de Tarefas

A equipe foi dividida com as seguintes responsabilidades principais:

-   **Lucas (Lógica Central e Personagens)**:
    -   Desenvolvimento da classe base `Personagem` e da classe especializada `Mago`, definindo atributos e habilidades.
    -   Implementação da lógica principal do combate por turnos (`batalha.py`) e da apresentação visual com artes ASCII.

-   **Júlia (Lógica de Interação e Personagens)**:
    -   Criação da classe `Arqueiro`, com foco em mecânicas de velocidade e esquiva.
    -   Desenvolvimento do sistema de log de batalha (`impressao.py`), responsável por registrar todas as ações e interações do jogo.

-   **Pedro (Estrutura de Jogo e Personagens)**:
    -   Criação da classe `Guerreiro`, com foco em mecânicas de defesa e resistência.
    -   Desenvolvimento da estrutura inicial do jogo, incluindo a seleção de personagens (`main.py`) e a configuração da classe `Batalha`.