linha1 = input().split(" ")
linha2 = input().split(" ")
cod1, qtde1, preço1=linha1
cod2, qtde2, preço2=linha2
total = (int(qtde1))*(float(preço1))+(int(qtde2)*float(preço2))
print(f"VALOR A PAGAR: R$ {(total):.2f}")