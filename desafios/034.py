a = float(input())
if a >1250.00:
    print(f"O seu salário de R$ {a:.2f} tera um aumento de 10% para R$ {((a*0.1)+a):.2f}")
else:
    print(f"O seu salário de R$ {a:.2f} tera um aumento de 15% para R$ {((a*0.15)+a):.2f}")