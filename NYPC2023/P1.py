n = int(input())
heroS = []
for i in range(n):
    heroS.append(input())

t = int(input())
wantEd = []
for i in range(t):
    wantEd.append(input())

for i in wantEd:
    if i in heroS:
        heroS.remove(i)

print(len(heroS))
for i in heroS:
    print(i)
