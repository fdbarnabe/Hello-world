media = 0
hmaisvelho = ""
idademv = 0
somaidade=0
sexof = 0
for a in range(1, 5):
    print("-=-"*5)
    nome = (str(input(f"Qual o seu nome: ")))
    idade = (int(input(f"Qual a sua idade: ")))
    sexo = (str(input(f"Qual o seu sexo [M/F]: ")))
    somaidade += idade
    if a == 1 and sexo in "Mm":
        hmaisvelho = nome
        idademv = idade
    if sexo in "Mm" and idade > idademv:
        idademv = idade
        hmaisvelho = nome
    if sexo in "Ff" and idade < 20:
        sexof += 1 
media = somaidade/4
print(f"A idade Media é de {media} anos.")
print(f"O homem mais velho se chama {hmaisvelho} e tem {idademv} anos.")
print(f"Existe {sexof} mulheres com menos de 20 anos")