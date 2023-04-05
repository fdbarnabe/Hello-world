a = float(input())
b = float(input())
m = (a+b)/2
if m <= 5:
    print(f"Sua média é {m:.1f} - Reprovado")
elif m>5 and m < 7:
    print(f"Sua média é {m:.1f} - Recuperação")
elif m >= 7:
    print(f"Sua média é {m:.1f} - Aprovado")