def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
a=int(input())
b=int(input())
i=a
d=0
while i<=b:
    if prime(i):
        d+=1
    i+=1
print(d)