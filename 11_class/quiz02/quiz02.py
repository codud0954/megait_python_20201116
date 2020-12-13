class Rectangle:
    # 생성자
    def __init__(self, width = 10, height = 10):
        self.width = width
        self.height = height

        print("가로 %dcm, 세로 %dcm 사각형이 만들어졌습니다." % (self.width, self.height))

    # 넓이
    def area(self):
        return self.width * self.height

    # 둘레
    def perimeter(self):
        return (self.width * 2) + (self.height * 2)

rect1 = Rectangle(30, 50)
print("사각형의 넓이는 %dcm^2 입니다." % (rect1.area()))
print("사각형의 둘레는 %dcm 입니다." % (rect1.perimeter()))

rect2 = Rectangle()
print("사각형의 넓이는 %dcm^2 입니다." % (rect2.area()))
print("사각형의 둘레는 %dcm 입니다." % (rect2.perimeter()))
