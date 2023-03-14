
menu=['짜장면','짱뽕','군만두','탕수육']
price=[5000,6000,8000,10000]
isorder=str
for i in range(1,4):
    print("<실행결과>")
    print("1.짜장면 - 5,000원\t2.짬뽕 - 6,000원")
    print("3.군만두 - 8,000원\t4.탕수육 - 10,000원")
    num=int(input("\n1. 위 메뉴 중 주문할 메뉴의 번호를 쓰세요: "))
    count=int(input("2. 위 메뉴의 주문 수량을 쓰세요: "))
    print("\n주문하신 메뉴는",menu[num-1]+"이고 주문 수량은",count,"그릇이며 주문금액은",price[num-1]*count,"원 입니다\n")
    print("\n3.추가 주문을 하시겠습니까? (Y / N) :")
    isorder=input()
    if(isorder=='N' or isorder=='n'):
        break