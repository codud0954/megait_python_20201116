# 1. 실수 연산
number1 = 33
number2 = 35.325
print('두 수의 곱은 %g 입니다.' % (number1 * number2))

# 2. 943 시간 -> 몇일 몇시간
hours = 943
day = hours / 24   # 몫
hour = hours % 24  # 나머지
print("%d시간은 %d일 %d시간 입니다." % (hours, day, hour))

# 3. 도형 넓이 구하기: 가로 길이 8 세로 길이 9인 삼각형, 사각형
width = 8
height = 9
rectangle = width * height     # 사각형
triangle = rectangle / 2  # 삼각형
print("사각형의 넓이:", rectangle)
print("삼각형의 넓이:", int(triangle))   # int() => 정수로 변환

# 4. 평균구하기. 국어:93 수학:88 영어:94
korean = 93
math = 88
english = 94
average = (korean + math + english) / 3
print("국어:%d, 수학:%d, 영어:%d" % (korean, math, english))
print("평균 %.2f점 입니다." % average)

# 5. 화씨 변환 :  30도 => 화씨
# 화씨 온도 = 9 / 5 * 섭씨온도 + 32
c = 30
f = 9 / 5 * c + 32
print("섭씨 %d도는 화씨 %g도 입니다." % (c, f))
