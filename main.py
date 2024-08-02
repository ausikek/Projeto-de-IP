import src.jogo as src
from src.utils import limpar
from tela_inicial import TelaInicial
fazer_tela = True
def main():
    limpar()
    if fazer_tela: #depois coloco de volta, preguiça de ficar apertando enter
        TelaInicial()
    game_loop = src.GameLoop()
    game_loop.run()
    print("Fim do jogo")

if __name__ == "__main__":
    main()

"""

Todo:

[X] - graficos.py
[ ] - Camera diminui com o crescimento do teu tamanho (adicionar coeficiente de scale) (n sei se eh necessario, quando tu ficar grande vai acabar o estagio)
[ ] - A cada comida o carinha fica mais rapido
[X] - Interpolação de movimento
[ ] - Adicionar uma bombinha, pequena, que fica andando caoticamente
[ ] - Adicionar uma bomba um pouco maior e mais lenta que diminui teu tamanho
[X] - Tela inicial
[ ] - Quao maior tu ficar, mais dispersas as comidas ficam
[X] - Adicionar em graficos.py um load_image, pra facilitar uso de imagem
[X] - Notificação no canto superior esquerdo
[X] - Adicionar ao radius algo equivalente ao q tu realmente consumiu
[X] - Suporte a comidas terem texturas própias e outras informações própias

"""