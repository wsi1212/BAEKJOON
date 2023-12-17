def printGap(gap):
    print('-' * gap, end="")


def printWords(str, printType, gap):
    if printType == 0:
        print(str, end="")
        printGap(gap)
    elif printType == 1:
        if gap % 2 == 0:
            printGap(gap // 2)
            print(str, end="")
            printGap(gap // 2)
        else:
            printGap(gap // 2)
            print(str, end="")
            printGap(gap // 2 + 1)
    elif printType == 2:
        printGap(gap)
        print(str, end="")
    print()


def printf(str, printType):
    words = str.split()
    temp = []
    i = 0
    space = m
    try:
        while space >= len(words[i]) + (1 if len(temp) > 0 else 0):
            if i == len(words) - 1:  # 마지막 index 경우
                printWords(words[i], printType, m - len(words[i]))
            else:  # 한 줄에 여러 단어가 들어가는 경우
                while space >= len(words[i]):
                    temp.append(words[i])
                    space -= len(words[i])
                    try:
                        if space >= len(words[i + 1]) + 1:  # 다음 단어가 올 수 있는 경우
                            space -= 1
                        else:
                            break
                    except Exception as error:

                        break
                    i += 1
                tempStr = '-'.join(temp)
                printWords(tempStr, printType, space)
                space = m
                temp.clear()
            # print("reset", i, space, temp)
            i += 1
    except:
        space = m

n, m = map(int, input().split(' '))
writing = []
printType = 0
for i in range(0, n):
    temp = input()
    writing.append(temp)

# print(writing)
for i in writing:
    if i == "<CENTER>":
        printType = 1
    elif i == "<RIGHT>":
        printType = 2
    elif i == "<LEFT>" or i == "</CENTER>" or i == "</RIGHT>" or i == "</LEFT>":
        printType = 0
    else:
        printf(i, printType)
