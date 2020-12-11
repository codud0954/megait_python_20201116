# 설계도(클래스) 만들기
class Person:
    # 생성자(constructor)
    def __init__(self, name="홍길동", birth="19000101", gender="없음"):
        # 속성 (필드, 멤버변수)
        self.name = name
        self.birth = birth
        self.gender = gender

    # 행위 (메소드) - 동사
    def greet(self):
        print("안녕하세요~")

    def walk(self):
        print("뚜벅뚜벅")

    def introduce(self):
        return "내 이름은 %s이고 성별은 %s이다." % (self.name, self.gender)

    def get_age(self):
        # "19990101"
        yyyy = self.birth[:4]  # 일반 변수
        return 2020 - int(yyyy) + 1

boram = Person("신보람", "19990101", "여자")
# 멤버변수에 값 넣기
# boram.name = "신보람"
# boram.birth = "19990101"
# boram.gender = "여자"

# 메소드 호출
boram.greet()
boram.walk()
introduce_text = boram.introduce()
print(introduce_text)
print("나이는 %d세 입니다." % boram.get_age())
