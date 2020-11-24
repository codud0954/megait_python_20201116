### 복합 대입 연산자(Assignment Operators)
|복합 대입연산자|등치|설명|
|------|------|------|
|a += b| a = a + b|a에 b를 더해서 a에 저장|
|a -= b| a = a - b|a에 b를 빼서 a에 저장|
|a *= b| a = a * b|a에 b를 곱해서 a에 저장|
|a /= b| a = a / b|a에 b를 나눠서 a에 저장|
|a %= b| a = a % b|a에 b를 나눈 나머지를 a에 저장|
|a **= b| a = a ** b|a에 b를 제곱해서 a에 저장|

### range 함수

* 0부터 n개까지 1씩 증가하는 range 객체가 반환된다.  
* **끝 숫자는 포함되지 않는다.**
* `0 <= n < 5` 
```
>>> a = range(5)
>>> a
range(0, 5)    # 0 1 2 3 4
```

　　
* 시작 숫자와 끝 숫자를 지정할 수도 있다.  
* 시작 숫자는 포함되고 **끝 숫자는 포함되지 않는다.**
* `3 <= n < 11`
```
>>> a = range(3, 11)
>>> a
range(3, 11)   # 3 4 5 6 7 8 9 10 
```

　　
* 반복문에서 사용하기
* `for i in range(n):`
```
for i in range(3):   # 0 <= i < 3
    print(i, end = " ")
```
> 결과
```
0 1 2
```

　　
* 반복문에서 사용하기(범위 지정)
* `for i in range(start, end):`
```
for i in range(5, 11):   # 5 <= i < 11
    print(i, end = " ")
```
> 결과
```
5 6 7 8 9 10
```

## 예제
- [예제1](ex01/ex01.py) - while 반복문
- [예제2](ex02/ex02.py) - for 반복문과 range 함수
- [예제3](ex03/ex03.py) - break, continue문

## 문제
- [문제1](quiz01/README.md) - while 반복문
- [문제2](quiz02/README.md) - for 반복문과 range 함수
- [문제3](quiz03/README.md) - break, continue문
- [문제4](quiz04/README.md) - 종합 문제
