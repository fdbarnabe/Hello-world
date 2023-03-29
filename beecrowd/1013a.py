lista = input().split(" ")
a,b,c=lista
ab = ((int(a)+int(b)+abs(int(a)-int(b)))/2)
abc = ((int(ab)+int(c)+abs(int(ab)-int(c)))/2)
print(f"{int(abc)} eh o maior")