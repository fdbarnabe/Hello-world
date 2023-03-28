a = float(input())
a100 = a//100
a = a%100
a50 = a//50
a = a%50
a20 = a//20
a = a%20
a10 = a//10
a = a%10
a5 = a//5
a = a%5
a2 = a//2
a = a%2
b = a*100
c = int(b)
a1 = c//100
a = c%100
a05 = a//50
a = a%50
a025 = a//25
a = a%25
a010 = a//10
a = a%10
a005 = a//5
a = a%5
a001 = a//1
a = a%1
print(f"NOTAS:")
print(f"{int(a100)} nota(s) de R$ 100.00")
print(f"{int(a50)} nota(s) de R$ 50.00")
print(f"{int(a20)} nota(s) de R$ 20.00")
print(f"{int(a10)} nota(s) de R$ 10.00")
print(f"{int(a5)} nota(s) de R$ 5.00")
print(f"{int(a2)} nota(s) de R$ 2.00")
print(f"MOEDAS:")
print(f"{int(a1)} moeda(s) de R$ 1.00")
print(f"{int(a05)} moeda(s) de R$ 0.50")
print(f"{int(a025)} moeda(s) de R$ 0.25")
print(f"{int(a010)} moeda(s) de R$ 0.10")
print(f"{int(a005)} moeda(s) de R$ 0.05")
print(f"{int(a001)} moeda(s) de R$ 0.01")
