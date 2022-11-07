n=int(input())
ls=list(map(int,input().split()))
max=ls[0]
f=0
for i in ls:
    if max<i:
        max=i
for i in range(2,max+1):
    c=0
    for j in ls:
        if j%i==0:
            c+=1
    if(c==n):
        f=1
        p=i
if(f==1):
       print(p)
else:
     print("1")
        