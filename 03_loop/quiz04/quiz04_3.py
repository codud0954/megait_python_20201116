n = int(input("수를 입력하세요: "))

# while

i = 1
while i <= n:
    if n % i == 0:
        print(i, end = " ")

    i += 1

print("")
print("=" * 50)

# for

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end = " ")
