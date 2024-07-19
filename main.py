import src.game_loop as src
from src.utils import limpar

def main():

    limpar()

    game_loop = src.GameLoop()

    game_loop.run()

    print("Fim do jogo")

if __name__ == "__main__":
    main()