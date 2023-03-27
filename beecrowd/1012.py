A,B,C=list(map(float,input().split(" ")))
pi = 3.14159
print(f"TRIANGULO: {(A*C)/2:.3f}")
print(f"CIRCULO: {pi*C*C:.3f}")
print(f"TRAPEZIO: {((A+B)/2)*C:.3f}")
print(f"QUADRADO: {B**2:.3f}")
print(f"RETANGULO: {(A*B):.3f}")