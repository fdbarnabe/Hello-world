a = float(input())
if a <=2000.00:
    print(f"Isento")
elif a > 2000.00 and a<=3000.00:
    b = (a-2000)*0.08
    print(f"R$ {b:.2f}")
elif a > 3000.00 and a <=4500.00:
    b = (1000*0.08)+((a-3000)*0.18)
    print(f"R$ {b:.2f}")
elif a > 4500.00:
    b= (1000*0.08)+(1500*.18)+((a-4500)*0.28)
    print(f"R$ {b:.2f}")
