a,b,c,d=list(map(int,input().split()))
horafinal = c - a
minfinal = d - b
if horafinal<0:
    horafinal = horafinal+24
if minfinal<0 :
    minfinal = minfinal+60
    horafinal = horafinal - 1
if horafinal==0 and minfinal == 0:
    print(f"O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print(f"O JOGO DUROU {horafinal} HORA(S) E {minfinal} MINUTO(S)")
