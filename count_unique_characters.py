a=input()
a=a.lower()
count=0
for i in a:
    if a.count(i)==1 and i not in' ':
        count+=1
print(count)