import pygame
import os

LAR = 500
ALT = 500
BACKGROUND = (0, 0, 0)  # preto

class TelaInicial:
    def __init__(self):
        self.nao_iniciou = True

    def run(self):
        pygame.init()
        pygame.display.set_caption("Tela inicial")

        tela = pygame.display.set_mode((LAR, ALT))
        image1 = pygame.image.load(os.path.join('assets', '1.png'))
        image2 = pygame.image.load(os.path.join('assets', '2.png'))
        clock = pygame.time.Clock()

        while self.nao_iniciou:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]:
                return True 
        
            tela.fill(BACKGROUND)
            if (pygame.time.get_ticks() // 500) % 2 == 0:
                tela.blit(image1, (0, 0))
            else:
                tela.blit(image2, (0, 0))

            pygame.display.flip()
            clock.tick(60)

        return False 

class TelaHistoria:
    def __init__(self):
        self.tela = pygame.display.set_mode((LAR, ALT))
        pygame.display.set_caption("História")
        self.font = pygame.font.Font(None, 24)
        self.prompts = [
            "Durante as aulas de introdução a programação do CIn,",
            "João, que aprendia python, efetuou uma divisão por zero.",
            "Isso resultou em um buraco negro na sua sala de aula (Grad 5).",
            "Controle o buraco negro para crescer e absorver tudo!"
        ]
        self.current_prompt = 0
        self.alpha = 0
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        if not self.next_prompt():
                            return True  

            self.tela.fill(BACKGROUND)
            
            a = self.font.render("Aperte enter para continuar...", True, (255, 255, 255))
            rect = a.get_rect(center=(LAR // 2, ALT - 36))
            self.tela.blit(a, rect)
            if self.current_prompt < len(self.prompts):
                text = self.font.render(self.prompts[self.current_prompt], True, (255, 255, 255))
                text.set_alpha(self.alpha)
                text_rect = text.get_rect(center=(LAR/2, ALT/2))
                self.tela.blit(text, text_rect)

                self.alpha = min(self.alpha + 2, 255)  

            pygame.display.flip()
            self.clock.tick(60)

        return True

    def next_prompt(self):
        self.current_prompt += 1
        self.alpha = 0
        if self.current_prompt >= len(self.prompts):
            return False
        return True

def main():
    pygame.init()
    tela_inicial = TelaInicial()
    if tela_inicial.run():
        tela_historia = TelaHistoria()
        tela_historia.run()
    
    pygame.quit()

if __name__ == "__main__":
    main()