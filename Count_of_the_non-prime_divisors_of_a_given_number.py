from math import sqrt
def isprime(n):
    if n==1:
        return 0
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
c=0
for i in range(1,n+1):
    if isprime(i)==0and n%i==0:
        c+=1
print(c)        
        