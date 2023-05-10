def soma(a,b):
    return a + b

def sub(a,b):
    return a-b

def mult(a,b):
    return a * b

def div(a,b):
    if a or b == 0:
        print(f"Não é possivel realizar divisão por 0.")
        return -1
    else:
        return a/b