import os

def limpar():
    
    if os.name == "nt":
        os.system("cls")
    
    elif os.name == "posix":
        os.system("clear")

    print("Iniciando...")

def displaysegundos(s):
	if s < 0:
		s = 0
	minutos = s // 60
	segundos = s - (minutos * 60)
	mins = ""
	if minutos < 10:
		mins = f"0{minutos}"
	else:
		mins = str(minutos)
	segs = ""
	if segundos < 10:
		segs = f"0{segundos}"
	else:
		segs = str(segundos)
	return f"{mins}:{segs}"
