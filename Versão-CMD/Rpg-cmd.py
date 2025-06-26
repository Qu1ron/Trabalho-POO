import time 
import sys
import numpy as np
import random
from Data import *

class Personagem:
        #Funcao para inicializar as variaveis
    def __init__(self, name, MaxHp = 100, Hp = 100, MaxMp = 100, Mp = 100, Defense = 10, Speed = 10):
        #Salvar os valores em variaveis:
        self.name = name
        self.MaxHp = MaxHp
        self.Hp = Hp
        self.MaxMp = MaxMp
        self.Mp = Mp 
        self.Defense = Defense
        self.Speed = Speed
    
        #Funcao pro ataque basico
    def ataque(self):
        self.dmg = 10
        return self.dmg
        
        #Funcao pra checar se o Personagem esta vivo
    def survived(self):
        if self.Hp <= 0:
            return False
        else:
            return True
    
        #funcao pra calcular o dano
    def damage_cal(self,dano):
        self.Hp = self.Hp - max(0, dano - self.Defense) #max garante que o dano não seja menor que 0
        
    
        #funcao pro dodge, tem que testar pra ver se a formula funciona bem   
    def dodge(self):
        self.base_chance = min(0.5*self.Speed, 90) #chance basica, sem nenhuma alteracao 50%, o min limita a 90% a chance base
        self.sorte = random.randint(0,10) #gera um numero aleatorio [0, 10]
        self.chance_desvio = self.base_chance + self.sorte #Entao se voce tem 100 de speed, 50 de base chance + de 0 a 10 dependendo da sorte
        self.rolagem = random.randint(0,100) #pensa num dado de 100 lados, se o numero que sair for menor que a chance, vc toma :P
        print(f"{self.chance_desvio} > {self.rolagem}?")
        if self.chance_desvio > self.rolagem:
            return True
        else: 
            return False
        
        
class Mago(Personagem):
    def __init__(self, name, MaxHp = 100, Hp = 100, MaxMp = 150, Mp = 150, Defense = 10, Speed = 10, skills = Ataques):
        super().__init__(name, MaxHp, Hp, MaxMp, Mp, Defense, Speed)
        
        #pra cada nome e detalhe no dicionario Ataques, se detalhe = 'Mago' agente copia todos os detalhes da skill com esse nome
        self.skills_mago = {}
        for nome, detalhe in skills.items(): 
            if detalhe['Classe'] == 'Mago':
                self.skills_mago[nome] = detalhe
    
    def ataque(self):
        if self.Mp >=5:
            self.dmg = 15
            self.Mp -= 5
        else:
            print("Não tem mana suficiente... Cajadada vai servir!")
            self.dmg = 5
        return int(self.dmg)
    
class Guerreiro(Personagem):
    def __init__(self, name, MaxHp = 100, Hp = 100, MaxMp = 100, Mp = 100, Defense = 30, Speed = 5, skills = Ataques):
        super().__init__(name, MaxHp, Hp, MaxMp, Mp, Defense, Speed)

        self.skills_guerreiro = {}
        for nome, detalhe in skills.items():
            if detalhe['Classe'] == 'Guerreiro':
                self.skills_guerreiro[nome] = detalhe
        
    def ataque(self):
        if self.Mp >= 20:
            self.dmg = 30
            self.Mp -= 20
        else:
            print("Lhe falta Vigor!")
            self.dmg = 20
        return int(self.dmg)
        
