import math
a,b,c=map(float, input().split(" "))
delta = (b**2)-(4*a*c)
if delta < 0 or a==0:
    print(f"Impossivel calcular")
else:
    D=math.sqrt(delta)
    R1 = (-b+D)/(2*a)
    R2 = (-b-D)/(2*a)
    print(f"R1 = {R1:.5f}\nR2 = {R2:.5f}")