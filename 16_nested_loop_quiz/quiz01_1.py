num = int(input("수를 입력 하세요:"))
cnt = 0
while(num != 0):
    num //= 10
    cnt += 1

print(cnt)
