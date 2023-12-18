import sys

input = sys.stdin.readline
n = int(input())
queue = []
for _ in range(n):
    command = input().rstrip()
    if ''.join(command[:4]) == "push":
        queue.append(int(command.split()[1]))
    elif command == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            del queue[0]
    elif command == "size":
        print(len(queue))
    elif command == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif command == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

