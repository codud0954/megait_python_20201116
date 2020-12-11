# 1. 리스트 더하기
print("### 1 ###")
a = [1, 2, 3]
b = [5, 4, 3]
print(a + b)

# 2. append 함수: 리스트 마지막에 요소를 추가(어떤 자료형이든 가능)
print(a)
a.append(5)
a.append(4)
a.append(3)
print(a)

# 리스트 자체를 통째로 넣기
a.append(b)
print(a)

# 3. 원하는 위치에 값 넣기 insert(인덱스, 값)
# 2와 3 사이에 100 넣기
a.insert(2, 100)
print(a)

# 4. 길이 구하기 len()
print(len(a))

# 5. 요소값 삭제하기
print("### 5(1) ###")

# del : 파이썬이 자체적으로 가지고 있는 문법(index로 지운다)
del a[2]
print(a)

print("### 5(2) ###")
# remove(삭제할값) : 리스트 중 첫번째로 나오는 요소를 제거한다.
a.remove(3)
print(a)

print("### 5(3) ###")
# pop(삭제할 index) : index번째의 요소를 삭제하고, 삭제된 값을 반환한다.
deleted = a.pop(5)
print(deleted)
print(a)

# 6. 요소가 몇 개인지 count(값)
print("### 6 ###")
print(a.count(5))

# 7. 값의 위치(index) 반환 index(값)
print("### 7 ###")
print(a.index(3))
