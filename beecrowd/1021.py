a = float(input())
notas100 = a//100
a = a%100
notas50 = a//50
a = a%50
notas20 = a//20
a = a%20
notas10 = a//10
a = a%10
notas5 = a//5
a = a%5
notas2 = a//2
a = a%2
b = a
moedas1 = b//1
b = b%1
moedas050 = b//0.50
b = b%0.50
moedas025 = b//0.25
b = b%0.25
moedas010 = b//0.10
b = b%0.10
moedas005 = b//0.5
b = b%0.5
moedas001 = b//0.01
print(f"NOTAS:")
print(f"{notas100} nota(s) de R$ 100.00")
print(f"{notas50} nota(s) de R$ 50.00")
print(f"{notas20} nota(s) de R$ 20.00")
print(f"{notas10} nota(s) de R$ 10.00")
print(f"{notas5} nota(s) de R$ 5.00")
print(f"{notas2} nota(s) de R$ 2.00")
print(f"MOEDAS:")
print(f"{moedas1} moeda(s) de R$ 1.00")
print(f"{moedas050} moeda(s) de R$ 0.50")
print(f"{moedas025} moeda(s) de R$ 0.25")
print(f"{moedas010} moeda(s) de R$ 0.10")
print(f"{moedas005} moeda(s) de R$ 0.05")
print(f"{moedas001} moeda(s) de R$ 0.01")
