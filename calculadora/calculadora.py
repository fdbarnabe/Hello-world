class Calculadora():
    def soma(self, a,b):
        return a + b
    def sub(self, a,b):
        return a-b
    def mult(self, a,b):
        return a * b
    def div(self, a,b):
        if a or b == 0:
            print(f"Não é possivel realizar divisão por 0.")
            return -1
        else:
            return a/b
