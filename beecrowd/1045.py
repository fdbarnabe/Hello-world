x,y,z=list(map(float, input().split()))

if x >= y and x>=z:
    a = x
    b = y
    c = z
elif y >= x and y >= z:
    a = y
    b = x
    c = z
elif z >= x and z >= y:
    a = z
    b = x
    c = y

if a >= (b+c):
    print(f"NAO FORMA TRIANGULO")
elif a**2 == ((b**2)+(c**2)):
    print(f"TRIANGULO RETANGULO")
elif a**2 > ((b**2)+(c**2)):
    print(f"TRIANGULO OBTUSANGULO")
elif a**2 < ((b**2)+(c**2)):
    print(f"TRIANGULO ACUTANGULO")

if a == b and b == c and a==c:
    print(f"TRIANGULO EQUILATERO")
elif a == b or b==c or a==c:
    print(f"TRIANGULO ISOSCELES")


