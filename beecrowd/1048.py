a = float(input())
if a >= 0 and a <= 400:
    b=(a+(a*15/100))
    c=a*15/100
    d=15
elif a > 400.00 and a <= 800:
    b = (a+(a*12/100))
    c=a*12/100
    d = 12
elif a > 800.00 and a <= 1200:
    b = (a+(a*10/100))
    c=a*10/100
    d = 10
elif a > 1200.00 and a <= 2000:
    b =( a+(a*7/100))
    c=a*7/100
    d = 7
elif a > 2000.00:
    b = (a+(a*4/100))
    c=a*4/100
    d = 4
print(f"Novo salario: {b:.2f}")
print(f"Reajuste ganho: {c:.2f}")
print(f"Em percentual: {d} %")