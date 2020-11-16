# format: 문자열 속에 다른 타입의 변수값을 넣을 때 사용

noodle_cup = 850;

# 정수(Integer)
print("육개장 하나의 가격은 %d입니다." % noodle_cup)

# 여러개의 변수 출력
print("육개장 하나의 가격은 %d이고 3개의 가격은 %d입니다." % (noodle_cup, noodle_cup * 3)) # 두 개 이상일 때는 치환할 변수들을 ()로 묶는다


# 소수(Float)
pi = 3.14
print("원주율 pi는 %f입니다." % pi)

# 문자(Character)
grade = 'A'
print("등급은 %c 입니다." % grade)

# 문자열(String)
name = '신보람'
print("이름은 %s 입니다." % name)


real_pi = 3.1415926535897;
# 소수점 표시
print("파이: %f" % real_pi)
print("소수점 둘째자리 파이: %.2f" % real_pi)
print("소수점 여덟째자리 파이: %.8f" % real_pi)
print("원주율 pi는 %g입니다." % real_pi)    # 소수점 아래 숫자가 없는 곳까지 깔끔하게 출력된다.

# 퍼센트(%) 문자 쓰기
print("%d%%" % 95)  # 95%
