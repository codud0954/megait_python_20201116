# 예제1
number = int(input("숫자를 입력하세요 : "))

# 10 <= number <= 40
if number >= 10 and number <= 40:
    print("%d 는 10보다 크고 40보다 작다" % number)


# 10 > number  또는  number < 40
if number < 10 or number > 40:
    print("%d 는 10보다 작거나 40보다 크다" % number)


# 예제2
weight, walk = input("몸무게와 걸은 수를 입력하세요 : ").split()
weight = int(weight)
walk = int(walk)

# 만약에 걸은 수가 10000보를 초과하면서(10001이상) 몸무게가 70키로 이하이면 '치킨이다!' 출력한다.  => 엄격한 다이어트
if walk > 10000 and weight <= 70:
    print("둘 다 만족하니 치킨이다!")

# 만약에 10000보 넘게 걸었거나 몸무게가 70키로 이하이면 '치킨이다!'를 출력한다.
if walk > 10000 or weight <= 70:
    print("하나라도 만족하니 치킨이다!")
