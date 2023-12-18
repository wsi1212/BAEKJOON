def get_divide_sum(n):
    sum = n
    while n >= 1:
        sum += n % 10
        n //= 10
    return sum


n = int(input())
for i in range(n):
    if get_divide_sum(i) == n:
        print(i)
        exit(0)
print(0)