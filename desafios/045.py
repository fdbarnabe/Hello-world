import random
print("-=-"*10)
print(f" Game JOKENPÔ ")
print("-=-"*10)
print(f"""Suas Opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura""")
      
print(f"-=-"*10)

a = int(input())

print(f"-=-"*10)

pc = random.randint(1, 3)
if a == 1:
    print(f"Você escolheu Pedra")
elif a == 2:
    print(f"Você escolheu Papel")
elif a == 3:
    print(f"Você escolheu Tesoura")
else:
    print(f"Opção Inválida.")

if 0 < a > 3:
    print(f"Opção Inválida.")
elif pc == 1:
    print(f"Computador escolheu Pedra")
elif pc == 2:
    print(f"Computador escolheu Papel")
elif pc == 3:
    print(f"Computador escolheu Tesoura")

print(f"-=-"*10)

if a == 1:
    if a == pc:
        print(f"Empate")
    elif pc == 3:
        print(f"Você Ganhou.")
    elif pc == 2:
        print(f"Você Perdeu.")
if a == 2:
    if a == pc:
        print(f"Empate")
    elif pc == 3:
        print(f"Você Perdeu.")
    elif pc == 1:
        print(f"Você Ganhou.")
if a == 3:
    if a == pc:
        print(f"Empate")
    elif pc == 2:
        print(f"Você Ganhou.")
    elif pc == 1:
        print(f"Você Perdeu.")