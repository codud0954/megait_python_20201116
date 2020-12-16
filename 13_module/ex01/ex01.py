# math 모듈 가져오기
import math     # 모듈이름을 명시해서 변수나 함수를 사용할 수 있다.

# math 모듈 이름의 별명 짓기
import math as m     # as 뒤의 별명으로 변수나 함수를 사용할 수 있다.

# 모듈의 일부만 가져오기(모듈 이름을 명시하지 않아도 가져온 변수나 함수 이름으로 바로 사용 가능)
from math import *    # math 모듈의 전체를 가져온다.
from math import pi   # math 모듈의 pi 변수만 가져온다.
from math import sqrt   # math 모듈의 sqrt 함수만 가져온다.

# random 모듈 가져오기
# import random
from random import randrange

# qrcode, pillow <- 추가로 설치 필요
import qrcode

img = qrcode.make("http://naver.com")
img.show()
img.save("qr.png")

# math의 pi 사용법
print(math.pi)
print(m.pi)
print(sqrt(9))  # 루트 씌우기

# 모듈 이름 안붙이고 부르기 (from)
print(sqrt(9))
print(pi)

# 주사위 던지기(1~6)
dice = randrange(1, 7) # start <= dice < stop
print(dice)
