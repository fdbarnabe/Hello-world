
# Criar uma classe chamada Carro com os atributos: nome, modelo, cor e ano
# E criar um método chamado buzina que imprime na tela "Buzinaa!"

class Carro():
    def __init__(self, nome, modelo, cor, ano):
        self.nome = nome
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def print(self):
        print(f"O carro é {self.nome}, modelo {self.modelo} da cor {self.cor} e do ano {self.ano}.")

    def buzina(self):
        print(f"Buzinaa!")

carro1 = Carro( "FIPE" , "KWID" , "PRATA", "2019")
carro1.print()
carro1.buzina()


