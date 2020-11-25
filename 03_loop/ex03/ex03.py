# break: break가 써진 가장 가까운 반복문을 빠져나간다.

# "안녕하세요" 5번 찍기
i = 0
while True:
    if i == 5:
        break

    print("안녕하세요", i)
    i += 1

# continue: continue가 써진 가장 가까운 반복문의 조건을 다시 본다.(아래 문장들을 수행하지 않고)

# 1~10 수 중에서 4의 배수일 때만 출력하지 않기  1 2 3 5 6 7 9 10
for i in range(1, 11): # 1 ~ 10
    if i % 4 == 0:
        pass   # 아무것도 실행하지 않는다.
    else:
        print(i, end=" ")

print()
for i in range(1, 11):
    if i % 4 == 0:
        continue

    print(i, end=" ")
