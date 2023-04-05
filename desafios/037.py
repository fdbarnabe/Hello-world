a = int(input())
print(f"""Escolha uma das bases para conversão:
[ 1 ] converter para binário,
[ 2 ] converter para octal,
[ 3 ] converter para hexadecimal.""")
b = int(input())
if b == 1:
    print(f"A conversão do numero {a} para binário é {bin(a)[2:]}.")
elif b == 2:
    print(f"A conversão do numero {a} para binário é {oct(a)[2:]}.")
elif b == 3:
    print(f"A conversão do numero {a} para binário é {hex(a)[2:]}.")
else:
    print(f"Opção inválida.")