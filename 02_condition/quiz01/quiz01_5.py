# 하샤드 수
num = int(input("수를 입력하세요: "))

q = num // 10  # 10의 자리
r = num % 10   # 1의 자리

if num % (q + r) == 0:
    print("%d는 하샤드 수 입니다." % num)
if num % (q + r) != 0:
    print("%d는 하샤드 수가 아닙니다." % num)
