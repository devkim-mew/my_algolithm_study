import sys
sys.stdin = open("input.txt", "r")

"""
직사각형 모양의 종이를 잘랐을 때 가장 큰 종이 조각의 넓이를 구하자

W, H  종이의 가로 및 세로 길이, 최대 100
cut_num 자르는 횟수
가로로 자르는 경우 0, 점선번호
세로로 자르는 경우 1, 점선번호

가장 큰 구간을 구해보자

쪼갠 구간의 곱 중 가장 큰 수를 고르자

"""


# 문제: 직사각형 종이를 점선을 따라 자를 때, 가장 큰 종이 조각의 넓이를 구하자.
# 입력:
# - 첫 줄에 종이의 가로(W)와 세로(H) 길이가 주어진다. (최대 100)
# - 둘째 줄에 점선의 개수 n이 주어진다.
# - 이후 n개의 줄에 걸쳐 각 줄마다 "방향 번호"가 주어진다.
#   - 방향이 0이면 가로(세로 길이 H에서 자르는 위치)를 의미하고,
#   - 방향이 1이면 세로(가로 길이 W에서 자르는 위치)를 의미한다.
#
# 풀이 아이디어:
# 각 방향(가로, 세로)마다 자르는 점들을 모은 후,
# 종이의 가장자리(0과 전체 길이)를 포함하는 리스트를 만들고 정렬합니다.
# 이후 인접한 두 점 사이의 거리를 계산하여 가장 큰 간격을 구합니다.
# 최종적으로 두 방향에서 구한 최대 간격의 곱이 가장 큰 종이 조각의 넓이가 됩니다.


# 종이의 가로(W)와 세로(H) 길이를 입력받습니다.
W, H = map(int, input().split())

# 자르는 점선의 개수를 입력받습니다.
n = int(input())

# 가로 자르는(즉, 세로 길이에 영향을 주는) 점선과 세로 자르는(가로 길이에 영향을 주는) 점선을 저장합니다.
# 가장자리를 포함하기 위해, 처음과 끝 위치를 미리 추가합니다.
horizontal_cuts = [0, H]  # 가로 방향 자르기는 y좌표 기준 (세로 길이)
vertical_cuts = [0, W]     # 세로 방향 자르기는 x좌표 기준 (가로 길이)


# n개의 점선 정보를 읽어들입니다.
for _ in range(n):
    direction, pos = map(int, input().split())
    if direction == 0:
        # 0은 가로 점선: y 좌표에 해당
        horizontal_cuts.append(pos)
    else:
        # 1은 세로 점선: x 좌표에 해당
        vertical_cuts.append(pos)

# 각 리스트를 오름차순으로 정렬합니다.
horizontal_cuts.sort()
vertical_cuts.sort()

# 가로(세로 길이)에서 가장 큰 간격(높이)을 구합니다.
max_h_gap = 0
for i in range(1, len(horizontal_cuts)):
    gap = horizontal_cuts[i] - horizontal_cuts[i - 1]
    if gap > max_h_gap:
        max_h_gap = gap

# 세로(가로 길이)에서 가장 큰 간격(너비)을 구합니다.
max_w_gap = 0
for i in range(1, len(vertical_cuts)):
    gap = vertical_cuts[i] - vertical_cuts[i - 1]
    if gap > max_w_gap:
        max_w_gap = gap

# 가장 큰 종이 조각의 넓이는 두 최대 간격의 곱입니다.
largest_area = max_h_gap * max_w_gap

# 결과 출력 (단위 없이 숫자만 출력)
print(largest_area)



##############################################################
#
# W, H = map(int, input().split())
# cut_num = int(input())
# cut_idx = [tuple(map(int, input().split())) for _ in range(cut_num)]
# cut_W = []
# cut_H = []
# for i in cut_idx:
#     if i[0] == 0:
#         cut_H.append(i)
#     else:
#         cut_W.append(i)
# cut_W.sort()
# cut_H.sort()
#
# W_len = 0
# for w in cut_W:
#     if w[1] - W_len > W_len:
#         W_len = w[1] - W_len
#     if w == cut_W[-1] and W_len < W - cut_W[-1][1]:
#         W_len = W - cut_W[-1][1]
#
# H_len = 0
# for h in cut_H:
#     if h[1] - H_len > H_len:
#         H_len = h[1] - H_len
#     if h == cut_H[-1] and H_len < H - cut_H[-1][1]:
#         H_len = H - cut_H[-1][1]
#
# print(W_len * H_len)
#
# #############################################################
#
# W, H = map(int, input().split())
# cut_num = int(input())
# cut_idx = [tuple(map(int, input().split())) for _ in range(cut_num)]
# cut_W = []
# cut_H = []
# for i in cut_idx:
#     if i[0] == 0:
#         cut_H.append(i)
#     else:
#         cut_W.append(i)
# cut_W.sort()
# cut_H.sort()
#
# W_len = 0
# prev = 0
# for w in cut_W:
#     W_len = max(W_len, w[1] - prev)
#     prev = w[1]
# W_len = max(W_len, W - prev)
#
# H_len = 0
# prev = 0
# for h in cut_H:
#     H_len = max(H_len, h[1] - prev)
#     prev = h[1]
# H_len = max(H_len, H - prev)
#
# print(W_len * H_len)