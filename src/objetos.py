import pygame
from .config import LAR, ALT
from .graficos import Graficos

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