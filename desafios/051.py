a = int(input(f"Digite o primeiro term da PA: "))
b = int(input(f"Digite a razão usada na PA: "))
decimo = a + (10-1)*b
for x in range(a, decimo+b, b):
    print(x, end=" ")