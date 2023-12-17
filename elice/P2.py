m, n = map(int, input().split())
places = list(map(int, input().split()))
result = -999999999999999
for i in range(0, len(places) - n + 1):
    temp = 0
    for j in range(i, i + n):
        temp += places[j]
    if temp >= result:
        result = temp
print(result)
