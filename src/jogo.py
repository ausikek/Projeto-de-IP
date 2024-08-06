import pygame
import random as r
from .utils import *
from .config import LAR, ALT, FUNDO,  PLAYER, COMIDA, RAIO_COMIDA, RAIO_INICIAL_JOGADOR
from .objetos import Player, Food, Notification
from .graficos import Graficos
import time 

class GameLoop:
    
    def __init__(self, background = None):
        self.pos_x = LAR // 2
        self.pos_y = ALT // 2
        self.target_x = self.pos_x  
        self.target_y = self.pos_y 
        self.raio = RAIO_INICIAL_JOGADOR
        self.velocidade = 4.2
        self.fator_i = 0.21 # #0.21  SUAVIDADE DA INTERPOL
        self.jogando = True
        self.comidinhas = []
        self.animacoes = []
        self.g = Graficos()
        self.notif:Notification = None
        self.tempo_inicial = time.time()
        self.tutorial = 0 #Steps do tutorial
        self.background = background
        self.tamanho = (0,0)
        self.clock = pygame.time.Clock() 
        if self.background != None:
            self.tamanho = self.g.texturas[self.background].get_size()
        self.elapsedTicks = 0
        self.raio_comida = RAIO_COMIDA

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
            if self.tutorial < 5: 
                agora = time.time()
                if(agora - self.tempo_inicial > 6 * (self.tutorial + 1)):
                    if self.tutorial == 0:
                        self.notif = Notification("A cada objeto que você absorve, você cresce.")
                    elif self.tutorial == 1:
                        self.notif = Notification("Seu objetivo é absorver o máximo de objetos!")
                    elif self.tutorial == 2:
                        self.notif = Notification("Mas cuidado, nem todos são benéficos pra você!")
                    elif self.tutorial == 3:
                        self.notif = Notification("A qualquer custo, não pegue a bandeira de greve!")
                    elif self.tutorial == 4:
                        self.notif = Notification("E cuidado com os computadores que tiverem vírus!")
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
                if(r.randint(1,15) == 1):
                    valida = False
                    nova_comida:Food = None
                    while not valida: 
                        comida_x = r.randint(int(self.pos_x) - self.raio_comida, int(self.pos_x) + self.raio_comida)
                        comida_y = r.randint(int(self.pos_y) - self.raio_comida, int(self.pos_y) + self.raio_comida)
                        raio = max(15, r.randint(1, int(self.raio * 0.4)))
                        nova_comida = Food(comida_x, comida_y, raio, COMIDA)
                        dx = comida_x - self.pos_x
                        dy = comida_y - self.pos_y
                        pitagoras = ((dx ** 2) + (dy ** 2)) ** 0.5
                        if pitagoras > self.raio:
                            #nao spawnou dentro fdo player logo ta tudo bem
                            valida = True
                    #Descobrir o tipo de comidinha
                    if(r.randint(1,5) == 1 and player.radius > 60):
                        if(r.randint(1,8) == 1):
                            nova_comida.info["textura"] = "greve"
                        else:
                            nova_comida.info["textura"] = "virus"
                    else:
                        resultado = r.randint(1,3)
                        if resultado == 1:
                            nova_comida.info["textura"] = "computador" #pc
                        elif resultado == 2:
                            nova_comida.info["textura"] = "mesa"
                        elif resultado == 3:
                            nova_comida.info["textura"] = "cadeira"
                    self.comidinhas.append(nova_comida)

            #Antes de desenhar, atualizar os offsets
            self.g.update(self.pos_x, self.pos_y)

            tela.fill(FUNDO)

            if self.background != None:
                self.g.textura(self.tamanho[0] // 2, self.tamanho[1] // 2, self.background)

            player.draw(self.g)

            for food_anim in self.animacoes:
                food_anim.draw_anim(self.g)
                food_anim.radius -= 0.525
                if(food_anim.radius < 1):
                    self.animacoes.remove(food_anim)

            
            for comida in self.comidinhas:
                dx = comida.x - self.pos_x
                dy = comida.y - self.pos_y
                pitagoras = ((dx ** 2) + (dy ** 2)) ** 0.5

                if pitagoras < self.raio and comida.radius < player.radius:
                    self.animacoes.append(comida)
                    self.comidinhas.remove(comida)
                    if(comida.info["textura"] == "virus"):
                        player.radius *= 1/2
                    if(comida.info["textura"] == "greve"):
                        exit() #fazer perder
                    else:
                        self.raio = ((3.141 * (self.raio ** 2) + 3.141 * (comida.radius ** 2)) / 3.141) ** (1/2)
                try:
                    if pitagoras > self.raio_comida:
                        self.comidinhas.remove(comida) #deletar a comida que tiver longe do cara
                except:
                    pass #por nenhum motivo, isso aqui deu errado uma vez isolada, nao faco ideia como, literal n tinha como, mas vou deicxar isso aqui
                comida.draw_spawn(self.g)

            if self.notif != None:
                self.notif.draw(tela)
                self.notif.alterar_opacidade(0.0063)
                if self.notif.pegar_opacidade() < 0.005:
                    self.notif = None
            pygame.display.flip()
            if(self.elapsedTicks % 230 == 229): #230 sendo num arbitrario so pra n printar toda hora
                print(f"{(self.elapsedTicks / (time.time() - self.tempo_inicial)):.2f} FPS | radius {player.radius}")
            self.elapsedTicks += 1
            self.clock.tick(60)
            self.raio_comida = int(RAIO_COMIDA + player.radius)
