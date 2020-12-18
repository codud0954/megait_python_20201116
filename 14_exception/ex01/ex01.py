# 예외처리(Exception): 프로그램 실행 시점(run time)에서 발생되는 오류
# try - except - finally

try:
    # 0으로 나누려고 시도 (ZeroDivisionError)
    # div = 1000 / 0

    # 잘못된 인덱스 참조 (IndexError)
    # list1 = [1, 2, 3]
    # print(list1[4])

    # 잘못된 타입 변환 (ValueError)
    text = 'abc'
    number = int(text)
except ZeroDivisionError as ze:
    print("0으로 나누면 안된다")   # 해당 오류가 발생하면 except문으로 오게된다. 개발자가 처리
except IndexError as ie:
    # pass  # 아무것도 안하고 싶으면
    print("잘못된 인덱스 참조")
except ValueError as ve:
    pass # 아무것도 안하고 싶으면
except Exception as e:  # 모든 익셉션들을 다 잡을 수 있다. (예외처리 이름을 모를 때 사용)
    pass
finally:
    print("마지막 처리") # 오류가 나지않고 try만 수행됐든, 오류가나서 except에 들어갔든 꼭 불려진다. 디비같은 경우 connection을 열면 닫아주지 않으면 계속 물고있어서 close 해줘야함

# 직접 예외를 발생시키기: raise
num = int(input("1부터 3까지의 숫자를 입력하세요: "))
if num < 1 or num > 3:
    raise ValueError

print("수행 끝")
