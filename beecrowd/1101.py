while (True):
    a,b=list(map(int,input().split()))
    x = min(a,b)
    y = max(a,b)
    soma = 0
    if x > 0:
        for i in range(x,y+1):
            print(f"{i}", end=" ")
            soma += i
            if i == y:
                print(f"Sum={soma}")
    else: 
        break