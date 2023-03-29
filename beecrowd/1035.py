a,b,c,d=list(map(int, input().split(" ")))
e = a%2
if b>c and d>a and (c+d)>(a+b) and c>0 and d>0 and e==0:
    print(f"Valores aceitos")
else:
    print(f"Valores nao aceitos")