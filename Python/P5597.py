result = []
for i in range(1, 29):
    a = int(input())
    result.append(a)
for i in range(1, 31):
    if result.count(i) == 0:
        print(i)
