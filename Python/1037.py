#잔짜 약수로 수 구하기
#진짜 약수중 가장 작은 거와 가장 큰 약수 구해서 곱하기
#12 -> 2, 3, 4, 6
#12 = 2*6
n = int(input())
a = list(map(int, input().split(" ")))

print(min(a)*max(a))