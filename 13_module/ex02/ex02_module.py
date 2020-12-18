# ex02_module.py
# 직접 만들어보는 모듈

# 모듈은 변수도 쓸 수 있고, 함수도 쓸 수 있다고 했다.

# 변수
module_author = "신보람"   # 모듈 만든 사람 이름을 변수로 저장해보자

# 함수

# 1. 주어진 리스트를 역순으로 리턴해주는 함수
def reverse_list(target_list):
    # ['a', 'b', 'c']  => ['c', 'b', 'a']
    #  0     1    2        2     1    0
    #  -3   -2   -1        -1   -2    -3

    # 리스트의 길이만큼 index 역순으로 저장하면 될 것
    # # 시간이 있다면 풀어보도록 시켜도 OK

    # 방법 1)
    '''
        reverse = list()
        for i in range(1, len(target_list) + 1):  # 1, 2, 3이 되도록 함  - 4가 포함 안되므로 +1
            reverse.append(target_list[i * -1])   # -1 을 곱해서 -1, -2, -3 이 되게 함

        return reverse
    '''

    # 방법 2)
    reverse = list()
    for i in range(len(target_list)):
        reverse.append(target_list[len(target_list) - i - 1])   # 길이가 3으로 나오므로 1을 더 빼준다. 길이에서 증가되는 i를 계속 빼주면 2 1 0이 됨

    return reverse

# 모듈을 import한 곳에서 자동 수행되는 것을 막기 위함. 모듈 안에서 테스트할 때만 수행된다.
if __name__ == "__main__":
    list1 = ['a', 'b', 'c']
    print(reverse_list(list1))
