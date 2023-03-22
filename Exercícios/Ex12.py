peso = float(input("Peso: "))
altura = float(input("Altura: "))
IMC = peso/(altura*altura);
if IMC <= 18.5:
    print(f"O seu IMC é {IMC} - Abaixo do Peso")
elif IMC > 18.5 and IMC <= 24.9:
    print(f"O seu IMC é {IMC} - Saudavel")
elif IMC > 24.9 and IMC <= 29.9:
    print(f"O seu IMC é {IMC} - Peso em excesso")
elif IMC > 29.9 and IMC <= 34.9:
    print(f"O seu IMC é {IMC} - Obesidade Grau I")
elif IMC > 34.9 and IMC <= 39.9:
    print(f"O seu IMC é {IMC} - Obesidade Grau II(severa)")
else:
    print(f"O seu IMC é {IMC} - Obesidade Grau III(morbida)")