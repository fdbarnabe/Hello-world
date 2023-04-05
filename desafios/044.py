a = float(input())
print(f"""[1] A vista,
[2] Cartão
[3] 2x no Cartão,
[4] 3x ou mais no Cartão.""")
b = int(input(f"opção: "))
if b == 1:
    print(f"o valor final do produto será R$ {a-(a*0.1):.2f}")
elif b == 2 :
    print(f"o valor final do produto será R$ {a-(a*0.05):.2f}")
elif b == 3 :
    print(f"o valor final do produto será R$ {a:.2f} parcelado em R$ {a/2:.2f} por mês.")
elif b == 4:
    c = int(input(f"quantas parcelas: "))
    valor = a+(a*0.2)
    print(f"o valor final do produto será R$ {valor:.2f} parcelado em R$ {valor/c:.2f} por mês em {c} meses.")