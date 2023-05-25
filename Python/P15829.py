l = int(input())
n = input()
result = 0
for i in range(0, len(n)):
    result += (31 ** i * (ord(n[i]) - ord('a') + 1)) % 1234567891
    result %= 1234567891
print(result)
