while (True):
    a,b=list(map(int,input().split()))
    soma = 0
    if a < b:
        for i in range(a,b+1):
            soma +=i
            print(f"{i} Sum={soma}, end=" "")
