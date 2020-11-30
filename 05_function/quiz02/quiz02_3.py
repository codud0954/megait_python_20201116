# 3. 소수 판별
# 함수 설계하기
def is_prime_number(num):
    # 구현
    # 2 : 소수
    # 5 / 2 3 4  => 모두 나누어지지 않으면 소수
    if num == 2:
        return "소수이다."

    for i in range(2, num): # 2, num - 1
        if num % i == 0:
            return "소수가 아니다."

    return "소수이다."

num = int(input("수를 입력하세요:"))
is_prime = is_prime_number(num)
print(is_prime)
