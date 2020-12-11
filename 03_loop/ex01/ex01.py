# '안녕하세요'를 3번 쓰기
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")

# 문자 또는 문자열에 곱하기
print("=" * 50)

# '안녕하세요'를 3번 쓰기 while 반복문 이용하기
i = 0  # 카운팅을 하기 위한 변수
while i < 3:
    print("안녕하세요 i: %d" % i)
    i = i + 1


# 0~4 : 5번
i = 0
while i < 5:
    print("Hello World %d", i)
    # i = i + 1;
    
    # 복합 대입 연산자
    i += 1

print("=" * 50)

# 1~5: 5번
i = 1
while i <= 5:
    print("Hello World %d", i)
    i += 1

print("=" * 50)

# 5~0: 6번
i = 5;
while i >= 0:
    print("Hello World %d", i)
    # 복합 대입 연산자
    # i = i - 1
    i -= 1

print("=" * 50)


# 반복할 횟수
count = int(input("반복할 횟수를 입력하세요 : "))

i = 0
while i < count:
    print("count %d", i)
    i += 1

# 합계 구하기
sum = 0;
i = 0;
while i <= 10:
    sum = sum + i
    i += 1;

print("합은 %d입니다." % sum);

print("=" * 50)

# 0은 거짓(false), 0이 아닌 수는 참(True)
while 1:
    print("무한루프")


# 증감 연산을 안하면 값이 계속 참이어서 무한루프를 돈다.
while i < 5:
    printf("Hello World %d" % i)
