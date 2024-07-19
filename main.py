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

tela = pygame.display.set_mode((800, 600)) #largura , altura
pygame.display.set_caption("Buraco negro da morte")

fundo = (0, 0, 0) #preto
player = (255,0,0) #vermelho

jogando = True

while jogando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False
    
    #desenhar
    tela.fill(fundo)

print("saindo")
"""
Todo:

[X] - Abrir o pygame 
[ ] - Mostrar o player 
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