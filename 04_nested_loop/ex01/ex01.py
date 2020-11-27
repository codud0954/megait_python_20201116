# 스쿼트 10회
'''
for i in range(10):
    print("앉았다 일어났다")
'''


# 스쿼트 10회 3세트

for i in range(3):
    for j in range(10):
        print("%d 세트째, %d번 앉았다 일어났다" % (i, j))


# 한줄짜리 별 5개 찍기
'''
for i in range(5):
    print("*", end=" ")
'''

# 한줄짜리 별 5개를 3행 찍기
for i in range(3):
    for j in range(5):
        print("*", end=" ")

    print()   # 줄바꿈
