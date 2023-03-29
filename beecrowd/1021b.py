b = float(input())
a = b+0.0001
notas = [100, 50, 20, 10, 5, 2]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
print(f"NOTAS:")
for nota in notas:
    print(f"{int(a//nota)} nota(s) de R$ {nota}.00")
    a = a%nota
print(f"MOEDAS:")
for moeda in moedas:
    print(f"{int(a//moeda)} moeda(s) de R$ {moeda:.2f}")
    a = a%moeda