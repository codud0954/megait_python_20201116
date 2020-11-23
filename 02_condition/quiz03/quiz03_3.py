bmi = int(input("bmi 수치를 입력하세요: "))

if bmi <= 10:
    print("정상")
elif bmi <= 20:
    print("과체중")
elif bmi > 20:
    print("비만")
