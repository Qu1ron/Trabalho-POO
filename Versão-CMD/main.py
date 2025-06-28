from Data import *
from classes import *
from batalha import *
from impressao import *

# função para definir a classe do jogador
def escolher_classe(nome_jogador):
    # Loop para garantir que os usuários escolham suas classes
    while True:
        print(f"\n{nome_jogador}, escolha sua classe: ")
        print("1 - Mago")
        print("2 - Guerreiro")
        print("3 - Arqueiro")
        escolha = int(log_obj.entrada("Classe escolhida: "))

        if escolha == 1:
            nome_personagem = input("Escolha um nome para seu Mago: ")
            return Mago(nome_personagem)
        elif escolha == 2:
            nome_personagem = input("Escolha um nome para seu Guerreiro: ")
            return Guerreiro(nome_personagem)
        elif escolha == 3:
            nome_personagem = input("Escolha um nome para seu Arqueiro: ")
            return Arqueiro(nome_personagem)
        else:
            print("Opção inválida, digite novamente.")

# Função para mostrar os guerreiros e seus respectivos atributos/ataques
def mostrar_guerreiros():
    print("\n=== CLASSES: ===\n")
    
    print("Mago:")
    print("  - HP: 110")
    print("  - MP: 150")
    print("  - Defesa: 15")
    print("  - Velocidade: 10")
    print("  - Ataques:")
    for nome, detalhe in Ataques.items():
        if detalhe["Classe"] == "Mago":
            print(f"  • {nome}: Dano {detalhe['Damage']}, MP {detalhe['Mp']}")
    
    print("\nGuerreiro:")
    print("  - HP: 100")
    print("  - MP: 110")
    print("  - Defesa: 30")
    print("  - Velocidade: 7")
    print("  - Ataques:")
    for nome, detalhe in Ataques.items():
        if detalhe["Classe"] == "Guerreiro":
            print(f"  • {nome}: Dano {detalhe['Damage']}, MP {detalhe['Mp']}")
    
    print("\nArqueiro:")
    print("  - HP: 100")
    print("  - MP: 125")
    print("  - Defesa: 20")
    print("  - Velocidade: 15")
    print("  - Ataques:")
    for nome, detalhe in Ataques.items():
        if detalhe["Classe"] == "Arqueiro":
            print(f"  • {nome}: Dano {detalhe['Damage']}, MP {detalhe['Mp']}")
    
    print("\n============================")


    
if __name__ == "__main__":
    print("------------------------------------")
    print("------------------------------------")
    mostrar_guerreiros()
    print("------------------------------------")
    print("------------------------------------")


    # Variáveis para armazenar as escolhas dos jogadores
    jogador1 = escolher_classe("Jogador 1")
    jogador2 = escolher_classe("Jogador 2")

    # Batalha iniciada
    batalha1 = Batalha(jogador1, jogador2)
    batalha1.iniciar()
    log_obj.fechar()
    #fechando o arquivo no final do código e restaurando a saída do programa para o terminal novamente
