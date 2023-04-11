soma = 0
cont = 0
for a in range(1,7):
    num=int(input(f"Digite o {a} Valor: "))
    if num%2==0:
        soma += num
        cont += 1 
print(f"Voce informou {cont} números pares, e a suas soma é {soma}")