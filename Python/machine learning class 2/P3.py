'''3. 과일 이름을 입력받은 후 “사과” 또는 “감”이 입력되면 "Very Good~~"를 출력, ”귤”이나 “복숭아”이  입력되면 "Good~~" 출력, 다른 값이 입력되면 "사과나 감, 귤, 복숭아 중 하나를 입력하세요~~"라는 메시지를 출력하시오.

<실행결과>

사과, 감, 귤, 복숭아 중에 어떤 과일을 좋아하세요?: 복숭아
Good~



'''

a=input("사과, 감, 귤, 복숭아 중에 어떤 과일을 좋아하세요?: ")
if(a=='귤' or a=="복숭아"):
    print("Good~~")
elif(a=='감' or a=="사과"):
    print("Very Good~~")
else:
    print("사과, 감, 귤, 복숭아 중 하나를 입력하세요~~")