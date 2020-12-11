# 산술연산자
noodle_cup = 850;

print("육개장 가격:", noodle_cup)

# 3개 가격 계산
sum = noodle_cup * 3;
print("육개장 3개의 가격:", sum)

# 가격 상승
noodle_cup = 950;

sum = noodle_cup * 3;
print("육개장 3개의 가격:", sum)
# 또는
print("육개장 3개의 가격:", noodle_cup * 3)

# 변수 여러개
print("육개장 하나의 가격은", noodle_cup, "이고, 3개의 가격은", sum, "입니다.")


# 10,000원으로 육개장 3개를 산 후 거스름돈 구하기
money = 10000
change = money - sum
print("거스름돈: ", change)

# 5,000원으로 육개장 몇 개를 살 수 있고, 거스름 돈은 얼마나 남는가?
money = 5000
buy_noodle_cup = money / noodle_cup
print("살 수 있는 개수", buy_noodle_cup) # 5개인데 소수로 나온다. 몫만 구하려면 //

buy_noodle_cup = money // noodle_cup
print("살 수 있는 개수", buy_noodle_cup)

change = money % noodle_cup  # 나머지 구하는 연산자 %
print("거스름돈", change)


# 제곱
# 5^2
print("5의 2제곱", 5 ** 2)
