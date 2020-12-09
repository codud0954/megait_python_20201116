'''
Dict 자료구조(dictionary)
1. key와 value 쌍으로 이루어져 있다.
2. key는 변하지 않는 값('apple'), 튜플, value는 모두 사용 가능하다.
3. key로 value를 찾는 구조로 사용한다.
'''
# dict 만들기
dict1 = {'name':'신보람', '생년월일':19990101, '성별':'여자'}
print(dict1)

# dict에 값 추가하기
dict1['나이'] = 22
print(dict1)

dict1['로또'] = [23, 5, 7, 13, 45, 10]
print(dict1)

# dict에 중복되는 키를 넣으면 => 값이 변경된다.
dict1['나이'] = 30
print(dict1)

# dict에 tuple을 키로 넣으면?
dict1[(10, 20, 30)] = 500
print(dict1)

# dict에 list를 키로 넣으면?  => 안된다
# dict1[[10, 20, 30]] = 300
# print(dict1)

# 요소 삭제하기
del dict1['로또']
print(dict1)

del dict1[(10, 20, 30)]
print(dict1)

# key를 통해 값 얻기 (1)
print(dict1['name'])
print(dict1['생년월일'])
print(dict1['성별'])
print(dict1['나이'])

# key를 통해 값 얻기 (2)
print(dict1.get('name'))
print(dict1.get('생년월일'))
print(dict1.get('성별'))
print(dict1.get('나이'))

# key들을 모아서 List로 만들기 =>  ['name', '생년월일', '성별', '나이']
dict_keys = dict1.keys()
print(list(dict_keys))

# value들을 모아서 List로 만들기 => ['신보람', 19990101, '여자', 30]
print(list(dict1.values()))

# key, value를 쌍으로 해서 Tuple List로 묶기 => [(키, 값), (키, 값), (키, 값)...]
print(list(dict1.items()))

# Key가 dict에 있는지 확인하기(존재 여부)
if '나이' in dict1:
    print("나이 정보가 있습니다.")
else:
    print("나이 정보가 없습니다.")

# dict 값 모두 지우기
dict1.clear()
print(dict1)

t1 = (1, 2, 3)
s1 = {1, 2, 3}
s1.clear()
print(s1)
