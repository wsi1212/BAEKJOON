# 25점 짜리 코드
"""a = list(map(str,input()))
for i in range(int(a.count('0')/2)):
    print(0,end="")
for i in range(int(a.count('1')/2)):
    print(1,end="")"""
# 100점 짜리 코드
a = list(map(int, input()))
zeroCnt = int(a.count(0) / 2)
oneCnt = int(a.count(1) / 2)
j = 0
for i in range(len(a)-1, 0, -1):
    if j >= zeroCnt:
        break
    if a[i] == 0:
        a[i] = 2
        j += 1
j = 0
for i in range(0, len(a)):
    if j >= oneCnt:
        break
    if a[i] == 1:
        a[i] = 2
        j += 1
for i in range(0, len(a)):
    if a[i] != 2:
        print(a[i], end="")
