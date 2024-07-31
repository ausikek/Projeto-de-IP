import pygame
import random as r
from .utils import *
from .config import LAR, ALT, FUNDO,  PLAYER, COMIDA, RAIO_COMIDA, RAIO_INICIAL_JOGADOR
from .objetos import Player, Food
from .graficos import Graficos

class GameLoop:
    
    def __init__(self):
        self.pos_x = LAR // 2
        self.pos_y = ALT // 2
        self.target_x = self.pos_x  
        self.target_y = self.pos_y  # 
        self.raio = RAIO_INICIAL_JOGADOR
        self.velocidade = 0.2
        self.fator_i = 0.01 #  SUAVIDADE DA INTERPOL
        self.jogando = True
        self.comidinhas = []
        self.animacoes = []
        self.g = Graficos()

    def run(self):
        pygame.init()
        pygame.display.set_caption("Buraco negro")

        tela = pygame.display.set_mode((LAR, ALT))
        
        self.g.setup(tela)

        while self.jogando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.jogando = False
                
            player = Player(self.raio, PLAYER)
            
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
                    comida_pos = (comida_x, comida_y)
                    nova_comida = Food(comida_x, comida_y, r.randint(1, int(self.raio * 0.4)), COMIDA)
                    self.comidinhas.append(nova_comida)
        
            tela.fill(FUNDO)
            #Antes de desenhar, atualizar os offsets
            self.g.update(self.pos_x, self.pos_y)

            player.draw(self.g)

            for animacao in self.animacoes:
                food_anim = Food(LAR // 2, ALT // 2, animacao, COMIDA) #remover isso aqui depois por motivos de cleanup, mas nao tem motivo imediato alem de reduzir uso de memoria, a nao ser que o python ja va jogar essa classe no lixo no tick seguinte, mas acho que nao eh o caso!
                food_anim.draw_anim(self.g)
                
                self.animacoes[self.animacoes.index(animacao)] -= 0.025
                animacao -= 0.025
                
                if(animacao == 1):
                    self.animacoes.remove(animacao)

            for comida in self.comidinhas: #Pq criar uma nova classe "Food" a cada tick? Não entendi a vantagem, então vou tirar
                dx = comida.x - self.pos_x
                dy = comida.y - self.pos_y
                pitagoras = ((dx ** 2) + (dy ** 2)) ** 0.5

                if pitagoras < self.raio:
                    self.comidinhas.remove(comida)
                    self.animacoes.append(comida.radius)
                    self.raio += comida.radius * 0.1
                
                comida.draw_spawn(self.g)

            pygame.display.flip()
