#1.
import sys
sys.stdin = open("input.txt", "r")
#############################################

T = 10    # test_case 개수를 받아옴

for tc in range(1, T+1) :
    pass
    N = int(input())
    tower_list = list(map(int, input().split()))
    light = 0

    for tower in range(2, N-2) :
        max_around_tower = max(tower_list[tower-2], tower_list[tower-1], tower_list[tower+1], tower_list[tower+2])

        if tower_list[tower] > max_around_tower :
            light += tower_list[tower] - max_around_tower

    print(f"#{tc} {light}")


#2.







