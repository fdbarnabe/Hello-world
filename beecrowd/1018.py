notas = int(input())
print(notas)
notas100 = notas//100
notas = notas%100
notas050 = notas//50
notas = notas%50
notas020 = notas//20
notas = notas%20
notas010 = notas//10
notas = notas%10
notas005 = notas//5
notas = notas%5
notas002 = notas//2
notas = notas%2
notas001 = notas//1
notas = notas%1
print(f"{notas100} nota(s) de R$ 100,00")
print(f"{notas050} nota(s) de R$ 50,00")
print(f"{notas020} nota(s) de R$ 20,00")
print(f"{notas010} nota(s) de R$ 10,00")
print(f"{notas005} nota(s) de R$ 5,00")
print(f"{notas002} nota(s) de R$ 2,00")
print(f"{notas001} nota(s) de R$ 1,00")