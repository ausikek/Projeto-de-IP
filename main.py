import src.jogo as src
from src.utils import limpar

def main():

    limpar()

    game_loop = src.GameLoop()

    game_loop.run()

    print("Fim do jogo")

if __name__ == "__main__":
    main()

"""

Todo:

[X] - graficos.py
[ ] - Camera diminui com o crescimento do teu tamanho (adicionar coeficiente de scale)
[ ] - A cada comida o carinha fica mais rapido
[ ] - Interpolação de movimento
[ ] - Adicionar uma bombinha, pequena, que fica andando caoticamente
[ ] - Adicionar uma bomba um pouco maior e mais lenta que diminui teu tamanho
[ ] - Tela inicial
[ ] - Quao maior tu ficar, mais dispersas as comidas ficam

"""