file = open("arquivos/teste.txt", "w")
nome = input("Digite seu nome: ")
file.write(f"O meu nome é {nome}\n")
file.close()