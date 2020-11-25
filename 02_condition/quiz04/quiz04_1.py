# 평균 합격 구하기

score1, score2 = input("두 점수를 입력하세요: ").split()
score1 = int(score1)
score2 = int(score2)
average = (score1 + score2) / 2

if average >= 70:
    print("합격입니다.")
else:
    print("불합격입니다.")
