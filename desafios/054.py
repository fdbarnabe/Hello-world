import datetime
maiorID = 0
menorID = 0
today = datetime.date.today().year
for a in range(1,8):
    idade= int(input("Qual o ano de nascimento: "))
    if today - idade >= 21:
        maiorID += 1
    elif today - idade < 21:
        menorID += 1
print(f"{maiorID} são maiores de idade, e {menorID} são menores de idade")