class Arqueiro(Personagem ) :
    def __init__ (self ,name, MaxHp = 100 ,Hp = 100 ,MaxMp = 125 ,Mp = 125 ,Defense = 20 ,Speed = 15 ,skills = Ataques) :
        super().__init__( name ,MaxHp ,Hp ,MaxMp ,Mp ,Defense ,Speed)
        
        self.skills_arqueiro = {}
        for nome ,detalhe in skills.items():
            if detalhe ['Classe'] == 'Arqueiro' :
                self.skills_arqueiro[nome] = detalhe
                    
    def ataque (self ):
        if self.Mp >= 12:
            self.dmg = 22
            self.Mp -= 12
        else:
            print("Perdeu o foco! Um simples arranhão ")
            self.dmg = 12
        return self.dmg


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
        print(f"{self.atacante.name} eh mais rapido, ele começa!")
    
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
                return self.atacante.ataque(), "Usando Ataque basico no lugar"

    # Método para representar o que irá acontecer em cada turno da batalha

    def turnos(self):

        print(f"___Turno {self.turno} de {self.atacante.name}___")
        print(f"\nJogador 2: {self.defensor.name}")
        print(f"\nHp: {self.defensor.Hp}/{self.defensor.MaxHp}")
        print(f"Mp: {self.defensor.Mp}/{self.defensor.MaxMp}\n")
        print("============================\n")
        print(f"\nJogador 1: {self.atacante.name}")
        print(f"\nHp: {self.atacante.Hp}/{self.atacante.MaxHp}")
        print(f"Mp: {self.atacante.Mp}/{self.atacante.MaxMp}\n")
        print("============================\n")
        print(f"{self.atacante.name} escolha sua ação:\n")
        print("1- Ataque Basico\n2- Skills\n3- Dodge\n")

        self.choice_atk = 0

        while self.choice_atk != (1 or 2 or 3):

            self.choice_atk = int(input("-> "))

            match self.choice_atk:

                case 1:
                    self.dmg_atacante = self.atacante.ataque()
                    self.nome_skill_atacante = ""
                    break


                case 2:
                    self.dmg_atacante, self.nome_skill_atacante = self.escolher_ataque(self.atacante)
                    break

                case 3:
                    print(f"Voce tentara se esquivar...")
                    break
                
                #Equivalente ao caso default no switch do c
                case _:
                    print("Escolha entre uma das 3 opcoes...\n")
                

        print("\n============================\n")
        print(f"___Turno {self.turno} de {self.defensor.name}___")
        print(f"\nJogador 1: {self.atacante.name}")
        print(f"\nHp: {self.atacante.Hp}/{self.atacante.MaxHp}")
        print(f"Mp: {self.atacante.Mp}/{self.atacante.MaxMp}\n")
        print("============================\n")
        print(f"\nJogador 2: {self.defensor.name}")
        print(f"\nHp: {self.defensor.Hp}/{self.defensor.MaxHp}")
        print(f"Mp: {self.defensor.Mp}/{self.defensor.MaxMp}\n")
        print("============================\n")
        print(f"{self.defensor.name} escolha sua ação:\n")
        print("1- Ataque Basico\n2- Skills\n3- Dodge\n")

        self.choice_defe = 0

        while self.choice_defe != (1 or 2 or 3):

            self.choice_defe = int(input("-> "))

            match self.choice_defe:

                case 1:
                    self.dmg_defe = self.defensor.ataque()
                    self.nome_skill_defe = ""
                    break


                case 2:
                    self.dmg_defe, self.nome_skill_defe = self.escolher_ataque(self.defensor)
                    break

                case 3:
                    print(f"Voce tenta se esquivar...")
                    break

                case _:
                    print("Escolha entre uma das 3 opcoes...\n")
                
        
        if (self.choice_atk == 1 or self.choice_atk == 2) and (self.choice_defe == 1 or self.choice_defe == 2):
            print(f"{self.atacante.name} Atacou {self.nome_skill_atacante}!\n")
            print(f"{self.defensor.name} tomou {max(0,self.dmg_atacante-self.defensor.Defense)} de dano!\n")
            self.defensor.damage_cal(self.dmg_atacante)
            if not self.defensor.survived():
                return
            else:
                print(f"{self.defensor.name} Atacou {self.nome_skill_defe}!\n")
                print(f"{self.atacante.name} tomou {max(0,self.dmg_defe-self.atacante.Defense)} de dano!\n")
                self.atacante.damage_cal(self.dmg_defe)

        if self.choice_atk == 3 and (self.choice_defe == 1 or self.choice_defe == 2):
            print(f"{self.defensor.name} Atacou {self.nome_skill_defe}!\n")
            print(f"{self.atacante.name} tenta se esquviar...\n")
            if self.atacante.dodge():
                print("Esquivou! dano evitado\n")
            else:
                print("Esquiva falhou...\n")
                print(f"{self.atacante.name} tomou {max(0,self.dmg_defe-self.atacante.Defense)} de dano!\n")
                self.atacante.damage_cal(self.dmg_defe)
        
        if (self.choice_atk == 1 or self.choice_atk == 2) and self.choice_defe == 3:
            print(f"{self.atacante.name} Atacou {self.nome_skill_atacante}!\n")
            print(f"{self.defensor.name} tenta se esquviar...\n")
            if self.defensor.dodge():
                print("Esquivou! dano evitado\n")
            else:
                print("Esquiva falhou...\n")
                print(f"{self.defensor.name} tomou {max(0,self.dmg_atacante-self.defensor.Defense)} de dano!\n")
                self.defensor.damage_cal(self.dmg_atacante)

        if self.choice_atk == 3 and self.choice_defe == 3:
            print("...Por que diabos os dois estao rolando pelo chão ao mesmo tempo? >,<'")
        
        self.turno += 1

    
    # No método iniciar, teremos o loop inicial do jogo:
    def iniciar(self):
        print("------ INICIO DO COMBATE ------")
        # Loop para garantir que o jogo só acabe até um dos jogadores morrerem
        while self.jogador1.survived() and self.jogador2.survived():
            # Dentro do loop, chamamos o método para o turno:
            self.turnos()

        # Fora do loop, temos um if/else para saber quem venceu: 
        if self.jogador1.survived():
            print(f"{self.jogador1.name} venceu !")
        else:
            print(f"{self.jogador2.name} venceu !")


# função para definir a classe do jogador
def escolher_classe(nome_jogador):
    # Loop para garantir que os usuários escolham suas classes
    while True:
        print(f"\n{nome_jogador}, escolha sua classe: ")
        print("1 - Mago")
        print("2 - Guerreiro")
        print("3 - Arqueiro")
        escolha = int(input("Classe escolhida: "))

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
    print("  - HP: 100")
    print("  - MP: 150")
    print("  - Defesa: 10")
    print("  - Velocidade: 10")
    print("  - Ataques:")
    for nome, detalhe in Ataques.items():
        if detalhe["Classe"] == "Mago":
            print(f"  • {nome}: Dano {detalhe['Damage']}, MP {detalhe['Mp']}")
    
    print("\nGuerreiro:")
    print("  - HP: 100")
    print("  - MP: 100")
    print("  - Defesa: 30")
    print("  - Velocidade: 5")
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