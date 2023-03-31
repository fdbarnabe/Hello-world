a = str(input()).upper().strip()
print(f" A letra A aparece {a.count('A')}")
print(f" A letra A aparece na posição {a.find('A')+1}")
print(f" A letra A aparece na posição {a.rfind('A')+1}")