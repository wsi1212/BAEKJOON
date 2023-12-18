import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
queue = deque()
for _ in range(n):
    command = input().rstrip()
    if command.split()[0] == "push_front":
        queue.appendleft(int(command.split()[1]))
    elif command.split()[0] == "push_back":
        queue.append(int(command.split()[1]))
    elif command == "pop_front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            del queue[0]
    elif command == "pop_back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
            del queue[-1]
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
