n, k = map(int, input().split())
people = []
result = 0
isChecked = [False] * n
for i in range(1, n+1):
    a = int(input())
    people.append(a)
point = people[0]
while not isChecked[k]:
    if(result >= len(people)):
        print(-1)
        exit(0)
    result += 1
    isChecked[point] = True
    point = people[point]
print(result)

