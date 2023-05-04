a = str(input(f"Qual o seu nome: ").strip())

nomesbanidos = ["igor", "fernando", "paulo"]
amin = a.lower().split()
a0 = amin[0]
am = a.capitalize()
if a0 not in nomesbanidos:
    b = int(input(f"Qual a sua idade: "))
    if b >= 18 and b<=30:
        print(f"Você não esta apto para continuar o cadastro")
    else:
        c = str(input(f"Qual o seu endereço: ").strip())
        cmin = c.lower().split()
        c0 = cmin[0]
        cm = c.capitalize()
        while c0 != str("rua"):
            c= str(input(f"Endereço invalido, digite novamente: "))
        print(f"Cadastro Realizado, nome: {am}, idade: {b}anos, endereço: {cm}")
else:
    print(f"Você não pode continuar com o cadastro")