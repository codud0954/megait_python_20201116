# 파일 쓰기

# 첫번째 파라미터: 파일 이름
# 두번째 파라미터: 옵션값 w 새로 쓰기, a 기존 내용에 쓰기
# 세번째 파라미터: 문자 인코딩   encoding='인코딩 종류'
f = open("test1.txt", 'w', encoding='utf8')
# data = "안녕하세요\n파일쓰기 입니다."
# f.write(data)

# 반복문을 통해서 파일 내용 쓰기
for i in range(1, 11):  # 1 ~ 10
    data = "%d번째 줄입니다.\n" % i
    f.write(data)

f.close()  # 파일 쓰기에서는 특히 close를 꼭 해주어야 한다.
