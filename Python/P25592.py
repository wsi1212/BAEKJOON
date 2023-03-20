n = int(input())
round = 0
while n >= 0:
    round += 1
    n -= round
round -= 1
if round % 2 == 1:
    print(0)
else:
    print(n*-1)
