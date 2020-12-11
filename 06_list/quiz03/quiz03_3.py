scores = [8, 7, 8, 8, 9, 4, 6, 8, 10, 8]

scores.sort()
print(scores)

# 첫 번째 인덱스와 마지막 인덱스를 제거해야 한다.

# 삭제하는 법
# 1. del 리스트[idx]
# 2. 리스트.pop(idx) 
# 3. 리스트.remove(값)

del scores[0]
del scores[len(scores) - 1]     # [0, 1, 2]  len: 3
print(scores)

sum = 0
for score in scores:
    sum += score

average = sum / len(scores)

print("최고점과 최저점을 제외한 평균 점수는 %g점 입니다." % average)
