a=input()
a=a.lower()
count=0
for i in a:
    if a.count(i)==1:
        count+=1
        print(i)
        break
if count==0:
   print('-1')