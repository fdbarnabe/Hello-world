import random

def exibe_cabecalho():
    print("-=-" * 10)
    print(" Game JOKENPÔ ")
    print("-=-" * 10)

def exibe_opcoes(options):
    print("Suas Opções:")
    for option in options:
        print(f"[ {option} ] {options[option]}")

def jogada(options):
    while True:
        a = int(input("Digite sua jogada: "))
        if a in options:
            return a
        print("Opção Inválida.")

def exibe_opcoes_escolhidas(a, pc, options):
    print(f"Você escolheu {options[a]}")
    print(f"Computador escolheu {options[pc]}")
    print("-=-" * 10)

def exibe_saida(a, pc):
    if a == pc:
        print("Empate")
    elif (a == 1 and pc == 3) or (a == 2 and pc == 1) or (a == 3 and pc == 2):
        print("Você Ganhou.")
    else:
        print("Você Perdeu.")

options = {1: "Pedra", 2: "Papel", 3: "Tesoura"}
exibe_cabecalho()
exibe_opcoes(options)
a = jogada(options)
pc = random.randint(1, 3)
exibe_opcoes_escolhidas(a, pc, options)
exibe_saida(a, pc)

