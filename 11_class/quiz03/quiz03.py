# 제품관리 설계도
class Product:
    # 생성자
    def __init__(self, name, price, expired_date):
        self.name = name
        self.price = price
        self.expired_date = expired_date

    # 제품 정보
    def product_info(self):
        print("이름:", self.name)
        print("가격:", self.price)
        print("유통기한", self.expired_date)

    # 제품 n개의 가격
    def price_of_product(self, count):
        return count * self.price

    # 판매 가능 여부
    def sale_status(self):
        # 오늘 날짜 <= 유통기한 날짜 : 판매 가능 상품
        # 오늘 날짜 > 유통기한 날짜 : 판매 불가 상품
        today = "2020-12-14"
        if today <= self.expired_date:
            return "판매 가능 상품"
        else:
            return "판매 불가 상품"


# 객체 생성
shrimp = Product("새우깡", 1300, "2021-03-01")
shrimp.product_info()
print()
print("제품 5개의 가격 : %d" % shrimp.price_of_product(5))
print("제품 13개의 가격 : %d" % shrimp.price_of_product(13))
print(shrimp.sale_status())
