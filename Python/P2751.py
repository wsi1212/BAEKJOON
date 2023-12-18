import sys

n = int(input())
a = []
input = sys.stdin.readline
for _ in range(n):
    temp = int(input())
    a.append(temp)
a.sort()
for i in a:
    print(i)
