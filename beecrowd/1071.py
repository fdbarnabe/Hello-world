X = int(input())
Y = int(input())
soma = 0
if X < Y:
    for a in range(X+1, Y):
        if a%2!=0:
            soma = soma + a
    print(soma)
elif X > Y:
    for a in range(Y+1, X):
        if a%2!=0:
            soma = soma + a
    print(soma)