import os

def limpar():
    
    if os.name == "nt":
        os.system("cls")
    
    elif os.name == "posix":
        os.system("clear")

    print("Iniciando...")