def swap(i, j):
    temp = points[i][0]
    points[i][0] = points[j][0]
    points[j][0] = temp
    temp = points[i]
    points[i] = points[j]
    points[j] = temp

def maxIndexOfPoints(i):
    temp = []
    for j in range(i, len(points) - i):
        element = points[j]
        temp.append(element[1])
    maxY = max(temp)
    for j in range(0, len(points)):
        if points[j][1] == maxY:
            xOfMaxY = points[j][0]
    maxPoint = []
    maxPoint.append(xOfMaxY)
    maxPoint.append(maxY)
    return points.index(maxPoint)

def minIndexOfPoint(i):
    temp = []
    for j in range(i, len(points) - i):
        element = points[j]
        temp.append(element[1])
    maxY = min(temp)
    for j in range(0, len(points)):
        if points[j][1] == maxY:
            xOfMaxY = points[j][0]
    maxPoint = []
    maxPoint.append(xOfMaxY)
    maxPoint.append(maxY)
    return points.index(maxPoint)

n = int(input())
points = []
for i in range(0, n):
    points.append(list(map(int, input().split())))
result = 0
points.sort()
for i in range(0, len(points) // 2):
    if not maxIndexOfPoints(i) == len(points) - i - 1:
        swap(maxIndexOfPoints(i), len(points) - i - 1)
        result += 1
    if not minIndexOfPoint(i) == i:
        swap(minIndexOfPoint(i),i)
        result += 1
print(result)
