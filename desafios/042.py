a,b,c=map(float, input().split())
color = {'amareloverm':'\033[1;33m','violetverm':'\033[1;35m', 'limpa':'\033m'}
if (a+b)>c and (b+c)>a and (c+a)>b:
    if a == b and b == c and a == c:
        print(f"{color['violetverm']}É um triângulo Equilátero.{color['limpa']}")
    elif a == b or b == c or a == c:
        print(f"{color['violetverm']}É um triângulo Isósceles.{color['limpa']}")
    elif a!=b and b!=c and a!=c:
        print(f"{color['violetverm']}É um triângulo Escaleno.{color['limpa']}")
else:
    print(f"\033[4;31;42m Não é um triângulo.\033")