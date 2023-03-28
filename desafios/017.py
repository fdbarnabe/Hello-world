import math
a = float(input())
b = float(input())
h1 = math.hypot(a,b)
formula = math.sqrt(a**2+b**2)
print(f"Hipotenusa é igual a {formula:.2f}.")
print(f"Hipotenusa é igual a {h1:.2f}")