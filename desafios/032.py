import calendar

a = int(input())
if calendar.isleap(a):
    print(f"{a} é ano bissexto")
else:
    print(f"{a} não é ano bissexto")
