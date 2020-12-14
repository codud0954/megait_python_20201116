# csv 파일 쓰기/읽기

# csv 파일 만들기
# f = open('member.csv', 'w', encoding='ms949')
# f.write("유재석,49,=\"01011112222\"\n")
# f.write("이효리,30,=\"01012346666\"\n")
# f.write("강호동,55,=\"01014563555\"\n")
# f.close()

# csv 파일 열기
f = open('member.csv', 'r', encoding='ms949')
while True:
    line = f.readline()
    if not line:
        break

    line = line.replace("\n", "")   # 줄바꿈 제거
    line = line.replace("=", "")    # = 제거
    line = line.replace('"', "")    # " 제거
    #print(line)
    name, age, phone = line.split(',')
    print("이름은 %s이고 나이는 %d, 번호는 %s이다." % (name, int(age), phone))


f.close()
