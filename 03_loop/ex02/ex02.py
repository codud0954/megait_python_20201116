# 0 ~ 4: 5개
for i in range(5):  # 0 1 2 3 4
    print("Hello, world!", i)

# 1 ~ 5: 5개
for i in range(1, 6): # 1 2 3 4 5 6
    print(i)

print("=" * 50)
# 5 ~ 1: 5개    5 4 3 2 1 0
for i in range(5, 0, -1):
    print(i)

# 1~10까지의 합
sum = 0
for i in range(1, 11): # 1 ~ 10
    sum += i    # sum = sum + i

print("합은 %d 입니다." % sum)
