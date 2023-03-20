a, b = map(int, input().split())
day = 1
weeks = int(1 + ((a - (8 - b)) + 6) / 7)
print("+---------------------+")
for i in range(1, weeks+1):
    print("|", end="")
    for weekday in range(1, 8):
        if (i == 1 and weekday < b) or (day > a):
            print("...", end="")
        else:
            print(".."+str(day) if day < 10 else "."+str(day), end="")
            day += 1
    print("|")
print("+---------------------+")
