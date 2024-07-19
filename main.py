import pygame
import os
import random as r
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

#config

FUNDO = (255, 255, 255) #branco
PLAYER = (0,0,0) #preto
COMIDA = (255, 0, 0) #vermelho
RAIO_COMIDA = 1000
RAIO_INICIAL_JOGADOR = 25

#jogador:

pos_x = LAR // 2 # offset
pos_y = ALT // 2 # offset da camera
raio = RAIO_INICIAL_JOGADOR
velocidade = 0.1
jogando = True

# util
def circulo(x, y, raio, cor, ehplayer = False):
    global pos_x
    global pos_y
    if not (ehplayer):
        pygame.draw.circle(tela, cor, (int(x - pos_x) + LAR // 2, int(y - pos_y) + ALT // 2), int(raio))
    else:
        pygame.draw.circle(tela, cor, (int(x), int(y)), int(raio)) #sem offset, pois eh o centro da camera

comidinhas = []
animacoes = []

while jogando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False
    #atualizar a posicao do bro
    velocidade_x = 0
    velocidade_y = 0
    keys = pygame.key.get_pressed()
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
    #spawnar onde ficaria as comidinhas, 1% de chance de spawnar comida por tick
    if(r.randint(1,100) == 1):
        comida_x = r.randint(int(pos_x) - RAIO_COMIDA, int(pos_x) + RAIO_COMIDA)
        comida_y = r.randint(int(pos_y) - RAIO_COMIDA, int(pos_y) + RAIO_COMIDA)
        comida_pos = (comida_x, comida_y)
        comidinhas.append([comida_pos, r.randint(1, int(raio * 0.4))])#tamanho da comida vai ser ate 40% do teu raio

    #desenhar
    tela.fill(FUNDO)
    circulo(LAR // 2, ALT // 2, raio, PLAYER, True) 
    for animacao in animacoes:
        circulo(LAR // 2, ALT // 2, animacao, COMIDA, True)
        animacoes[animacoes.index(animacao)] -= 0.025
        animacao -= 0.025
        if(animacao == 1):
            animacoes.remove(animacao) 
    #player deve ser desenhado ANTES dos obstaculos pq ele é um buraco no chao
    for comida in comidinhas:
        dx = comida[0][0] - pos_x
        dy = comida[0][1] - pos_y
        pitagoras = ((dx ** 2) + (dy ** 2)) ** 0.5
        if pitagoras < raio:
            comidinhas.remove(comida)
            animacoes.append(comida[1])
            raio += comida[1] * 0.1
        circulo(comida[0][0], comida[0][1], comida[1], COMIDA)
        
    pygame.display.flip()

print("saindo")
"""
Todo:

[X] - Abrir o pygame 
[X] - Mostrar o player 
[X] - Fazer o player andar
[X] - Fazer a camera seguir o mano player 
[X] - Spawnar comida ao redor do player
[X] - Detectar colisão entre player e comida
[X] - Animação da comida caindo no buraco

(Depois de tudo estar 100% correto):

[ ] - Afastar a camera com o crescimento do raio do player
[ ] - Aprender a fazer um mapa de background
[ ] - Meio de criar objetos com texturas customizadas e tal
[ ] - Aprender a colocar esses objetos no mapa de background (fazer uma extensao de arquivo que no eval() é uma lista de objetos com [loc_textura, tamanho, posicao])
[ ] - Colocar timer limite da partida de 2minutos
[ ] - Criar historinha inicial (só um prompt dizendo que joaozinho efetuou divisao por 0 na aula de ip e por isso criou um buraco negro) 
"""