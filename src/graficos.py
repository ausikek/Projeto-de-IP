import pygame
import os
from .config import LAR, ALT

class Graficos:

    def __init__(self):
        self.texturas = {"tigrinho" : pygame.image.load(os.path.join('assets', f'boss_final.jpg'))}
        self.scale = 1

    def setup(self, tela):
        self.tela = tela

    def update(self, off_x, off_y): #universalizar o offset , pra nao ficar mandando o mesmo offset como argumento varias vezes, só usar desse aqui
        self.off_x = off_x
        self.off_y = off_y

    def textura(self, x,y, textura, tamanho_x = 0, tamanho_y = 0, tem_offset = True):
        image = self.texturas[textura]

        if tamanho_x != 0 and tamanho_y != 0:
            image = pygame.transform.scale(image, (tamanho_x, tamanho_y))
        tamanho = image.get_size()
        x -= tamanho[0] // 2
        y -= tamanho[1] // 2
        if tem_offset:
            self.tela.blit(image, (int(x - self.off_x) + LAR // 2, int(y - self.off_y) + ALT // 2))
        else:
            self.tela.blit(image, (int(x), int(y)))

    def circle(self, color, raio, x, y, tem_offset = True): #Manter uma classe pra ficar desenhando tudo, facilitando acesso a scale e readability do codigo
        if tem_offset: 
            pygame.draw.circle(self.tela, color, (int(x - self.off_x) + LAR // 2, int(y - self.off_y) + ALT // 2), raio * self.scale)
        else:
            pygame.draw.circle(self.tela, color, (int(x), int(y)), raio * self.scale)