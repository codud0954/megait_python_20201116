# 파일 읽기

# 첫번째 파라미터: 읽을 파일 이름
# 두번째 파라미터: 옵션값 r 읽기
# 세번째 파라미터: 문자 인코딩
f = open("test1.txt", 'r', encoding='utf8')
print(f.read())  # 파일 내용 전체를 읽어온다.(위험)
line = f.readline() # 한 줄 읽기 : 읽을 때마다 읽은 줄이 소비된다.
print("line1:", line)

# 커서(cursor) 개념이므로 다 읽으면 맨 끝을 가리킨다.

# 커서를 맨 앞으로 옮기기
f.seek(0)
line = f.readline()
print("line2:", line)

f.seek(1)   # seek 함수는 글자 하나씩 이동
line = f.readline()
print("line3:", line)

f.seek(0)
# 한 줄씩 파일 전체 읽기
while True:
    line = f.readline()
    line = line.replace('\n', "")  # 줄바꿈 제거
    print(line)

    # 더이상 읽을 내용이 없을 때 반복문 종료
    if not line:    # line == "":
        break

f.seek(0)
print(f.readlines()) # 한 줄을 list에 담는다. (위험)

f.close()
