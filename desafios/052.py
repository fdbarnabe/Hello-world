num = int(input())
divisores = 0
for a in range (1, num+1):
    if num%a==0:
        divisores += 1
if divisores == 2:
    print(f"O número {num} é um número primo.")
else:
    print(f"O número {num} não é um número primo.")