# 리스트 값 초기화
numbers = [89, 98, 100, 70]
print(numbers)

# 리스트 값 초기화(문자)
chars = ["a", "b", 'c', 100]
print(chars)

# range 함수를 리스트로 변환
r_list = list(range(5, 10))
print(r_list)

# 동적으로 값 할당하기 => append()
animals = list()
print(animals)
animals.append("사자")
animals.append("고양이")
animals.append("개")
print(animals)

# 요소값 출력(index)
print(animals[0])
print(animals[1])
print(animals[2])

# 개 -> 강아지: 요소값 변경
animals[2] = '강아지'
print(animals[2])
print(animals)

#animals[4] = '코끼리'

# 반복문으로 출력하기(index)
for i in range(len(animals)): # 0 1 2 => 3
    print(animals[i])

# 반복문으로 출력하기(값)
for animal in animals:
    print(animal)
