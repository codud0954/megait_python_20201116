# 문자열 더하기
a = "I like"
b = " Python"
c = a + b
print(c)

# 문자열 곱하기
print(b * 5)
print("=" * 50)

# 문자열의 길이 구하기
print(len(c))

# 문자열의 index
print(c[0])
print(c[len(c) - 1])  # 마지막 문자
print(c[-1]) # 마지막 문자

# 문자열 index로 값 변경하기 => 바꿀 수 없다.
# c[-1] = 'm'

# 문자열 슬라이싱 [index:index]
# I like Python    => "like"
print(c[2:6])  # like

# Python만 뽑아내기
print(c[7:])  # Python

# 특정 문자 개수 세기
print("i의 개수는", c.count("i"))

# 찾는 문자의 첫번째 index (1)
print("y의 인덱스는", c.find('y'))
print("a의 인덱스는", c.find('a')) # 없는 문자를 찾는 경우 -1

# 찾는 문자의 첫번째 index (2)
print("y의 인덱스는", c.index('y'))
#print("a의 인덱스는", c.index('a')) # 없는 문자를 찾는 경우 에러

# 문자열 치환
# I like Python => You like Python
c = c.replace("I", "You")
print(c)

# 문자열 나누기
words = c.split()   # 아무 파라미터를 넣지 않으면 기본으로 공백 기준으로 문자열을 자른다.
print(words)

fruits = "grape:apple:orange:peach"
fruit_list = fruits.split(':')
print(fruit_list)

# 문자 입력받기
# a, b = input("2개의 숫자를 입력하세요:").split()
# print(a, b)

# words = input("2개의 숫자를 입력하세요:").split()
# print(words)

a, b = [1, 2]
print(a, b)


