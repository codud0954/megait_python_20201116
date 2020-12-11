def sum_limit_100(n):
    sum = 0
    last_num = 0
    for i in range(1, n + 1):
        sum += i
        last_num = i
        
        if sum > 100:
            break

    return (sum, last_num)

n = int(input("수를 입력하세요: "))
sum, last_num = sum_limit_100(n)
print("합은 %d이고 마지막으로 더해진 수는 %d이다." % (sum, last_num))
