n = int(input("입력: "))
sum = 0

# 1234 / 1000  => 1.234   몫:1  나머지:234
# 234 / 100    => 2.34    몫:2  나머지:34
# 34 / 10      => 3.4     몫:3  나머지:4

num = 1234
sum = 0
q = num // 1000  # 1
r = num % 1000   # 234
sum = sum + q
q = r // 100     # 2
r = r % 100      # 34
sum = sum + q
q = r // 10       # 3
r = r % 10        # 4
sum = sum + q
sum = sum + r
print(sum)

# 다른 방법
q, r = divmod(n, 1000)
sum += q
q, r = divmod(r, 100)
sum += q
q, r = divmod(r, 10)
sum += q
sum += r
print("합계는 %d 입니다." % sum)
