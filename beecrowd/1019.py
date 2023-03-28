a = int(input())
hrs = a//(60*60)
a = a%(60*60)
min = a//60
a = a%60
seg = a
print(f"{hrs}:{min}:{seg}")