# 거꾸로 된 삼각형 출력하기
'''
*****
****
***
**
*
'''

# 첫 번째 방법
for i in range(5, 0, -1): # 5 4 3 2 1 (5개의 행)
    for j in range(i): # 5 4 3 2 1 (별의 개수)
        print("*", end = " ") # 한 줄에 연속해서 출력

    print()  # 한 행이 끝나면 줄바꿈 처리

# 두 번째 방법
for i in range(5): # 0 1 2 3 4
    for j in range(5 - i): # 5 - i개 만큼 별의 개수 출력
        print("*", end = " ")

    print() # 한 행이 끝나면 줄바꿈 처리
