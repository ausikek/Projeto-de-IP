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
