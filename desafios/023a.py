b = int(input())
if b >= 1000 :
    a = str(b)
    print(f"Unidade: {a[3]}")
    print(f"Dezena: {a[2]}")
    print(f"Centena: {a[1]}")
    print(f"Milhar: {a[0]}")
elif b >= 100 and b < 1000:
    a = str(b)
    print(f"Unidade: {a[2]}")
    print(f"Dezena: {a[1]}")
    print(f"Centena: {a[0]}")
    print(f"Milhar: {0}")
elif b >= 10 and b < 100:
    a = str(b)
    print(f"Unidade: {a[1]}")
    print(f"Dezena: {a[0]}")
    print(f"Centena: {0}")
    print(f"Milhar: {0}")
else:
    a = str(b)
    print(f"Unidade: {a[0]}")
    print(f"Dezena: {0}")
    print(f"Centena: {0}")
    print(f"Milhar: {0}")