
a=int(input())
f=0
for i in range(2,a):
    if a%i==0:
        f=1
        break
if f==1:
    print('not a prime')
else:
    print('prime')