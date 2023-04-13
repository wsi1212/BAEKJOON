import sys
input = sys.stdin.readline
print = sys.stdout.write

n = input().rstrip()
for i in range(int(n)):
    a, b = map(int,input().split(" "))
    print(str(a+b))
    print("\n")


