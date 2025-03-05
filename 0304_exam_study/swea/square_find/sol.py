
"""
크기가 N*N인 2차원 배열 내부에 1로 채워진 사각형이 있음
사각형의 가로 세로 칸 수를 곱한 값을 출력하자
사각형이 여러개이므로 max를 찾아야

1의 위치를 찾고 찾은 곳에서 가로길이 확인 후 세로 길이 확인
가로 * 세로 후 max인지 확인
그 다름 또 반복 후 max 값 찾기

어떻게 풀까?
1의 위치 좌표를 찾고
해당 위치에서 가로 길이 계산, 해당 위치 에서 세로길이 계산
가로와 세로를 곱하고
최대값인지 확인

입력
T : 1 < T < 50
N : N*N 배열의 크기 (1 < N < 100)

"""

import sys
sys.stdin = open("11039_sample_in.txt", "r")

def get_col_lenth(row, col):
    col_lenth = 0                   # 세로 길이
    for j in range(col, N):         # 세로의 그 지점부터 끝까지
        if arr[row][j] == 0:        # 0이 되는 곳을 찾는다면 반복종료
            break
        else:
            col_lenth += 1          # 1이라면 카운팅
    return col_lenth                # 세로길이 반환

def get_row_lenth(row, col):
    row_lenth = 0
    for i in range(row, N):
        if arr[i][col] == 0:
            break
        else:
            row_lenth += 1
    return row_lenth


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]   # 사각형 정보 받아오기
    result = 0                                                  # 큰 사각형 값

    for row in range(N):                                        # 정사각형을 돌면서 큰 사각형을 찾자
        for col in range(N):
            if arr[row][col] == 1:                              # 사각형의 첫 지점을 찾으면
                col_lenth = get_col_lenth(row, col)             # 세로탐색먼저
                row_lenth = get_row_lenth(row, col)             # 가로탐색
                max_re = col_lenth * row_lenth                  # 가로세로 곱한 뒤
                result = max(max_re, result)                    # 큰 수로 업데이트

    print(f"#{tc}", result)


















# def get_col_lenth(row, col):
#     col_len = 0
#     for j in range(col, N):
#         if arr[row][j] == 0:
#             return col_len
#         else:
#             col_len += 1
#
# def get_row_lenth(row, col):
#     row_len = 0
#     for i in range(row, N):
#         if arr[i][col] == 0:
#             return row_len
#         else:
#             row_len += 1
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     max_area = 0
#
#     # 1좌표 찾자
#     for row in range(N):
#         for col in range(N):
#             if arr[row][col] == 1:
#                 # 가로의 길이 함수를 만들어 보자
#                 # 코드를 함수로 만들 떄는 네모를 그려보고 외부에서 받아오는 값을 인풋으로 결정
#                 # 함수를 사용할 떄는 리턴 값을 받아야 하는지 고민해야
#                 col_lenth = get_col_lenth(row, col)
#                 # 세로의 길이
#                 row_lenth = get_row_lenth(row, col)
#
#                 # 0이 되면 곱하지 못하니 안에서 곱해줘야 함
#                 # if 문을 쓸 떄는 결과 저장의 위치를 꼭 고민해야
#                 area = col_lenth * row_lenth
#
#                 # 최대값도 안에서 구해야 함
#                 if max_area < area:
#                     max_area = area
#
#     print(f"#{tc}", max_area)
#
#
#










