# 큰 값 구하기

a, b, c = input("세 개의 수를 입력하세요: ").split()
a = int(a)
b = int(b)
c = int(c)

# max라는 변수를 만들어서 a, b, c를 비교하면서 큰 값을 max에 담는다.

max = a

if max < b:
    max = b

if max < c:
    max = c
    
# elif 로는 쓰면 안되는 이유는 만약 a b c 가  1 2 3 이었다면, 첫번째 조건이 만족해서 끝나버리고 다음 조건을 검사 안하기 때문에

print(max)
