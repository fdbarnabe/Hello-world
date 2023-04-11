soma = 0
count = 0
for c in range(1, 501):
    if c%3==0 and c%2!=0:
        soma = soma + c
        count = count + 1
print(f"A soma de {count} valores impares multiplos por 3 é {soma}.")
