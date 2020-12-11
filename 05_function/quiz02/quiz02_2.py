def get_min(n1, n2, n3, n4, n5):
    min = n1
    if min > n2:
        min = n2
    if min > n3:
        min = n3
    if min > n4:
        min = n4
    if min > n5:
        min = n5
    print("최소값은 %d입니다." % min)

def get_min_new(*args):
    min = args[0]
    for i in args:
        if min > i:
            min = i
    print("최소값은 %d입니다." % min)

n1, n2, n3, n4, n5 = input("5개의 수를 입력하세요").split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
n4 = int(n4)
n5 = int(n5)
get_min_new(n1, n2, n3, n4, n5)
