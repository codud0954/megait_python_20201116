num = int(input("수를 입력하세요:"))
clap_cnt = 0
for i in range(1, num + 1):
    a, b = divmod(i, 10)
    
    if a != 0 and a % 3 == 0:
        clap_cnt += 1
    if b != 0 and b % 3 == 0:
        clap_cnt += 1

print(clap_cnt)
