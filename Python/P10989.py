#계수 정렬
from sys import stdin
n = int(stdin.readline())
numbers = [0] * 10001
for i in range(0,n):
    temp = int(stdin.readline())
    numbers[temp] += 1
for i in range(0, 10001):
    for j in range(0,numbers[i]):
        print(i)