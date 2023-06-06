n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if i==l.count(i):
        if i not in k:
            k.append(i)
if k==[]:
    print(-1)
else:
    c=sum(k)/len(k)
    print('%.2f'%c)