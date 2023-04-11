listapeso = []
for a in range(1, 6):
    listapeso.append(float(input(f"Qual o seu peso: ")))
b = sorted(listapeso)
print(b)
print(f"O maior peso é {b[-1]:.2f} kg e o menor é {b[0]:.2f} kg.")