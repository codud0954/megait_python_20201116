# 5개의 수를 입력받아 최소값 구하기

i = 1
min = 0    # 입력받은 수가 0보다 커서 최저값이 0으로 찍히는 경우가 생길 수 있다.
while i <= 5:
    num = int(input("%d번째 수를 입력하세요: " % i))
    if i == 0:
        min = num

    if min > num:
        min = num

    i += 1

print("최소값은 %d입니다." % min)
