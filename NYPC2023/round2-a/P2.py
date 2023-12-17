a = int(input())
for i in range(0, a):
    n, m = map(int, input().split())

    try:
        if m == n:
            print("Yes")
        elif divmod(m,divmod(n, m)[1])[1] == 0 and n-m >= 1 and divmod(m,divmod(n, m)[1])[0] != m:
            print("Yes")
        else:
            print("No")
    except:
        if divmod(n, m)[1] == 0 and n-m >= 1:
            print("Yes")
        else:
            print("No")