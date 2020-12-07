t0 = 1,
print(t0)

t1 = (1, 2, 3)
# index로 접근하기
print(t1[0])
print(t1[1])
print(t1[2])

# 튜플은 요소값을 수정할 수 없다.
# t1[0] = 100
# print(t1[0])

# 튜플끼리 더하기
t2 = ('a', 'b', "c")
print(t1 + t2)

# 튜플 곱하기
print(t2 * 3)

# 길이 구하기
print(len(t2))

# 슬라이싱  [:]
# t2 값에서 'b', 'c'
print(t2[1:3])

# t2 값에서 'b'
print(t2[1:2])

# divmod() 함수 사용하기
q, r = divmod(100, 7)
print("몫은 %d이고, 나머지는 %d이다." % (q, r))

result_tuple = divmod(100, 6)
print("몫은 %d이고, 나머지는 %d이다." % result_tuple)
