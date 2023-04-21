a,b=list(map(int, input().split()))
if a>=b:
    dur = 24-a+b
else:
    dur = b-a
print(f"O JOGO DUROU {dur} HORA(S)")
