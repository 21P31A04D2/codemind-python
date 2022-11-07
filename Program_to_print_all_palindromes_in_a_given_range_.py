t1=int(input())
t2=int(input())
for i in range(t1,t2+1):
    sum=0
    temp=i
    while temp!=0:
        r=temp%10
        sum=sum*10+r
        temp=temp//10
    if i==sum:
       print(i,end=" ")
