class Pessoa():
    def __init__(self, nome , idade):
        self.nome = nome
        self.idade = idade
    
    def exibe(self):
        print(f"Nome: {self.nome}, idade: {self.idade} anos.")

p1 = Pessoa("igor" , "29")
p1.exibe()