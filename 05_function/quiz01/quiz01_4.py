# 홀수, 짝수 여부
def odd_even(n):
    if n % 2 == 0:
        return "짝수"
    else:
        return "홀수"

n = int(input("숫자를 입력하세요: "))
print(odd_even(n))
