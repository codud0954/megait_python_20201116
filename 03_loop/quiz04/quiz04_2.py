n = int(input("수를 입력하세요: "))

# while

i = 2
fact = 1
while i <= n:
    fact *= i
    i += 1

print("%d!는 %d입니다." % (n, fact))

print("=" * 50)

# for

fact = 1
for i in range(2, n + 1):
    fact *= i

print("%d!는 %d입니다." % (n, fact))
