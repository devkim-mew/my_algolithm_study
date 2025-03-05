import sys
sys.stdin = open("input.txt", "r")



"""
0 ~ 9 까지 10장의 카드 중 6개만 임의로 뽑았을 때

3장의 카드가 연속적인 번호를 갖는 경우를 run
동일한 카드가 3개인 경우는 triplet

6장이 run 과 triplet으로 이루어진 경우를 baby gin이라 함

baby gin은 True
아니면 False를 보내자


순서가 중요하니 일단 순열

"""

from itertools import permutations


def is_babygin(cnt_list):
    # run인지 확인
    # 해당 숫자의 개수가 1이상이면 가능성이 있음
    babyjin = 0
    idx = 0
    while idx < 10 : # for문으로 돌리면 문제가 있음
        # if cnt_list[idx] >= 1 and cnt_list[idx+1] >= 1 and cnt_list[idx+2] >= 1: # 중첩하여 사용도 가능
        # run은 0~7까지만 체크해야 함
        if idx <= 7 : # idx가 8이라면 그 뒤는 판단할 필요가 없기 때문에 기본값인 false가 출력(이것이 단축평가)
            if cnt_list[idx] >= 1 :
                if cnt_list[idx+1] >= 1:
                    if cnt_list[idx+2] >= 1:
                        babyjin += 1
                        cnt_list[idx] -= 1  # 확인한 카드들은 빼줘야 함
                        cnt_list[idx+1] -= 1
                        cnt_list[idx+2] -= 1
                        continue
        idx += 1

    # triplet 확인
    # 해당 숫자의 개수가 3이상이면 됨
    while idx <= 10 :
        if cnt_list[idx] >= 3:
            babyjin += 1
            cnt_list[idx] -= 3
            continue
        idx += 1

    return babyjin == 2


T = int(input())

for tc in range(1, T+1) :
    card_list = list(map(int, input()))

    cnt_list = [0]*10 # 카드 번호별(인덱스)로 0값으로 초기화
    # 카드 번호의 개수를 세자
    for i in card_list:
        cnt_list[i] += 1

    # print(cnt_list) # 각 카드를 확인할 수 있음

    result = "false"
    if is_babygin(cnt_list):























