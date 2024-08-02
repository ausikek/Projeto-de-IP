import pygame 
import time
import os

LAR = 500
ALT = 500
BACKGROUND = (0,0,0) # preto, mas isso nao vai nem aparecer

#Não importar outros modulos aqui, tentar deixar isso aqui o mais "portavel" possivel pela simplicidade

class TelaInicial:
    def __init__(self):
        self.nao_iniciou = True
        self.run()

    def run(self):
        pygame.init()
        pygame.display.set_caption("Tela inicial")

        tela = pygame.display.set_mode((LAR, ALT))
        i = 0
        image1 = pygame.image.load(os.path.join('assets', '1.png'))
        image2 = pygame.image.load(os.path.join('assets', '2.png'))
        while self.nao_iniciou:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.nao_iniciou = False

            keys = pygame.key.get_pressed()

            if(keys[pygame.K_RETURN] or keys[pygame.KSCAN_KP_ENTER]):
                self.nao_iniciou = False
        
            tela.fill(BACKGROUND)
            if((pygame.time.get_ticks() // 500) % 2 == 0):
                tela.blit(image1, (0,0)) #A cada segundo troca
            else:
                tela.blit(image2, (0,0))
            #Antes de desenhar, atualizar os offsets
            pygame.display.flip()




