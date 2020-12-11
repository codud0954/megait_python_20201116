num = int(input("입력: "))

# 1234 / 1000  => 1.234   몫:1  나머지:234
# 234 / 100    => 2.34    몫:2  나머지:34
# 34 / 10      => 3.4     몫:3  나머지:4

q = num // 1000  # 1
r = num % 1000   # 234
print(q)
q = r // 100     # 2
r = r % 100      # 34
print(q)
q = r // 10       # 3
r = r % 10        # 4
print(q)
print(r)

# 다른 방법
q, r = divmod(num, 1000)
print(q)
q, r = divmod(r, 100)
print(q)
q, r = divmod(r, 10)
print(q)
print(r)
