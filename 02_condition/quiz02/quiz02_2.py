# 공배수 구하기(2와 3의 공배수인지)
n = int(input("수를 입력하세요: "))

# # 문장으로 써볼까?
# 입력받은 숫자가 2의 배수이면서 3의 배수이면 2와 3의 공배수이다.
if n % 2 == 0 and n % 3 == 0:
    print("%d는 2와 3의 공배수 입니다." % n)
