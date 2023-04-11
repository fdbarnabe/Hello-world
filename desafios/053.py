texto = str(input(f"Digite o texto para saber se é uma frase palíndromo: "))
textosemespaço = texto.replace(" ","")
tminus=textosemespaço.lower()
tinverso=tminus[::-1]
if tinverso==tminus:
    print(f"É palíndromo")
else:
    print(f"Não é palíndromo")