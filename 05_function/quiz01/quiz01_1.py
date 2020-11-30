# n의 제곱 구하기

def squared(n):
    return n ** 2

n = int(input("수를 입력하세요: "))
print("%d의 제곱은 %d 이다." % (n, squared(n)))
