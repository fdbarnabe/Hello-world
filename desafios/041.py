from datetime import date
today = date.today().year
a = int(input())
idade = today - a
if idade <=9:
    print(f""" O atleta tem {idade} anos
Categoria: Mirim.""")
elif 9< idade <=14:
    print(f""" O atleta tem {idade} anos
Categoria: Infantil.""")
elif 14< idade <=19:
    print(f""" O atleta tem {idade} anos
Categoria: Junior.""")
elif 19< idade <=20:
    print(f""" O atleta tem {idade} anos
Categoria: Sênior.""")
elif idade > 20:
    print(f""" O atleta tem {idade} anos
Categoria: Master.""")