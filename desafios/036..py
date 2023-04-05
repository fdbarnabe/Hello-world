a = float(input("Valor da Casa: "))
b = float(input("Valor do Salário: "))
c = float(input("Quantos anos pretende pagar: "))
if a/(c*12) > 0.3*b:
    print(f"Empréstimo negado")
else:
    print(f"Empréstimo aprovado")