from itertools import *
cnt = 0
a, b = map(int, input().split())
ice = [[False for n in range(a)] for n in range(a)]
for i in range(b):
    x, y = map(int, input().split())
    ice[x-1][y-1] = True
    ice[y-1][x-1] = True
for i in combinations(range(a), 3):
    if ice[i[0]][i[1]] or ice[i[0]][i[2]] or ice[i[1]][i[2]]:
        continue
    cnt += 1
print(cnt)