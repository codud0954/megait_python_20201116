n = int(input("수를 입력하세요: "))

# while
i = 0
sum = 0
while i <= n:
    sum += i
    i += 1
    

print("합은 %d입니다." % sum)

print("=" * 50)

# for
sum = 0
for i in range(1, n + 1):
    sum += i

print("합은 %d입니다." % sum)
