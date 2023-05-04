while (True):
    a,b=list(map(int,input().split()))
    if a > b:
        print(f"Decrescente")
    if a < b:
        print(f"Crescente")
    if a == b:
        break