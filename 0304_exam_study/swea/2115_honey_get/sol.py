"""
원래는 DFS로 풀어야 함




"""

import sys
sys.stdin = open('input.txt', 'r')
###################################
T = int(input())

for tc in range(1, T+1):
    N, M, C = list(map(int, input().split()))
    honey_grid = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0

    # 일꾼1이 전체적으로 순회를 한다
    # 단, 벌통의 개수 M 직전까지만 순회를 한다
    for fst_i in range(N):      # 첫번째 일꾼의 i (행)
        for fst_j in range(N):  # 첫번째 일꾼의 j (열), 꿀통은 열로 연속되어야 한다.
            # 슬라이싱을 이용해서 첫번째 일꾼이 선택한 꿀통만 가져온다
            # 첫번째 일꾼이 선택한 꿀통리스트, 슬라이싱 해서 가져온다
            fst_select_honey_list = honey_grid[fst_i][fst_j: fst_j+M]

            # 가져온 쿨통에서 최대 이익을 구해보자
            # 부분집합을 구한 다음, 거기서 최대 이익을 구하자
            fst_select_honey_max = 0
            # 부분집합은 모든 조합의 경우의 수와 같음


    print(f"{tc}", max_sum)