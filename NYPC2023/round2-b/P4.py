n, q = map(int, input().split())
store = list(map(int, input().split()))

for i in range(0, q):
    L, R, X = map(int, input().split())
    money = [0] * len(store)
    L -= 1
    R -= 1
    X -= 1
    max = 0
    temp = 0
    money[len(money) - 1] = store[len(store) - 1] - store[X]
    for i in range(X - 1, -1, -1):
        money[i] = store[X] - store[i] + money[i + 1]
    for i in range(R, L - 1, -1):
        if money[i] >= max:
            max = money[i]
    print(max)
'''
7 6
2 5 6 5 2 1 7
1 4 7
1 3 4
2 3 3
4 6 7
1 4 6
6 7 7
'''