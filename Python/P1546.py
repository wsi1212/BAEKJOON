n = int(input())
a = list(map(float, input().split()))
max = max(a)
for i in range(0, n):
    a[i] = a[i] / max * 100
print(sum(a)/len(a))