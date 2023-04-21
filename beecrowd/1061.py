a,b=list(map(str,input().split()))
c=int(b)
h1,m1,s1=list(map(int,input().split(":")))
d,e=list(map(str,input().split()))
f=int(e)
h2,m2,s2=list(map(int,input().split(":")))
diainicial=c*86400+h1*3600+m1*60+s1
diafinal=f*86400+h2*3600+m2*60+s2
dia=diafinal-diainicial
dias=dia//86400
i=dia%86400
hora=i//3600
i=i%3600
min=i//60
i=i%60
s=i
print(f"{dias} dia(s)")
print(f"{hora} hora(s)")
print(f"{min} minuto(s)")
print(f"{s} segundo(s)")
