# 몫과 나머지 출력

def division(n, divide):
    q = n // divide
    r = n % divide
    print("몫: %d 나머지: %d" % (q, r))

n, d = input("숫자와 나눌 수를 입력하세요: ").split()
n = int(n)
d = int(d)

division(n, d)
