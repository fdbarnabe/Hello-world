N = int(input())
for a in range(N):
    b,c,d=list(map(float,input().split()))
    total = ((b*2)+(c*3)+(d*5))/(2+3+5)
    print(f"{total:.1f}")
