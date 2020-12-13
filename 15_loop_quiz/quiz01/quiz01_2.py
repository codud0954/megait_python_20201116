max = int(input("수를 입력하세요: "))
for i in range(4):  # 바깥에서 한 번 입력 받으므로 4번 돌림
    num = int(input("수를 입력하세요: "))
    if max < num:
        max = num

print("가장 큰 수는 %d입니다." % max)
