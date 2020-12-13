# 등차수열 1 4 7 10 13 16 19 22 25...
# 1부터 3을 더해 다음 수를 만든 수열

a, d, n = input("세 개의 수를 입력하세요: ").split()
a = int(a)
d = int(d)
n = int(n)

result = a   # 시작값
for i in range(n - 1):  # 시작값이 첫번째를 의미하므로 2번째부터 시작(n - 1 : 반복 개수를 1 줄임)
    result += d   # 더할값

print(result)
