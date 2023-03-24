n = int(input())
board = list(map(int, input().split()))
x = int(input())
cnt = 0
idx = -1
count = board.count(1)
if count >= 3:
    print("NO")
elif count == 2:
    start = board.index(1)
    if start + x >= len(board):
        print("NO")
    elif board[start + x] == 1:
        print("YES")
        print(start, start + x)
    else:
        print("NO")
elif count == 1:
    start = board.index(1)#뒤에서 1로 옮
    if start >= x:
        if board[start - x] >= 3:
            print("YES")
            print(start - x, start)
        else:
            if start + x >= len(board):
                print("NO")
            elif board[start + x] >= 1:
                print("YES")
                print(start, start + x)
            else:
                print("NO")
    elif start + x >= len(board):#1이 가는경우
        print("NO")
    elif board[start + x] >= 1:
        print("YES")
        print(start, start + x)
    else:
        print("NO")
else:
    for i in board:
        idx += 1
        if idx + x < len(board) and (board[idx + x] >= 2 and board[idx] >= 3):
            cnt += 1
            start = idx
            end = start + x
    if cnt >= 1:
        print("YES")
        print(start, end)
    else:
        print("NO")