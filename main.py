import pygame
import os

def limpar(): #so para fins de organizar isso
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix": #breno usuario de linux
        os.system("clear")

limpar()
print("iniciando")

pygame.init()
LAR, ALT = 800, 600
tela = pygame.display.set_mode((LAR, ALT)) #largura , altura
pygame.display.set_caption("Buraco negro da morte")

FUNDO = (255, 255, 255) #branco
PLAYER = (0,0,0) #preto
COMIDA = (255, 0, 0) #vermelho
#jogador:

pos_x = LAR // 2
pos_y = ALT // 2
raio = 25

jogando = True
def circulo(x, y, raio, cor):
    pygame.draw.circle(tela, cor, (int(x), int(y)), int(raio))

while jogando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False
    
    #desenhar
    tela.fill(FUNDO)
    circulo(pos_x, pos_y, raio, PLAYER)
    pygame.display.flip()

print("saindo")
"""
Todo:

[X] - Abrir o pygame 
[X] - Mostrar o player 
[ ] - Fazer o player andar 
[ ] - Spawnar comida ao redor do player
[ ] - Detectar colisão entre player e comida
[ ] - Animação da comida caindo no buraco

(Depois de tudo estar 100% correto):

[ ] - Aprender a fazer um mapa de background
[ ] - Meio de criar objetos com texturas customizadas e tal
[ ] - Aprender a colocar esses objetos no mapa de background
[ ] - Colocar timer limite da partida de 2minutos
[ ] - Criar historinha inicial (só um prompt dizendo que joaozinho efetuou divisao por 0 na aula de ip e por isso criou um buraco negro) 
"""