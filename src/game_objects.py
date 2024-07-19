import pygame
from .settings import LAR, ALT

class Player:

    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color


    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius))


class Food:
    
        def __init__(self, x, y, radius, color):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
    

        def draw_anim(self, surface):
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius))


        def draw_spawn(self, surface, off_x, off_y):
            pygame.draw.circle(surface, self.color, (int(self.x - off_x) + LAR // 2, int(self.y - off_y) + ALT // 2), self.radius)