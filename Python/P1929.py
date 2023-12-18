n, m = map(int, input().split())
map = [0] * (m + 1)
result = []
for i in range(2, m + 1):
    map[i] = i
map[0] = 0
map[1] = 0
for i in range(2, m + 1):
    if map[i] == 0:
        continue
    if i >= n:
        result.append(i)
    for j in range(i, m + 1, i):
        map[j] = 0
for i in result:
    print(i)