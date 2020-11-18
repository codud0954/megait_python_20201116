# 입력하기
"""
noodle = input("육개장 가격을 입력하세요:") # input함수로 입력되는 값은 String(문자열)이다.
print(noodle)
print(type(noodle))  # type()  int()

# 문자 -> 숫자로 자료형(Data type) 변경: casting
noodle = int(noodle)
print(type(noodle))
print("육개장 가격은 %d입니다." % noodle)
"""
noodle = int(input("육개장 가격을 입력하세요:"))
print(noodle)
print(type(noodle))

noodle3 = noodle * 3
print("육개장 3개의 가격은 %d원 입니다." % noodle3)
