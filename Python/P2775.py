def count_residents(k, n):
    apt = [[0] * n for _ in range(k)]
    for i in range(n):
        apt[0][i] = i + 1
    for i in range(1, k):
        temp = 0
        for j in range(n):
            temp += apt[i - 1][j]
            apt[i][j] = temp
    sum = 0
    for i in apt[k - 1]:
        sum += i
    return sum


t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    result = count_residents(k, n)
    print(result)
