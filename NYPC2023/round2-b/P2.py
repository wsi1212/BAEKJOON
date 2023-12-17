def perform_operations(arr):
    n = len(arr)
    result = 0
    temp = []
    seen_states = set()
    while True:
        if tuple(arr) in seen_states:
            return -1
        seen_states.add(tuple(arr))
        left = []
        right = []
        pivot = arr[len(arr) - 1]
        for i in arr:
            if i > pivot:
                right.append(i)
            else:
                left.append(i)
        for i in left:
            temp.append(i)
        for i in right:
            temp.append(i)
        if arr == temp:
            break
        arr = temp
        temp = []
        result += 1
    return result

n = int(input())
arr = list(map(int, input().split()))
result = perform_operations(arr)
print(result)
