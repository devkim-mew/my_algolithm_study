import sys
sys.stdin = open("in.txt", "r")

#############################################

T = int(input())    # test_case 개수를 받아옴

for tc in range(1, T+1) :
    pass
    N = int(input())
    box_list = list(map(int, input().split()))  # 리스트 받아옴
    max_down = 0                                # 최대 낙차, i열에서 큰 수들 제외

    for i in range(N) :
        down = 0                                # 개별 낙차
        big_box_cnt = 0                         # i일 때 자신보다 큰 박스의 수
        for j in range(N) :                     #
            if box_list[j] > box_list[i] :
                big_box_cnt += 1
        max_down = max(max_down, big_box_cnt)

    print(max_down)


