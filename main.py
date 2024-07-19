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
velocidade = 0.1
jogando = True
def circulo(x, y, raio, cor):
    pygame.draw.circle(tela, cor, (int(x), int(y)), int(raio))

while jogando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False
    #atualizar a posicao do  bro
    keys = pygame.key.get_pressed()
    velocidade_x = 0
    velocidade_y = 0
    if(keys[pygame.K_RIGHT]):
        velocidade_x += 1
    if(keys[pygame.K_LEFT]):
        velocidade_x -=  1
    if(keys[pygame.K_UP]):
        velocidade_y -= 1
    if(keys[pygame.K_DOWN]):
        velocidade_y += 1
    
    velocidade_x *= velocidade
    velocidade_y *= velocidade
    pos_x += velocidade_x
    pos_y += velocidade_y

    #desenhar
    tela.fill(FUNDO)
    circulo(pos_x, pos_y, raio, PLAYER)
    circulo(0,0, 100, COMIDA) #circulo aleatorio so p saber se ele ta se mexendo
    pygame.display.flip()

print("saindo")
"""
Todo:

[X] - Abrir o pygame 
[X] - Mostrar o player 
[X] - Fazer o player andar
[ ] - Fazer a camera seguir o mano player 
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