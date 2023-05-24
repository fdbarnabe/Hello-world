class Papainoel():
    def __init__(self, Ho):
        self.ho = Ho

    def print(self):
        print(f"{self.ho}", end=" ")

ho1=Papainoel("Ho")
x = int(input())

for a in range(1,x):
    ho1.print()
    if a == x-1:
        print(f"Ho!")    