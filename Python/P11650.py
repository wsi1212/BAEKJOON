n = int(input())
a = []
for _ in range(n):
    x, y = map(int,input().split())
    a.append([x, y])
a.sort()
for i in a:
    print(*i)
