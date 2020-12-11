'''
*
**
***
****
*****
'''

# 2중 반복문
#   규칙: i번째 행에 별의 개수는 i개이다.
for i in range(1, 6):
    for j in range(i):      # 별을 i번 만큼 찍는다.
        print("*", end=" ")
    print() # 줄바꿈

    
# 1중 반복문으로 푸는법
for i in range(1, 6):
    print("*" * i)    # "*" 문자를 i번 곱한다.
