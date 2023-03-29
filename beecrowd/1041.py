X,Y=map(float, input().split(" "))
if X==0 and Y==0:
    print("Origem")
elif X > 0 and Y > 0:
    print(f"Q1")
elif X > 0 and Y < 0:
    print(f"Q4")
elif X < 0 and Y < 0:
    print(f"Q3")
elif X < 0 and Y > 0:
    print(f"Q2")
elif X==0 and Y==0:
    print("Origem")
elif Y==0 :
    print("Eixo X")
elif X==0 :
    print("Eixo Y")