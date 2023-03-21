x, n = list(map(int, input().split()))
if n % 2 == 1 and n != 1:
    print("ERROR")
elif (n == 0 and x > 0) or (n == 1 and x < 0):
    print("INFINITE")
elif (n == 1 and x >= 0) or x <= 0:
    print(0)
else:
    n = n // 2
    print((x + n - 1) // n - 1)