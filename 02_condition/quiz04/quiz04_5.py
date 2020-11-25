"""
윷놀이
*  4개의 윷 상태가 입력되면 도, 개, 걸, 윷, 모를 출력하는 프로그램을 작성하시오.
* 윷의 상태가 0이면 뒤집어 지지 않은 상태, 1이면 뒤집어진 상태를 의미한다.
> 윷놀이는 4개의 윷을 이용하는 게임이다.
> 도 : 1개가 뒤집어진 상태  
> 개 : 2개가 뒤집어진 상태  
> 걸 : 3개가 뒤집어진 상태  
> 윷 : 4개가 뒤집어진 상태  
> 모 : 하나도 뒤집어지지 않은 상태  
"""

stick1, stick2, stick3, stick4 = input("윷 상태를 입력하세요: ").split()
stick1 = int(stick1)
stick2 = int(stick2)
stick3 = int(stick3)
stick4 = int(stick4)

cnt = stick1 + stick2 + stick3 + stick4

if cnt == 1:
    print("도")
elif cnt == 2:
    print("개")
elif cnt == 3:
    print("걸")
elif cnt == 4:
    print("윷")
else:
    print("모")
