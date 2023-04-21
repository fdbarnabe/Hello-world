a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
list = [a,b,c,d,e]
vp = 0
for x in list:
    if x%2== 0:
        vp = vp + 1
print(f"{vp} valores pares")