weight = int(input("몸무게를 입력하세요 : "))

# if와 else문: if 조건이 아닌 모든 경우
if weight <= 70:
    print("치킨 먹자")
else:
    print("샐러드 먹자")


# if - elif - else문
  # if문 조건이 아닌 경우 elif 확인, elif 확인... 모든 조건 아닌 경우 else 확인
  # 이 조건들 중 무조건 하나의 조건에 걸린다. 처음에 걸렸다면 뒤 조건 확인 안함
  # 만약, 모든 조건들을 다 검사하려면 if문으로 쓰면 된다.
  # else 생략 가능
  
if weight <= 70:
    print("치킨 먹자")
elif weight <= 75:
    print("닭가슴살 먹자")
elif weight <= 80:
    print("샐러드나 먹자")
else:
    print("굶자")
