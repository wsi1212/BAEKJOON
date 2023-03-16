def reverse(number):
  rever = str(number)[::-1]
  if number < 0:
    rever = "-" + rever[:-1]
  return int(rever)

a,b=map(int,input().split())

a=reverse(a)
b=reverse(b)
if(a>b):
  print(a)
else:
  print(b)
