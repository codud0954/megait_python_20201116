def sum_limit_100(num):
    sum = 0
    for i in range(1, num + 1):  # 1 ~ num
        sum += i
        if sum > 100:
            break  # 100이 넘으면 반복문에서 빠져나간다.
    return sum
#
#
# # 함수 사용하기
num = int(input("수를 입력하세요:"))
result = sum_limit_100(num)
print(result)
