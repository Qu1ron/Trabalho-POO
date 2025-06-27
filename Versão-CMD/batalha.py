from classes import Mago, Guerreiro, Arqueiro
import os
from time import sleep

# Nesse arquivo temos a lógica da batalha

def imprimir_arte(arte_p1,arte_p2):
    linhas_p1 = arte_p1.strip().splitlines() #divide as artes em uma lista de linhas
    linhas_p2 = arte_p2.strip().splitlines()

    for x in range(len(linhas_p1)): #intera x no range da quantidade de linhas
        print(linhas_p1[x]+ " " + linhas_p2[x]) #imprime as duas artes linha a linha


# Funcao pra limpar o terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Criamos uma classe batalha onde teremos os métodos e os atributos que serão utéis
class Batalha:
    def __init__(self, jogador1, jogador2):
        # armazenando os jogadores 1 e 2
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        # definindo uma variável de controle para turno
        self.turno = 1

        # Definindo que será o atacante entre os dois jogadores, aquele que tiver mais velocidade será o atacante
        if(jogador1.Speed >= jogador2.Speed):
            self.atacante = jogador1
            self.defensor = jogador2
        else:
            self.atacante = jogador2
            self.defensor = jogador1
        print(f"\n{self.atacante.name} é mais rápido e começa o combate!\n")
        sleep(1.5)
    
    # Método identificar_habilidades, que basicamente retorna as skills de algum jogador
    def identificar_habilidades(self, jogador):
        if isinstance(jogador, Mago):
            return jogador.skills_mago
        if isinstance(jogador, Guerreiro):
            return jogador.skills_guerreiro
        if isinstance(jogador, Arqueiro):
            return jogador.skills_arqueiro
    
    # Método para cada jogador escolher seus ataques
    def escolher_ataque(self, jogador):
        # chama o método mostrar_habilidades e armazena as habilidades do jogador
        skills = self.identificar_habilidades(jogador)
        print(f"{jogador.name} escolha o seu ataque: ")

        # enumerate cria um objeto enumerado, onde teremos um indíce e um nome, por exemplo: {0 : "Bola de fogo"}
        for i, nome in enumerate(skills):
            skill = skills[nome]
            # Printando todos os ataques com um índice atualiado e seus respectivos dano e Mana necessária
            print(f"{i + 1} - {nome} (Dano: {skill['Damage']}, Mp: {skill['Mp']})")
        
        # Aqui temos um loop para garantir que o jogador escolha um ataque válido conforme sua Mana
        while True:
            escolha = int(input("Ataque escolhido: "))
            # Crio uma lista com as chaves de skill que são os nomes e armazeno conforme a escolha do ataque
            skill_nome = list(skills.keys())[escolha - 1]
            # Armazenando a skill escolhida
            skill = skills[skill_nome]

            # Se a mana do jogador for suficiente, nós diminuimos a mana necessária do ataque e então retornamos o dano e o nome da skill
            if jogador.Mp >= skill['Mp']:
                jogador.Mp -= skill['Mp']
                return skill['Damage'], "com "+skill_nome
            else:
                print("Mana insuficiente...\n")
                return jogador.ataque(), "Usando Ataque basico no lugar"

    # Método para representar o que irá acontecer em cada turno da batalha

    def turnos(self):
        
        limpar_tela()

        imprimir_arte(self.atacante.arte,self.defensor.arte_inv)

        print(f"\n=== (Turno {self.turno} | Vez de: {self.atacante.name}) ===")
        print(f"\nJogador 2: {self.defensor.name}")
        print(f"\nHp: {self.defensor.Hp}/{self.defensor.MaxHp}")
        print(f"Mp: {self.defensor.Mp}/{self.defensor.MaxMp}\n")
        print("="*50)
        print(f"\nJogador 1: {self.atacante.name}")
        print(f"\nHp: {self.atacante.Hp}/{self.atacante.MaxHp}")
        print(f"Mp: {self.atacante.Mp}/{self.atacante.MaxMp}\n")
        print("="*50)
        print(f"{self.atacante.name} escolha sua ação:\n")
        print("1- Ataque Basico\n2- Skills\n3- Dodge\n")

        self.choice_atk = 0

        while self.choice_atk not in [1, 2, 3]:

            self.choice_atk = int(input("-> "))
            

            match self.choice_atk:

                case 1:
                    self.dmg_atacante = self.atacante.ataque()
                    self.nome_skill_atacante = ""
                    break


                case 2:
                    sleep(0.25)
                    self.dmg_atacante, self.nome_skill_atacante = self.escolher_ataque(self.atacante)
                    break

                case 3:
                    print(f"Voce tentara se esquivar...")
                    sleep(1)
                    break
                
                #Equivalente ao caso default no switch do c
                case _:
                    print("Escolha entre uma das 3 opcoes...\n")
        sleep(0.5)
        
        limpar_tela()
        imprimir_arte(self.defensor.arte,self.atacante.arte_inv)
        print()
        print("="*50)
        print(f"--- (Turno {self.turno} | Vez de: {self.defensor.name}) ---")
        print(f"\nJogador 1: {self.atacante.name}")
        print(f"\nHp: {self.atacante.Hp}/{self.atacante.MaxHp}")
        print(f"Mp: {self.atacante.Mp}/{self.atacante.MaxMp}\n")
        print("="*50)
        print(f"\nJogador 2: {self.defensor.name}")
        print(f"\nHp: {self.defensor.Hp}/{self.defensor.MaxHp}")
        print(f"Mp: {self.defensor.Mp}/{self.defensor.MaxMp}\n")
        print("="*50)
        print(f"{self.defensor.name} escolha sua ação:\n")
        print("1- Ataque Basico\n2- Skills\n3- Dodge\n")

        self.choice_defe = 0

        while self.choice_defe not in [1, 2, 3]:

            self.choice_defe = int(input("-> "))

            match self.choice_defe:

                case 1:
                    self.dmg_defe = self.defensor.ataque()
                    self.nome_skill_defe = ""
                    break


                case 2:
                    sleep(0.25)
                    self.dmg_defe, self.nome_skill_defe = self.escolher_ataque(self.defensor)
                    break

                case 3:
                    break

                case _:
                    print("Escolha entre uma das 3 opcoes...\n")
                
        
        if (self.choice_atk == 1 or self.choice_atk == 2) and (self.choice_defe == 1 or self.choice_defe == 2):
            print(f"{self.atacante.name} Atacou {self.nome_skill_atacante}!\n")
            sleep(1.5)
            print(f"{self.defensor.name} tomou {max(1,self.dmg_atacante-self.defensor.Defense/2)} de dano!\n")
            sleep(1.5)
            self.defensor.damage_cal(self.dmg_atacante)
            if not self.defensor.survived():
                return
            else:
                print(f"{self.defensor.name} Atacou {self.nome_skill_defe}!\n")
                sleep(1.5)
                print(f"{self.atacante.name} tomou {max(1,self.dmg_defe-self.atacante.Defense/2)} de dano!\n")
                sleep(1.5)
                self.atacante.damage_cal(self.dmg_defe)

        if self.choice_atk == 3 and (self.choice_defe == 1 or self.choice_defe == 2):
            print(f"\n{self.defensor.name} Atacou {self.nome_skill_defe}!\n")
            sleep(1.5)
            print(f"{self.atacante.name} tenta se esquviar...\n")
            sleep(1.5)
            if self.atacante.dodge():
                print("Esquivou! dano evitado\n")
                sleep(1.5)
            else:
                print("Esquiva falhou...\n")
                sleep(1.5)
                print(f"{self.atacante.name} tomou {max(1,self.dmg_defe-self.atacante.Defense/2)} de dano!\n")
                sleep(1.5)
                self.atacante.damage_cal(self.dmg_defe)
        
        if (self.choice_atk == 1 or self.choice_atk == 2) and self.choice_defe == 3:
            print(f"\n{self.atacante.name} Atacou {self.nome_skill_atacante}!\n")
            sleep(1.5)
            print(f"{self.defensor.name} tenta se esquviar...\n")
            sleep(1.5)
            if self.defensor.dodge():
                print("Esquivou! dano evitado\n")
                sleep(1.5)
            else:
                print("Esquiva falhou...\n")
                print(f"{self.defensor.name} tomou {max(1,self.dmg_atacante-self.defensor.Defense/2)} de dano!\n")
                sleep(1.5)
                self.defensor.damage_cal(self.dmg_atacante)

        if self.choice_atk == 3 and self.choice_defe == 3:
            print("\n...Por que diabos os dois estao rolando pelo chão ao mesmo tempo? >,<'")
            sleep(1.5)
        
        self.turno += 1
        
        print("\nRecuperando mana...")

        # Recuperação para o Atacante
        if isinstance(self.atacante, Mago) and self.atacante.Mp <= self.atacante.MaxMp - 20:
            self.atacante.Mp += 20
        elif isinstance(self.atacante, Arqueiro) and self.atacante.Mp <= self.atacante.MaxMp - 12:
            self.atacante.Mp += 12
        elif isinstance(self.atacante, Guerreiro) and self.atacante.Mp <= self.atacante.MaxMp - 5:
            self.atacante.Mp += 5
        
        # Recuperação para o Defensor
        if isinstance(self.defensor, Mago) and self.defensor.Mp <= self.defensor.MaxMp - 20:
            self.defensor.Mp += 20
        elif isinstance(self.defensor, Arqueiro) and self.defensor.Mp <= self.defensor.MaxMp - 12:
            self.defensor.Mp += 12
        elif isinstance(self.defensor, Guerreiro) and self.defensor.Mp <= self.defensor.MaxMp - 5:
            self.defensor.Mp += 5

            sleep(2)

    
    # No método iniciar, teremos o loop inicial do jogo:
    def iniciar(self):
        limpar_tela()
        # Loop para garantir que o jogo só acabe até um dos jogadores morrerem
        while self.jogador1.survived() and self.jogador2.survived():
            # Dentro do loop, chamamos o método para o turno:
            self.turnos()

        # Fora do loop, temos um if/else para saber quem venceu: 
        if self.jogador1.survived():
            print(f"{self.jogador1.name} venceu !")
        else:
            print(f"{self.jogador2.name} venceu !")
