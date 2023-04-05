a,b,c = list(map(int, input().split()))

if a > b and b > c:
    print(f"""{c}
{b}
{a}
    
{a}
{b}
{c}""")
elif a > c and c > b:
    print(f"""{b}
{c}
{a}
    
{a}
{b}
{c}""")
elif b > a and a > c:
    print(f"""{c}
{a}
{b}
    
{a}
{b}
{c}""") 
elif b > c and c > a:
    print(f"""{a}
{c}
{b}
    
{a}
{b}
{c}""")
elif c > a and a > b:
    print(f"""{a}
{a}
{c}
    
{a}
{b}
{c}""")
elif c > b and b > a:
    print(f"""{a}
{b}
{c}
    
{a}
{b}
{c}""")