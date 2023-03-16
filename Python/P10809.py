a=list(map(str,input()))
for i in range(0,26):
    print(a.find(chr((ord(a)+i))))
