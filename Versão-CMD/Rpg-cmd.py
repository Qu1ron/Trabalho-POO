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
        if Hp <= 0:
            return False
        else:
            return True
    
        #funcao pra calcular o dano
    def damage_cal(self,dano):
        self.Hp = self.Hp - (dano-self.Defense)
        
    
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
        
        
        
        
    
    
    
    
    
if __name__ == "__main__":
    pass