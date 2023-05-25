import sys

n = int(sys.stdin.readline().rstrip())
words = []
for i in range(0, n):
    words.append(sys.stdin.readline().rstrip())
#중복 제거 위해서 집합으로 만들고 다시 리스트로 돌리기
words = set(words)
words = list(words)
words.sort()
words.sort(key=len)
for n in words:
    print(n)