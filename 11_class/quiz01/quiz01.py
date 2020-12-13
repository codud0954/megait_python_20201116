class Person:
    def __init__(self):
        # 1. 멤버변수
        name = None
        birth = None
        gender = None

    # 2. 메소드
    def greet(self):
        print("안녕하세요~ 반갑습니다!")

    def walk(self):
        print("걷는다")

    def introduce(self):
        print("내 이름은 %s이고, 성별은 %s입니다." % (self.name, self.gender))

    def age(self):
        yyyy = self.birth[0:4]
        age = 2020 - int(yyyy) + 1
        print("나이는 %d세 입니다." % age)

boram = Person()
boram.name = "신보람"
boram.birth = "19990101"
boram.gender = "여자"

boram.greet()
boram.walk()
boram.introduce()
boram.age()
