## 파이썬 개발환경 구축  
* [파이썬 다운로드](https://www.python.org/downloads/windows)  
1. Windows x86-64 executable installer
2. add Python 3.8 to Path **꼭 체크하기**
3. success 후 disable path length.. 클릭 > 예   
* cmd > python 
* [Pycharm 프로그램 다운로드](https://www.jetbrains.com/ko-kr/pycharm/download/#section=windows)
  * Community용 설치
  
## 자료형(Data Type)의 종류
* 자료형이 무엇인지 확인할 때는 type() 함수를 사용한다.  

|자료형(type)| 설명|
|------|------|
|None | 비어있음 |
|Boolean|True(참) 또는 False(거짓)|
|Int|정수(Integer)|
|Float|실수(Float)|
|String|문자열|  
  
## 산술 연산자 종류

|산술연산자|	설명|
|------|------|
|+| 더하기|
|-| 빼기 |
|*	|곱하기|
|**	|제곱|
|/| 나눈 후 결과 (소수 또는 정수)|
|//| 나눈 후 결과 (정수)|
|%|나눈 후 나머지|

## format 종류
문자열 속에서 다른 타입의 값을 출력할 때 format을 사용한다.  

|format|	설명|
|------|------|
|%d| 정수(0~9)|
|%f| 실수(소수점). %.1f: 소수점 한 자리까지, %.2f: 소수점 두 자리까지  |
|%g| 정수 또는 실수. 실수 자동 표시|
|%c| 문자|
|%s|문자열(문장)|
|%o	|8진수(0~7)|
|%x	|16진수(0 ~ 9, A ~ F)|

## 파이참 유용한 단축키
|기능 |단축키 |
|------|------|
|파일 이름 변경 | Shift + F6|
|주석 처리/해제 | 선택된 영역에서 Ctrl + /|
|전체 실행|alt + shift + F10|
|블록 실행|alt + shift + e|
|커서 위치한 줄 복사| Ctrl + d |
|커서 위치한 줄 삭제| Ctrl + y|

## 파이썬 Style 가이드 사이트

[파이썬 스타일 가이드](https://google.github.io/styleguide/pyguide.htm)

## 파이썬 이름짓기 가이드

```
module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, 
instance_var_name, function_parameter_name, local_var_name
```
> [참조 사이트](https://google.github.io/styleguide/pyguide.html#3164-guidelines-derived-from-guidos-recommendations)

# 파이참에서 'no python interpreter configured for the project'가 뜰 때 해결법
https://marobiana.tistory.com/161
