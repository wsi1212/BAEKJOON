y = [10, 20, 30]
try:
    a, b = map(int, input().split())
    print(int(y[a]/b))
except Exception as e:
    print(e)