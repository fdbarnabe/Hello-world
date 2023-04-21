a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
list = [a,b,c,d,e,f]
vp = 0
media = 0
for x in list:
    if x > 0:
        vp = vp + 1
        media+=x
print(f"{vp} valores positivos")
print(f"{media/vp:.1f}")