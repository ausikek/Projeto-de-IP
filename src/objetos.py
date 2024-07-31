import pygame
from .config import LAR, ALT
from .graficos import Graficos

class Notification: #Utilizar isso aqui também como um "mini tutorial". Ter notificações programadas como:
    # "Boa sorte!" no início
    # "Cuidado com a bomba nseique" quando a primeira bomba spawnar ou entrar no field of view do player
    # entre outros usos ai
    def __init__(self, texto, cor = (255,255,255)):
        self.text = texto
        self.opacity = 1.0
        self.fonte = pygame.font.Font(None, 36)
        self.cor = cor
    def pegar_opacidade(self):
        return self.opacity
    def alterar_opacidade(self, o, decrescimo = True):
        if decrescimo:
            self.opacity -= o
        else:
            self.opacity = o
    def draw(self, tela):
        opacidade = 255 * self.opacity # Valor entre 0 (transparente) e 255 (opaco)
        cor = (self.cor[0], self.cor[1], self.cor[2], opacidade)  # Branco com opacidade variável
        texto = self.fonte.render(self.text, True, cor)

        # Workaround pra pygame que não deixa nativamente vc colocar texto opacos (nao mexer)
        texto_superficie = pygame.Surface(texto.get_size(), pygame.SRCALPHA)
        texto_superficie.fill((self.cor[0], self.cor[1], self.cor[2], opacidade))
        texto_superficie.blit(texto, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        # ^ deixa como ta
        tela.blit(texto_superficie, (0, 0))

# Não mexam na classe acima, é bem simples de usar, tudo é automatico , só criar uma notificação como Notification(texto, cor) e o resto é automatico!

class Player:

    def __init__(self, radius, color): #não tem necessidade de definir player posx e posy, uma vez que nunca muda
        self.radius = radius
        self.color = color


    def draw(self, g:Graficos):
        g.circle(self.color, self.radius, LAR // 2, ALT // 2, False)
       # pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius))


class Food:
    
        def __init__(self, x, y, radius, color):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color

        def draw_anim(self, g:Graficos):
            g.circle(self.color, self.radius, int(self.x), int(self.y), False)
            #pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius))

        def draw_spawn(self, g:Graficos):
            g.circle(self.color, self.radius, int(self.x), int(self.y)) 
           # pygame.draw.circle(surface, self.color, (int(self.x - off_x) + LAR // 2, int(self.y - off_y) + ALT // 2), self.radius)