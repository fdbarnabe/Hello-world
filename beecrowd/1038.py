a,b=list(map(int, input().split(" ")))
if a==1:
    print(f"Total: R$ {4*b:.2f}")
elif a==2:
    print(f"Total: R$ {4.5*b:.2f}")
elif a==3:
    print(f"Total: R$ {5*b:.2f}")
elif a==4:
    print(f"Total: R$ {2*b:.2f}")
elif a==5:
    print(f"Total: R$ {1.5*b:.2f}")