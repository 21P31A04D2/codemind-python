def fun(n):
    rev=0
    while n:
        d=n%10
        rev=rev*10+d
        n=n//10
    return rev
x=int(input())
p=fun(x)
x+=p
while(True):
    t=x
    p=fun(x)
    x+=p
    if p==t:
        print(p)
        break