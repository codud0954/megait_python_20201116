# 1에서 입력한 수까지의 짝수 합 구하기

# 1. while문
num = int(input("수를 입력하세요: "))

# sum = 0
# i = 1
# while (i <= num):
#     if i % 2 == 0:
#         sum += i
#     i += 1
#
# print("더한 결과는 %d입니다." % sum)

# 2. for문
sum = 0
for i in range(1, num + 1):
    if i % 2 == 0:
        sum += i

print("더한 결과는 %d입니다." % sum)
