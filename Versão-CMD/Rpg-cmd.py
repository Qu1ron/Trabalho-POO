import time 
import sys
import numpy as np
import random
from Data import *


#Log de batalha
class log:
    def __init__(self,arquivo="battle_log.txt" ) :
        self.terminal = sys.stdout 
        #Para não "perder" a saída do terminal pois ela será modificada, originalmente a saída é configurada para o terminal
        self.log_file = open(arquivo,"w",encoding="utf-8") 
        #Abertura do arquivo para que possa ser escrito
        #utf-8 é a biblioteca geral e moderna que abrange vários caracteres 
        
    def write (self,message ) :
    #"Duplica" o texto para aparecer tanto no terminal quanto no arquivo
        self.terminal.write(message) 
        #Sem isso não apareceria os print no terminal
        self.log_file.write(message) 
        #Escreve no arquivo de texto
        
    def flush(self ) :
    #Envio imediato das informações
        self.terminal.flush() 
        #Para o terminal
        self.log_file.flush() 
        #Para o arquivo


sys.stdout = log("battle_log.txt")
#stdout é a saída do código, originalmente é o terminal mas aqui eu transformo em um obj da classe Log


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
        self.base_chance = min(0.5*self.speed, 90) #chance basica, sem nenhuma alteracao 50%, o min limita a 90% a chance base
        self.sorte = random.randint(0,10) #gera um numero aleatorio [0, 10]
        self.chance_desvio = self.base_chance + self.sorte #Entao se voce tem 100 de speed, 50 de base chance + de 0 a 10 dependendo da sorte
        self.rolagem = random.randint(0,100) #pensa num dado de 100 lados, se o numero que sair for menor que a chance, vc toma :P
        if self.chance_desvio < self.rolagem:
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
        return self.dmg
    
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
        return self.dmg
        
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
