import pygame
import os

LAR = 500
ALT = 500
BACKGROUND = (0, 0, 0)  # preto

class TelaVitoria:
    def __init__(self):
        self.nao_iniciou = True

    def run(self):
        pygame.init()
        pygame.display.set_caption("Tela inicial")

        tela = pygame.display.set_mode((LAR, ALT))
        image1 = pygame.image.load(os.path.join('assets', '3.png'))

        while self.nao_iniciou:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]:
                return True
            elif keys[pygame.K_ESCAPE]:
                return False
        
            tela.fill(BACKGROUND)
            
            tela.blit(image1, (0, 0))
            
           

            pygame.display.flip()

        return False 