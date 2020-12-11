numbers = [3, 8, 9, 4, 2, 1, 7, 5]

# 1. List의 4번째 값을 6으로 바꾸고 전체를 출력하세요.
numbers[3] = 6
print(numbers)

# 2. List의 값 중 가장 큰 값을 출력하세요
# 가장 큰 값은 9 입니다.
max = numbers[0]
for num in numbers:
    if max < num:
        max = num

print("가장 큰 값은 %d 입니다." % max)

# 3. List의 모든 수의 합
# 합은 39 입니다.
sum = 0
for num in numbers:
    sum += num

print("합은 %d 입니다." % sum)
