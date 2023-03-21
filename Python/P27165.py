n = int(input())
board = list(map(int, input().split()))
x = int(input())

if board.count(1) >= 3 or board.count(1) == 0:
    print("NO")
elif board.count(1) == 1:
    start = board.index(1)
    if start + x >= len(board):
        print("NO")
    elif board[start + x] >= 2:
        print("YES")
        print(start, start + x)
    else:
        print("NO")
elif board.count(1) == 2:
    start = board.index(1)
    if start + x >= len(board):
        print("NO")
    elif board[start + x] == 1:
        print("YES")
        print(start, start + x)
    else:
        print("NO")
