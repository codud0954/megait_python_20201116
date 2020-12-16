import random

lotto = list()

while (len(lotto) < 6):  # 참인 동안 루프가 돈다.
    randNum = random.randrange(1, 46) # 1 ~ 45
    # 중복된 번호가 나오면 밑에 내용을 수행하지 않고 조건을 본다.
    if randNum in lotto:
        continue

    lotto.append(randNum)

print(lotto)
