a,b,c,d=map(float, input().split(" "))
media = ((a*2)+(b*3)+(c*4)+(d*1))/(2+3+4+1)
print(f"Media: {(media):.1f}")
if media >=7.0:
    print(f"Aluno aprovado.")
elif media < 5.0:
    print(f"Aluno reprovado.")
elif media >=5.0 and media < 7.0:
    print(f"Aluno em exame.")
    e = float(input())
    print(f"Nota do exame: {e:.1f}")
    media2 = (media+e)/2
    if media2 >= 5.0:
        print(f"Aluno aprovado.")
        print(f"Media final: {media2:.1f}")
    elif media2 < 5:
        print(f"Aluno reprovado.")
        print(f"Media final: {media2:.1f}")   
 