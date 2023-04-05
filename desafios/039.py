from datetime import date
today = date.today()
a = int(input(f"Seu ano de nascimento: "))
idade = today.year - a
if idade == 18:
    print(f"Se aliste imediatamente!.")
elif idade < 18:
    print(f"""Ainda Vai se alistar, faltam {18-idade} anos,
seu ano de alistamento sera em {today.year + (18-idade)}""")
else:
    print(f"""Já passou {idade-18} anos do tempo de alistamento,
seu ano de alistamento foi em {today.year-(idade-18)}""")