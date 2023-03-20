a, b = map(int, input().split())
for i in range(0,a):
    c = input()
    d = list(c)
    d.reverse()
    print(''.join(d))
