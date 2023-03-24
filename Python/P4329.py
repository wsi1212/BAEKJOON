#unsolved
people = []
deathPeople = []
# people[cnt][] 0 == name, 1 == date, 2 == mother, 3 == father
cnt = -1
n = str
calledName = str


def findIndex(name):  # 이름 리스트에 name이 있는가?
    for i in range(len(people)):
        try:
            if people[i].index(name) == 0:
                return i
        except:
            continue
    return -1


def isFind(name):
    for i in range(len(people)):
        try:
            if people[i][0] == name:
                return True
        except:
            continue
    return False


while (n != "QUIT"):
    cnt += 1
    n = input()
    command = n.split(" ")
    information = n.split(':')

    if command[0] == "BIRTH":
        people.append(list())
        people[cnt].append(' '.join(information[0].split(" ")[1:-1]))
        people[cnt].append(information[1].strip())
        people[cnt].append(information[2].strip())
        people[cnt].append(information[3].strip())
    elif command[0] == "DEATH":
        for i in range(len(people)):
            try:
                people[i].index(' '.join(information[0].split(" ")[1:3]))  # 0
                deathPeople.append(' '.join(information[0].split(" ")[1:3]).strip())
                deathPeople.append(information[1].strip())
            except:
                continue
    elif command[0] == "ANCESTORS":
        calledName = ' '.join(command[1:3])
        calledName = calledName
        print("ANCESTORS of", calledName)
        if people[findIndex(calledName)][-2:-1] >= people[findIndex(calledName)][-1:]:
            firstParent = ' '.join(people[findIndex(calledName)][-1:])
            secondParent = ' '.join(people[findIndex(calledName)][-2:-1])
        else:
            firstParent = ' '.join(people[findIndex(calledName)][-2:-1])
            secondParent = ' '.join(people[findIndex(calledName)][-1:])

        while isFind(calledName):
            print("  ", end="")
            print(firstParent)
            if people[findIndex(firstParent)][-2:-1] >= people[findIndex(secondParent)][-1:]:
                firstParent = ' '.join(people[findIndex(calledName)][-1:])
                secondParent = ' '.join(people[findIndex(calledName)][-2:-1])
            else:
                firstParent = ' '.join(people[findIndex(calledName)][-2:-1])
                secondParent = ' '.join(people[findIndex(calledName)][-1:])

            calledName = firstParent[:]


        calledName = ' '.join(command[1:3])

        if people[findIndex(firstParent)][-2:-1] >= people[findIndex(secondParent)][-1:]:
            firstParent = ' '.join(people[findIndex(calledName)][-1:])
            secondParent = ' '.join(people[findIndex(calledName)][-2:-1])
        else:
            firstParent = ' '.join(people[findIndex(calledName)][-2:-1])
            secondParent = ' '.join(people[findIndex(calledName)][-1:])
        print(firstParent, secondParent)
        while isFind(calledName):
            print("  ", end="")
            print(secondParent)
            if people[findIndex(calledName)][-2:-1] >= people[findIndex(calledName)][-1:]:
                firstParent = people[findIndex(calledName)][-1:]
                secondParent = people[findIndex(calledName)][-2:-1]
            else:
                firstParent = people[findIndex(calledName)][-2:-1]
                secondParent = people[findIndex(calledName)][-1:]
            calledName = secondParent[:]

    elif command[0] == "DESCENDANTS":
        continue



print(people)
print(deathPeople)
