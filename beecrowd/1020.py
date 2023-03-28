a = int(input())
anos = a//(365)
a = a%(365)
meses = a//30
a = a%30
dias = a
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")