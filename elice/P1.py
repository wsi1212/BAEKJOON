
m, n = map(int, input().split())
starts = []
ends = []
result = -1
for i in range(0, m):
    s, e = map(int, input().split())
    starts.append(s)
    ends.append(e)
endsTemp = ends
max = sorted(endsTemp)[-n]
for i in range(min(starts), max + 1):
    cnt = 0
    for j in range(0, m):
        if ends[j] >= i >= starts[j]:
            cnt += 1
    if cnt >= n:
        result = i
        break
print(result)
