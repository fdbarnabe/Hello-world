N = int(input())
for a in range(1,N+1):
    X = int(input())
    if X > 0 and X%2==0:
        print(f"EVEN POSITIVE")
    elif X > 0 and X%2!=0:
        print(f"ODD POSITIVE")
    elif X < 0 and X%2==0:
        print(f"EVEN NEGATIVE")
    elif X < 0 and X%2!=0:
        print(f"ODD NEGATIVE")
    elif X == 0:
        print(f"NULL")