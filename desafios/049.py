a = int(input(f"Digite um numero para saber a tabuada dele: "))
soma = 0
for b in range(1, 11):
    soma = soma + 1
    print(f"{a:2}*{soma:2} = {a*soma:2}")
