n = int(input())
fiboArray = [-1] * 40


def fibo(n):
    if n > 0:
        zeroCnt = 0
        oneCnt = 0
        if fiboArray[n] == -1:
            fiboArray[n] = fibo(n - 1)
            fiboArray[n] = fibo(n - 2)
        elif n == 1:
            oneCnt += 1
        elif n == 0:
            zeroCnt += 1
        print(zeroCnt, oneCnt)


for i in range(0, n):
    a = int(input())
    fibo(a)
