import sys

input = sys.stdin.readline
n = int(input())
removeN = n * 15 / 100
if removeN % 1 >= 0.5:
    removeN = int(removeN) + 1
else:
    removeN = int(removeN)
points = []
for _ in range(n):
    points.append(int(input()))
points.sort()
for i in range(removeN):
    points[i] = 0
    points[-(i + 1)] = 0

if len(points) != 0:
    result = sum(points) / (len(points) - removeN * 2)
    if result % 1 >= 0.5:
        print(int(result) + 1)
    else:
        print(int(result))
else:
    print(0)
