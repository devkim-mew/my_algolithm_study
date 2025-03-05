import sys
sys.stdin = open("input.txt", "r")

"""
길이가 100인 정사각형의 도화지에서 
길이가 10인 정사각형의 색종이를 붙인다

색종이가 붙은 영역의 넓이를 구해보자

겹치는 부분은 빼자
"""

N = int(input())
color_p_list = [tuple(map(int, input().split())) for _ in range(N)]
white_board = [[0]*100 for _ in range(100)]                             # 보드
cnt = 0

for i, j in color_p_list:                                               # 색종이 첫 좌표 가져와서
    for tx in range(10):
        for ty in range(10):
            if white_board[i+tx][j+ty] == 0:                            # 0일 경우 전부 칠해준다
                white_board[i+tx][j+ty] += 1
                cnt += 1                                                # 그리고 카운팅

print(cnt)
