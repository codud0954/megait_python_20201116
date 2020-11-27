'''
함수 만들기
1. 어떤 함수를 만들지 (이름)
2. input(파라미터, 매개변수, argument, 인자)
3. output(결과값, return값)
4. 함수 내용 구현하기
'''
# 함수 만들기
def sum(x, y):
    result = x + y
    return result

def minus(x, y):
    print("x - y = %d" % (x - y))

def add_many(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

# 함수 사용하기
a = 3
b = 10
result = sum(a, b)
print(result)
print(sum(a, b))

minus(a, b)
print(add_many(10, 20, 30, 40, 50))
