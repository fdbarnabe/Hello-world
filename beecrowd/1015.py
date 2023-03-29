import math
a1 = input().split(" ")
a2 = input().split(" ")
x1, y1 = a1
x2, y2 = a2
F = math.sqrt((float(x2) -float(x1))**2 + (float(y2)-float(y1))**2)
print(f"{F:.4f}")