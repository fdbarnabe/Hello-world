import random
print(("-=-")*20)
a = int(input("Tente adivinhar o número que estou pensando entre 1 a 10: "))
b = random.randint(1, 11)
palpites = 1
while a!=b:
        a = int(input(f"Você errou, escolha novamente: "))
        palpites += 1
print(f"Você ganhou após {palpites} tentativas, eu pensei no numero {b}")