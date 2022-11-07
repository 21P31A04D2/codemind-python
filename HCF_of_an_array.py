n=int(input())
arr=list(map(int,input().split()))
m=max(arr)
h=0
for i in range(1,m):
    c=0
    for p in range(n):
        if(arr[p]%i==0):
            c+=1
    if c==n:
        h=i
print(h)
            