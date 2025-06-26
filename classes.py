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
        self.dmg = 12
        return self.dmg
        
        #Funcao pra checar se o Personagem esta vivo
    def survived(self):
        if self.Hp <= 0:
            return False
        else:
            return True
    
        #funcao pra calcular o dano
    def damage_cal(self,dano):
        self.Hp = self.Hp - max(1, dano - (self.Defense / 2)) #max garante que o dano não seja menor que 0
        
    
        #funcao pro dodge, tem que testar pra ver se a formula funciona bem   
    def dodge(self):
        self.base_chance = min(1.0*self.Speed, 90) #chance basica, sem nenhuma alteracao 50%, o min limita a 90% a chance base
        self.sorte = random.randint(0,10) #gera um numero aleatorio [0, 10]
        self.chance_desvio = self.base_chance + self.sorte #Entao se voce tem 100 de speed, 50 de base chance + de 0 a 10 dependendo da sorte
        self.rolagem = random.randint(0,100) #pensa num dado de 100 lados, se o numero que sair for menor que a chance, vc toma :P
        print(f"{self.chance_desvio} > {self.rolagem}?")
        if self.chance_desvio > self.rolagem:
            return True
        else: 
            return False
        
        
class Mago(Personagem):
    def __init__(self, name, MaxHp = 110, Hp = 110, MaxMp = 150, Mp = 150, Defense = 15, Speed = 10, skills = Ataques):
        super().__init__(name, MaxHp, Hp, MaxMp, Mp, Defense, Speed)
        
        #pra cada nome e detalhe no dicionario Ataques, se detalhe = 'Mago' agente copia todos os detalhes da skill com esse nome
        self.skills_mago = {}
        for nome, detalhe in skills.items(): 
            if detalhe['Classe'] == 'Mago':
                self.skills_mago[nome] = detalhe
    
    def ataque(self):
        if self.Mp >=5:
            self.dmg = 20
            self.Mp -= 5
        else:
            print("Não tem mana suficiente... Cajadada vai servir!")
            self.dmg = super().ataque() # Chama o ataque básico padrão 
        return int(self.dmg)
    
class Guerreiro(Personagem):
    def __init__(self, name, MaxHp = 100, Hp = 100, MaxMp = 110, Mp = 110, Defense = 30, Speed = 7, skills = Ataques):
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
            self.dmg = super().ataque() #Chama o ataque básico padrão
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
            self.dmg = super().ataque()
        return self.dmg
