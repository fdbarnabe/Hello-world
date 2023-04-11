sexo = str(input(f"Qual o seu sexo[M/F]: ")).strip().upper()[0]
while sexo not in "FM":
    sexo=str(input(f"Dados inválidos, Qual o seu sexo [M/F]: ")).strip().upper()[0]
print(f"Sexo {sexo} registrado.")