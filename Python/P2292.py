n = int(input())
round = 1
result = 1
i = 1

while n > round:
    result += 1
    round += 6 * i
    i += 1
print(result)
