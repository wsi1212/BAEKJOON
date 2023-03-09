seet=['VIP','S','A','B']
money=['150000','110000','90000','70000']
a=input("어디 앉을거임? ")
for i in seet:
    if(str(i)==a):
        print(money[seet.index(i)])
        exit()
print("너는 걍 보지마셈")