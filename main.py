import src.jogo as src
from src.utils import limpar
from tela_inicial import TelaInicial
fazer_tela = True
def main():
    limpar()
    if fazer_tela:
        TelaInicial()
    game_loop = src.GameLoop() #Executar isso uma vez pra cada estagio
    game_loop.run()
    print("Fim do jogo")

if __name__ == "__main__":
    main()

"""
Todo:

[X] - Nao podem spawnar coisinhas dentro do jogador
[X] - Quao maior tu ficar, mais dispersas as comidas ficam
[ ] - Cutscene/historinha inicial
[X] - Vírus
[X] - Texturas:
    [X] - Mesa
    [X] - Cadeira
    [X] - Vírus
    [X] - Computador
    [X] - Greve
    [X] - Game over tela
[X] - Greve
[ ] - Sistema de estágio, usando um coeficiente de dificuldade que pode aumentar infinitamente se tu tiver sobrevivendo 
[X] - Prompts do tutorial
[ ] - Implementar tela de game over
[ ] - Implementar um cronômetro
[ ] - Sistema de passar de estagio
[ ] - Background que simula o chão do grad 5 gerado automaticamente

"""