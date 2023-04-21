high=0
pos=0
for a in range(1,101):
    N = int(input())
    if N > high:
        high=N
        pos=a
print(f"{high}")
print(f"{pos}")