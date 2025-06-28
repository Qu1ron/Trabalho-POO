import random
from Data import *

# Nesse arquivo temos as classes

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
        self.Hp = self.Hp - max(1, dano - (self.Defense / 2)) #max garante que o dano não seja menor que 1
        
    
        #funcao pro dodge, tem que testar pra ver se a formula funciona bem   
    def dodge(self):
        self.base_chance = max(5, min(5 + (self.Speed * 4), 85)) #Nova formula pro dodge, dando mais importancia a speed
        self.sorte = random.randint(0,3) #gera um numero aleatorio [0, 3] 
        self.chance_desvio = self.base_chance + self.sorte #Entao se voce tem 100 de speed, 50 de base chance + de 0 a 10 dependendo da sorte
        self.rolagem = random.randint(0,100) #pensa num dado de 100 lados, se o numero que sair for menor que a chance, vc toma :P
        print(f"\n{self.chance_desvio} > {self.rolagem}?")
        if self.chance_desvio > self.rolagem:
            return True
        else: 
            return False
        
        
class Mago(Personagem):
    def __init__(self, name, MaxHp = 180, Hp = 180, MaxMp = 200, Mp = 200, Defense = 15, Speed = 10, skills = Ataques, arte = mago_arte, arte_invertida = mago_inv_arte):
        super().__init__(name, MaxHp, Hp, MaxMp, Mp, Defense, Speed)
        self.arte = arte
        self.arte_inv = arte_invertida
        
        #pra cada nome e detalhe no dicionario Ataques, se detalhe = 'Mago' agente copia todos os detalhes da skill com esse nome
        self.skills_mago = {}
        for nome, detalhe in skills.items(): 
            if detalhe['Classe'] == 'Mago':
                self.skills_mago[nome] = detalhe
    
    def ataque(self):
        if self.Mp >=8:
            self.dmg = 25
            self.Mp -= 8
        else:
            print("Não tem mana suficiente... Cajadada vai servir!")
            self.dmg = super().ataque() # Chama o ataque básico padrão 
        return int(self.dmg)
    
class Guerreiro(Personagem):
    def __init__(self, name, MaxHp = 250, Hp = 250, MaxMp = 100, Mp = 100, Defense = 40, Speed = 7, skills = Ataques, arte = guerreiro_arte, arte_invertida = guerreio_inv_arte):
        super().__init__(name, MaxHp, Hp, MaxMp, Mp, Defense, Speed)
        self.arte = arte
        self.arte_inv = arte_invertida


        self.skills_guerreiro = {}
        for nome, detalhe in skills.items():
            if detalhe['Classe'] == 'Guerreiro':
                self.skills_guerreiro[nome] = detalhe
        
    def ataque(self):
        if self.Mp >= 10:
            self.dmg = 20
            self.Mp -= 10
        else:
            print("Lhe falta Vigor!")
            self.dmg = super().ataque() #Chama o ataque básico padrão
        return int(self.dmg)
        
class Arqueiro(Personagem ) :
    def __init__ (self ,name, MaxHp = 200 ,Hp = 200 ,MaxMp = 150 ,Mp = 150 ,Defense = 25 ,Speed = 16 ,skills = Ataques, arte = arqueiro_arte, arte_invertida = arqueiro_inv_arte) :
        super().__init__( name ,MaxHp ,Hp ,MaxMp ,Mp ,Defense ,Speed)
        self.arte = arte
        self.arte_inv = arte_invertida
        
        self.skills_arqueiro = {}
        for nome ,detalhe in skills.items():
            if detalhe ['Classe'] == 'Arqueiro' :
                self.skills_arqueiro[nome] = detalhe
                    
    def ataque (self ):
        if self.Mp >= 12:
            self.dmg = 26
            self.Mp -= 12
        else:
            print("Perdeu o foco! Um simples arranhão ")
            self.dmg = super().ataque()
        return int(self.dmg)
