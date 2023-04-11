import random
print(("-=-")*20)
a = int(input("Tente adivinhar o número que estou pensando: "))
print(("-=-")*20)
b = random.randint(0, 5)
while a!=b:
    a = int(input(f"Você errou, eu pensei no numero {b}, escolha novamente: "))
else:
    print(f"Você errou, eu pensei no numero {b}")