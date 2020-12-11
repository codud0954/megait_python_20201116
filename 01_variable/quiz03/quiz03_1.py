value1 = int(input("입력1: "))
value2 = int(input("입력2: "))

quotient = value1 / value2
remainder = value1 % value2

print("몫: %d 나머지 %d" % (quotient, remainder))

# 다른 방법
print(divmod(value1, value2))
print("몫: %d 나머지 %d" % divmod(value1, value2))
