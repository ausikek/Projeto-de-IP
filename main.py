import src.jogo as src
from src.utils import limpar
from tela_inicial import TelaInicial
def main():
    limpar()
    TelaInicial()
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
[X] - Tela inicial
[ ] - Quao maior tu ficar, mais dispersas as comidas ficam
[ ] - Adicionar em graficos.py um load_image, pra facilitar uso de imagem

"""