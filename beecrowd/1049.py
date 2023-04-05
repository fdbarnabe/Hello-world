a=input()
b=input()
c=input()
if a == 'vertebrado':
    if b == 'ave':
        if c == 'carnivoro':
            print(f"aguia")
        elif c == 'onivero':
            print(f"pomba")
    elif b == 'mamifero':
        if c == 'onivoro':
            print(f"homem")
        elif c =='herbivoro':
            print(f"vaca")
elif a == 'invertebrado':
    if b == 'inseto':
        if c == 'hematofago':
            print(f"pulga")
        elif c == 'herbivoro':
            print(f"lagarta")
    elif b == 'anelideo':
        if c == 'hematofago':
            print(f"sanguessuga")
        elif c == 'onivoro':
            print(f"minhoca")