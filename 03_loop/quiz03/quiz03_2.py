sum = 0
for i in range(3, 51): # 3 ~ 50
    if i % 3 != 0:
        continue

    sum += i

print(sum)
