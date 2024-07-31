import pygame
from .config import LAR, ALT
class Graficos:
    def __init__(self):
        self.scale = 1
    def setup(self, tela):
        self.tela = tela
    def update(self, off_x, off_y): #universalizar o offset , pra nao ficar mandando o mesmo offset como argumento varias vezes, só usar desse aqui
        self.off_x = off_x
        self.off_y = off_y
    def scale(self,s):
        self.scale = s
    def circle(self, color, raio, x, y, tem_offset = True): #Manter uma classe pra ficar desenhando tudo, facilitando acesso a scale e readability do codigo
        if tem_offset: 
            pygame.draw.circle(self.tela, color, (int(x - self.off_x) + LAR // 2, int(y - self.off_y) + ALT // 2), raio * self.scale)
        else:
            pygame.draw.circle(self.tela, color, (int(x), int(y)), raio * self.scale)