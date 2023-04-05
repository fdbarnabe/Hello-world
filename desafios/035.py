a,b,c=map(float, input().split())
color = {'amareloverm':'\033[1;33m','violetverm':'\033[1;35m', 'limpa':'\033m'}
if (a+b)>c and (b+c)>a and (c+a)>b:
    print(f"{color['violetverm']}É um triângulo.{color['limpa']}")
else:
    print(f"\033[4;31;42m Não é um triângulo.")