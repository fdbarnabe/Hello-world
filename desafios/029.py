a = int(input())
if a > 80:
    print(f"Você foi multado e precisa pagar uma multa de R$ {(a-80)*7:.2f}")
else:
    print(f"Você não foi multado")