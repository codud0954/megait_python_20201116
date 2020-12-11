# 1번째 방법
def average(s1, s2, s3, s4):
    average = (s1 + s2 + s3 + s4) / 4
    return average

score1, score2, score3, score4 = input("점수를 입력하세요: ").split()
score1 = int(score1)
score2 = int(score2)
score3 = int(score3)
score4 = int(score4)
average = average(score1, score2, score3, score4)

print("평균은 %.2f 입니다." % average)



# 2번째 방법
def average(*args):
    sum = 0
    for i in args:
        sum += i

    return sum / len(args)

# 이렇게하면 문제에서 3개의 값으로 변경되든, 5개로 변경되든 저 함수는 다 처리가능
score1, score2, score3, score4 = input("점수를 입력하세요: ").split()
score1 = int(score1)
score2 = int(score2)
score3 = int(score3)
score4 = int(score4)
average = average(score1, score2, score3, score4)

print("평균은 %.2f 입니다." % average)
