import src.jogo as src
from src.utils import limpar
import tela_inicial
fazer_tela = True
def main():
    limpar()
    if fazer_tela:
        tela_inicial.main()
    game_loop = src.GameLoop(1) #Executar isso uma vez pra cada estagio
    game_loop.run()
    print("Fim do jogo")

if __name__ == "__main__":
    main()

"""
Todo:

[X] - Nao podem spawnar coisinhas dentro do jogador
[X] - Quao maior tu ficar, mais dispersas as comidas ficam
[X] - Vírus
[X] - Texturas:
    [X] - Mesa
    [X] - Cadeira
    [X] - Vírus
    [X] - Computador
    [X] - Greve
    [X] - Game over tela
[X] - Greve
[X] - Prompts do tutorial
[X] - Implementar tela de game over
[X] - Background que simula o chão do grad 5 gerado automaticamente

[X] - Cutscene/historinha inicial
[X] - Sistema de estágio, usando um coeficiente de dificuldade que pode aumentar infinitamente se tu tiver sobrevivendo
[X] - Sistema de passar de estagio

[X] - Implementar um cronômetro 
[X] - Negocios do mal se moverem levemente em estagios >= 2 


"""