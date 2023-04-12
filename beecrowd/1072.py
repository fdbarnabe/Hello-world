X = int(input())
inn = 0
out = 0
for a in range(1,X+1):
    N = int(input())
    if (10 <= N <=20):
        inn += 1
    else:
        out += 1
print(f"{inn} in")
print(f"{out} out")


