print("2020 / 7\n")
print(" S  M  T  W  T  F  S")

for day in range(-2, 32):
    if day < 1:
        print("   ", end="")
    elif day < 10:
        print(" %d " % day, end="")
    else:
        print("%d " % day, end="")

    if day == 4 or day == 11 or day == 18 or day == 25:
        print() # 줄바꿈
