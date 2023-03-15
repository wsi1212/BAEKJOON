a=input()
s1=set([])
for i in range(len(a)):
    for j in range(i, len(a)):
        s1.add(a[i:j+1])
print(len(s1))