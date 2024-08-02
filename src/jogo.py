import pygame
import random as r
from .utils import *
from .config import LAR, ALT, FUNDO,  PLAYER, COMIDA, RAIO_COMIDA, RAIO_INICIAL_JOGADOR
from .objetos import Player, Food, Notification
from .graficos import Graficos
import time 

class GameLoop:
    
    def __init__(self):
        self.pos_x = LAR // 2
        self.pos_y = ALT // 2
        self.target_x = self.pos_x  
        self.target_y = self.pos_y 
        self.raio = RAIO_INICIAL_JOGADOR
        self.velocidade = 0.2
        self.fator_i = 0.01 #  SUAVIDADE DA INTERPOL
        self.jogando = True
        self.comidinhas = []
        self.animacoes = []
        self.g = Graficos()
        self.notif:Notification = None
        self.tempo_inicial = time.time()
        self.tutorial = 0 #Steps do tutorial

    def run(self):
        pygame.init()
        pygame.display.set_caption("Buraco negro")

        tela = pygame.display.set_mode((LAR, ALT))
        
        self.g.setup(tela)
        
        self.notif = Notification("Boa sorte!")

        player = Player(self.raio, PLAYER)

        while self.jogando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.jogando = False
            

            #Timers
            if self.tutorial > 2: 
                agora = time.time()
                if(agora - self.tempo_inicial > 6 * (self.tutorial + 1)):
                    if self.tutorial == 0:
                        self.notif = Notification("A cada bolinha vermelha que você absorve, você cresce.")
                    elif self.tutorial == 1:
                        self.notif = Notification("Seu objetivo é absorver o máximo de bolinhas vermelhas!")
                    self.tutorial += 1
                #depois adicionar mais prompts a medida que a gente for adicionando coisa ao jogo

            player.radius = self.raio
            
            velocidade_x = 0
            velocidade_y = 0
            
            keys = pygame.key.get_pressed()
            
            if(keys[pygame.K_RIGHT] or keys[pygame.K_d]):
                velocidade_x += 1
            if(keys[pygame.K_LEFT] or keys[pygame.K_a]):
                velocidade_x -=  1
            if(keys[pygame.K_UP] or keys[pygame.K_w]):
                velocidade_y -= 1
            if(keys[pygame.K_DOWN] or keys[pygame.K_s]):
                velocidade_y += 1
            
            if(velocidade_x != 0 and velocidade_y != 0):
                velocidade_x *= (2 ** (1/2)) / 2
                velocidade_y *= (2 ** (1/2)) / 2
            velocidade_x *= self.velocidade
            velocidade_y *= self.velocidade

            self.target_x += velocidade_x
            self.target_y += velocidade_y

            self.pos_x += (self.target_x - self.pos_x) * self.fator_i
            self.pos_y += (self.target_y - self.pos_y) * self.fator_i

            if(len(self.comidinhas) < 100):            
                if(r.randint(1,100) == 1):
                    comida_x = r.randint(int(self.pos_x) - RAIO_COMIDA, int(self.pos_x) + RAIO_COMIDA)
                    comida_y = r.randint(int(self.pos_y) - RAIO_COMIDA, int(self.pos_y) + RAIO_COMIDA)
                    nova_comida = Food(comida_x, comida_y, r.randint(1, int(self.raio * 0.4)), COMIDA)
                    if(r.randint(1,5) == 5):nova_comida.info["textura"] = "tigrinho"
                    self.comidinhas.append(nova_comida)
        
            tela.fill(FUNDO)
            #Antes de desenhar, atualizar os offsets
            self.g.update(self.pos_x, self.pos_y)
            
            player.draw(self.g)

            for food_anim in self.animacoes:
                food_anim.draw_anim(self.g)
                food_anim.radius -= 0.025
                if(food_anim.radius < 1):
                    self.animacoes.remove(food_anim)

            
            for comida in self.comidinhas:
                dx = comida.x - self.pos_x
                dy = comida.y - self.pos_y
                pitagoras = ((dx ** 2) + (dy ** 2)) ** 0.5

                if pitagoras < self.raio:
                    self.animacoes.append(comida)
                    self.comidinhas.remove(comida)
                    self.raio = ((3.141 * (self.raio ** 2) + 3.141 * (comida.radius ** 2)) / 3.141) ** (1/2)
                try:
                    if pitagoras > RAIO_COMIDA:
                        self.comidinhas.remove(comida) #deletar a comida que tiver longe do cara
                except:
                    pass
                comida.draw_spawn(self.g)

            if self.notif != None:
                self.notif.draw(tela)
                self.notif.alterar_opacidade(0.0003)
                if self.notif.pegar_opacidade() < 0.005:
                    self.notif = None
            
            pygame.display.flip()
