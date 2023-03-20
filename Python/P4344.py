n = int(input())
for i in range(0, n):
    a = input()
    m = a.split()[0]
    value = list(map(float, a.split()[1:]))
    avr = sum(value)/len(value)
    overAvr = 0
    for j in range(0,len(value)):
        if(value[j] > avr):
            overAvr += 1
    per = float(overAvr/len(value)*100)
    print('{:.3f}%'.format(per))


