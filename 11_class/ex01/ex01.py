# 클래스
class Cellphone:
    name = "핸드폰"  # 클래스 변수

    # 생성자(Constructor): 객체가 생성될 때 자동으로 불려지는 메소드(method)
    def __init__(self):
        print("객체가 생성되었다.")
        # 1. 속성: 멤버변수 또는 필드(field)
        self.model_name = None
        self.color = None
        self.price = 0
        self.maker = None

    # 2. 행위(기능): 멤버함수, method
    def call(self):
        print("전화하기")

    def camera(self):
        print("카메라 찰칵")

    def introduce(self):
        print("제조사는 %s이며 모델명은 %s이고 가격은 %d원 입니다."
              % (self.maker, self.model_name, self.price))

# 코드의 흐름이 있는 곳
# 인스턴스 화 => 객체로 만든다.
test = Cellphone()
print(type(test))

# 멤버변수(필드)에 값 넣기
test.model_name = "iphonepro11"
test.color = "gold"
test.price = 18300000
test.maker = "iphone"

# 멤버변수(필드) 값 출력하기
print(test.model_name)
print(test.color)
print(test.price)
print(test.maker)

# 메소드 호출
#   호출시에는 self를 넣지 않아도 된다.
test.call()
test.camera()
test.introduce()

test.model_name = "z플립"
test.maker = "삼성"
print(test.model_name)
print(test.maker)


# 메소드에 self가 붙는 이유
# 멤버변수는 객체마다 고유의 멤버변수들을 가지고 있으나 메소드는 하나만 만들어지고
# 각 객체들이 하나의 메소드를 공유해서 사용한다.
# 메소드 입장에서는 어떤 객체가 사용하는지 모르기 때문에 
# 어떤 객체가 불렀는지 알게 하기 위해서 self(객체를 통째로) 받는다.
