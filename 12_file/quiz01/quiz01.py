# 1. file 쓰기를 통해서 csv 파일로 저장
f = open('product.csv', 'w', encoding='utf8')
f.write("새우깡,1300\n")
f.write("육개장,850\n")
f.write("스크류바,1200\n")
f.write("츄파춥스,200\n")
f.write("꼬북칩,1500\n")
f.close()

f = open('product.csv', 'r', encoding='utf8')
# {"새우깡":1300, "육개장":850, "스크류바":1200, "츄파춥스":200, "꼬북칩":1500}
product_dict = dict()
while True:
    line = f.readline()
    if not line:
        break

    line = line.replace('\n', '')  # 줄바꿈 제거
    name, price = line.split(',')
    product_dict[name] = int(price)


print(product_dict)
# 2. 새우깡 1개 육개장 1개 츄파춥스 3개의 합산 가격을 계산하세요.
shrimp_price = product_dict.get('새우깡')
noodle_price = product_dict.get("육개장")
candy_price = product_dict.get("츄파춥스")
sum_price = shrimp_price + noodle_price + (candy_price * 3)
print("%d원" % sum_price)

# 3. 스크류바는 2+1 행사를 한다. 196개를 샀을 때 가격
screwbar_price = product_dict.get("스크류바")
# 몇 개가 공짜로 얻어지는가?
# 196 // 3 => 65개 
# 공짜로 얻어진 65개를 뺀 가격을 구하면 된다. 196 - 65 => 131개
sum_price = (196 - (196 // 3)) * screwbar_price
print("%d원" % sum_price)

# 다른 방법
q, r = divmod(196, 3)  # q:65, r:1
# 지불해야하는 2개 상품의 계산 + 2+1이 되지 않은 지불해야하는 값
sum_price = (q * (screwbar_price * 2)) + (screwbar_price * r)
print("%d원" % sum_price)

f.close()
