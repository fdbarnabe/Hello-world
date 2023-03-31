import random
print(("-=-")*20)
a = int(input("Tente adivinhar o número que estou pensando: "))
print(("-=-")*20)
b = random.randint(0, 5)
if a == b:
    print(f"Você acertou, eu pensei no numero {b}")
else:
    print(f"Você errou, eu pensei no numero {b}")