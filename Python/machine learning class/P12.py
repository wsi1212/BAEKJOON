print("현재 이 과목의 수강 신청자는 ['홍길동', '일지매']입니다")
c=['홍길동', '일지매']
a=input("목록에 추가할 첫번째 학생의 이름을 입력하세요:")
print(a,"학생의 신청이 완료되었습니다.\n")
c.append(a)
b=input("목록에 추가할 두번째 학생의 이름을 입력하세요:")
print(b,"학생의 신청이 완료되었습니다.\n")
c.append(b)
print("현재 이 과목의 최종 수강 신청자는",c,"입니다")