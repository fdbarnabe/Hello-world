a = float(input(f"Valor do produto: "))
desconto = 5/100
print(f"O valor do produto é de R$ {a:.2f}, o valor de 5% de desconto é de R$ {(a*desconto):.2f}, valor final é de R$ {(a - (a*desconto)):.2f}.")