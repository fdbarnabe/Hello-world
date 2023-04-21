N = int(input())
for a in range(N):
    b,c=list(map(int,input().split()))
    soma = 0
    if b>c:
        for i in range(c+1,b):
            if i%2!=0:
                soma+=i
        print(soma)
    if b < c:
        for i in range(b+1,c):
            if i%2!=0:
                soma+=i
        print(soma)
    if b==c:
        print(0)
