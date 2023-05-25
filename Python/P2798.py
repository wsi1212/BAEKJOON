import sys
from itertools import *

n, m = map(int, sys.stdin.readline().rstrip().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))
dateSet = list(permutations(data, 3))
result = 0

for i in dateSet:
    if result <= sum(i) <= m:
        result = sum(i)

print(result)
