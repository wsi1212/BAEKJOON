n, m = map(int, input().split(" "))
l = list(map(int, input().split(" ")))
max = max(l)
for i in range(max, 0, -1):
    temp = 0
    for j in l:
        if j - i > 0:
            temp += j - i;
    if(temp == m):
        print(i)
        break
