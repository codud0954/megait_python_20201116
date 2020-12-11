# 과락 포함 합격 여부

score1, score2 = input("두 개의 점수를 입력하세요: ").split()
score1 = int(score1)
score2 = int(score2)

average = (score1 + score2) / 2

if score1 <= 50 or score2 <= 50:
    print("과락")
elif average < 60:
    print("불합격")
else:
    print("합격")
