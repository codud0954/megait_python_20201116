# 윤년 개수
year1, year2 = input("두 개의 연도를 입력하세요:").split()
year1 = int(year1)
year2 = int(year2)

leap_year_cnt = 0
for year in range(year1, year2 + 1):
    condition1 = year % 4 == 0 and year % 100 != 0
    condition2 = year % 400 == 0

    if condition1 or condition2:
        leap_year_cnt += 1

print(leap_year_cnt)
