import random
a = str(input())
b = str(input())
c = str(input())
d = str(input())
lista = a, b, c, d
escolhido = random.choice(lista)
print(f"O aluno escolhido é {escolhido}.")