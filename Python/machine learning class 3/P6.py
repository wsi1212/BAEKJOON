a=int(input())
b=int(input())
temp=int(0)
if(b<a):
    temp=a
    a=b
    b=temp
for i in range(a,b+1):
    if i%10!=3:
        print(i)