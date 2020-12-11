'''
Set을 초기화 하는 방법
'''
# set을 만드는 방법 1
s1 = {1, 2, 3, 3}
# 중복이 알아서 제거된다.
print(s1)

# set을 만드는 방법 2 - set 함수에 String 값을 넣는다.
s2 = set("hello")
print(s2)

# 숫자로는 초기화 할 수 없다.
#s3 = set(8, 3, 5)

# 튜플은 set으로 초기화 가능하다
s3 = set((8, 3, 5))   # set 함수는 파라미터를 하나만 받는것이다

# set 함수에 리스트를 넣는다.
s3 = set([3, 4, 5, 6])
print(s3)


'''
Set 추가, 삭
add, update, remove
'''

# 값 한 개 추가하기(add)
s4.add(10)
print(s4)

# 값 여러 개 추가하기(update)
s4.update([100, 101, 102])
print(s4)

# 특정 값 제거하기(remove)
s4.remove(3)
print(s4)

print("=" * 50)

'''
집합 구하기
'''

set1 = {1, 2, 3, 4}
set2 = set([2, 4, 6, 8])

# 합집합

print("합집합 1:", set1 | set2)
print("합집합 2:", set1.union(set2))

# 교집합

print("교집합 1:", set1 & set2)
print("교집합 2:", set1.intersection(set2))

# 차집합
print("차집합 1:", set1 - set2)
print("교집합 2:", set1.difference(set2))
