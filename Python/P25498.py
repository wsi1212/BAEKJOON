# unsolved
n = int(input())
edges = []
tree = list(map(str, input()))
queue = []
result = []
visited = [False, ]
validNodes = []
tmp = []
maxStr = ""
for i in range(1, n):
    edges.append(list(map(int, input().split(" "))))
    visited.append(False)
queue.append(tree[0])
result.append((queue[0]))
print(edges)
print(queue)
queue.append(1)
visited[1] = True
while queue:
    validNodes.clear()
    tmp.clear()
    for i in range(len(queue)):
        print(i)
        for next in edges[i]:
            if visited[next - 1]:
                continue
            nextStr = str(tree[next - 1])
            print("nextStr", nextStr)
            if maxStr > nextStr:
                continue
            if not validNodes or maxStr < tree[next - 1]:
                maxStr = tree[next - 1]
            validNodes.append(next - 1)
            print("Max, next, valid", maxStr, next, validNodes)
    if not validNodes:
        break
    result.append(maxStr)
    for next in validNodes:
        visited[next] = True
        tmp.append(next)
    queue = tmp

print("result", result)
