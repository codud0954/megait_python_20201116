a = [10, 1, 8, 2, 5]

# 1. 정렬하기 (오름차순)
a.sort() # 저장까지 된다.
print(a)

# 2. 정렬하기 (내림차순)
a.reverse() # 저장까지 된다.
print(a)

# 3. 슬라이싱
a = [10, 1, 8, 2, 5]
# [10, 1, 8]
slice_a = a[0:3] # 0 ~ 2
print(slice_a)
print(a[:3])

# [8, 2, 5]
print(a[2:5]) # 2 ~ 4
print(a[2:])

# 4. 어떤 값이 리스트에 포함되었는지 확인
if 5 in a:
    print("a 리스트에 5가 들어있다.")
else:
    print("a 리스트에 5가 들어있지 않다.")
