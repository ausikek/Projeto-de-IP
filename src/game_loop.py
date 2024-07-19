import pygame
import random as r
from .utils import *
from .settings import LAR, ALT, FUNDO, PLAYER, COMIDA, RAIO_COMIDA, RAIO_INICIAL_JOGADOR
from .game_objects import Player, Food

class GameLoop:
    
    def __init__(self):
        self.pos_x = LAR // 2
        self.pos_y = ALT // 2
        self.raio = RAIO_INICIAL_JOGADOR
        self.velocidade = 0.1
        self.jogando = True
        self.comidinhas = []
        self.animacoes = []


    def run(self):
        pygame.init()
        pygame.display.set_caption("Buraco negro da morte")

        tela = pygame.display.set_mode((LAR, ALT))

        while self.jogando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.jogando = False
                
            player = Player(LAR // 2, ALT // 2, self.raio, PLAYER)
            
            velocidade_x = 0
            velocidade_y = 0
            
            keys = pygame.key.get_pressed()
            
            if(keys[pygame.K_RIGHT]):
                velocidade_x += 1
            if(keys[pygame.K_LEFT]):
                velocidade_x -=  1
            if(keys[pygame.K_UP]):
                velocidade_y -= 1
            if(keys[pygame.K_DOWN]):
                velocidade_y += 1
            
            velocidade_x *= self.velocidade
            velocidade_y *= self.velocidade
            self.pos_x += velocidade_x
            self.pos_y += velocidade_y
                        
            if(r.randint(1,100) == 1):
                comida_x = r.randint(int(self.pos_x) - RAIO_COMIDA, int(self.pos_x) + RAIO_COMIDA)
                comida_y = r.randint(int(self.pos_y) - RAIO_COMIDA, int(self.pos_y) + RAIO_COMIDA)
                comida_pos = (comida_x, comida_y)
                self.comidinhas.append([comida_pos, r.randint(1, int(self.raio * 0.4))])
        
            tela.fill(FUNDO)
            player.draw(tela)

            for animacao in self.animacoes:
                food_anim = Food(LAR // 2, ALT // 2, animacao, COMIDA)
                food_anim.draw_anim(tela)
                
                self.animacoes[self.animacoes.index(animacao)] -= 0.025
                animacao -= 0.025
                
                if(animacao == 1):
                    self.animacoes.remove(animacao)

            for comida in self.comidinhas:
                food_spawn = Food(comida[0][0], comida[0][1], comida[1], COMIDA)

                dx = food_spawn.x - self.pos_x
                dy = food_spawn.y - self.pos_y
                pitagoras = ((dx ** 2) + (dy ** 2)) ** 0.5

                if pitagoras < self.raio:
                    self.comidinhas.remove(comida)
                    self.animacoes.append(food_spawn.radius)
                    self.raio += food_spawn.radius * 0.1
                
                food_spawn.draw_spawn(tela, self.pos_x, self.pos_y)

            pygame.display.flip()
