n = int(input())
for i in range(0, n):
    a, b, c = map(int, (input()).split())
    if c % a == 0:
        result = int(c / a + a * 100)
    else:
        result = int(c / a + c % a * 100 + 1)
    print(result)