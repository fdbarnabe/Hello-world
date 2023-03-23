peso = float(input("Peso: "))
altura = float(input("Altura: "))
IMC = peso/(altura*altura);
if IMC <= 18.6:
    print(f"O seu IMC é {IMC} - Abaixo do Peso")
elif IMC >= 18.6 and IMC < 25.0:
    print(f"O seu IMC é {IMC} - Saudavel")
elif IMC >= 25.0 and IMC < 30.0:
    print(f"O seu IMC é {IMC} - Peso em excesso")
elif IMC >= 30.0 and IMC < 35.0:
    print(f"O seu IMC é {IMC} - Obesidade Grau I")
elif IMC >= 35.0 and IMC < 40.0:
    print(f"O seu IMC é {IMC} - Obesidade Grau II(severa)")
else:
    print(f"O seu IMC é {IMC} - Obesidade Grau III(morbida)")