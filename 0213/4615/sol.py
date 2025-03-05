import sys
from pprint import pprint
sys.stdin = open("sample_input(1).txt", "r")

"""
오셀로 게임을 구현해보자
오셀로는 내 돌 사이에 상대 돌이 있다면 그 사이 모든 상대돌을 내 돌로 바꾸는 게임이다
게임이 끝났을 떄의 흑돌과 백돌의 개수를 출력하자

보드의 길이와 돌을 두는 횟수가 주어지고
그 다음부터는 좌표와 돌의 색이 연속하여 입력된다

어떻게 풀까?
먼저 빈 보드를 만들고
해당 좌표에 돌을 두는 for 문을 돌린다

돌을 둘 때, 상하좌우 대각선 방향으로 상대 돌을 찾았다면
델타 탐색으로 if로 상대돌 확인 및 상대돌 좌표 저장

그 다음에 내 돌이 있는 지 확인하고 상대돌을 바꾼다
해당방향으로 한칸 더 가서 if로 내 돌 확인 후 저장된 좌표를 내 돌로 바꿈

그리고 for 문이 끝났을 때 돌 상태 출력
"""

T = int(input())    # test_case 개수를 받아옴

for tc in range(1, T+1) :
    N, M = map(int, input().split())                    # N 보드의 길이, M 돌을 두는 횟수
    board = [([0]*N) for _ in range(N)]                 # 보드 생성
    board[N//2-1][N//2] = 1                             # 보드 돌 셋팅
    board[N//2][N//2-1] = 1
    board[N//2-1][N//2-1] = 2
    board[N//2][N//2] = 2

    for turn in range(M):                                       # 횟수 만큼 턴을 돎
        turn_x, turn_y, player = map(int, input().split())      # 돌 두는 값을 받아옴

        board[turn_x-1][turn_y-1] = player                      # 현재 플레이어의 돌을 둠

        dxy = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dx, dy in dxy:
            x = turn_x-1
            y = turn_y-1

            if 0 <= x < N and 0 <= y < N:                       # out of range 방지
                change = []                                     # 바꿔버릴 대상들을 잠시 저장
                for _ in range(N):                              # 내 돌을 찾을 때까지 상대돌인지 확인하기 위해 순회
                    x += dx
                    y += dy
                    if 0 <= x < N and 0 <= y < N:
                        if board[x][y] == [0, 2, 1][player]:    # 상대돌이라면 일단 저장 후 다음 것도 확인
                            change.append([x, y])
                        elif board[x][y] == 0:                  # 중간에 비어있다면 그만 둠
                            break
                        elif board[x][y] == player:             # 내 돌이라면 이전 좌표까지만 저장
                            for c, h in change:
                                board[c][h] = player
                            break

    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1
    print(f"#{tc}", black, white)



























#
# for tc in range(1, T+1) :
#     pass
#     N, M = map(int, input().split())
#     # N 보드의 길이
#     # M 돌을 두는 횟수
#
#     matrix = [[0]*N for _ in range(N)] # 바둑판 생성
#     matrix[N//2-1][N//2] = 1    # 검은 돌 초기 세팅
#     matrix[N//2][N//2-1] = 1    # 검은 돌 초기 세팅
#     matrix[N//2-1][N//2-1] = 2  # 흰 돌 초기 세팅
#     matrix[N//2][N//2] = 2      # 흰 돌 초기 세팅
#
#
#     def oselo(x, y, player) : # x, y : 돌을 두는 기준 좌표, player : 흑돌과 백돌의 구분이 1, 2로 들어옴
#     # 게임 규칙
#     # 상대 돌을 낄 수 있는 곳에만 돌을 들 수 있고 그 돌을 내돌로 만들 수 있음
#
#     # 놓는 위치는 xy로 정해져 있으니
#
#     # 상하좌우대각선 방향에 +1칸에 상대돌이 있는지, 델타 탐색해야
#         my_dxy = [[-2, 0], [2, 0], [0, -2], [0, 2], [2, 2], [-2, -2], [-2, 2], [2, -2]] # 내 돌을 건너 탐색 좌표
#
#         # for i in range(N) :
#         #     for j in range(N) :
#
#         put_rock = matrix[x][y] # 돌을 놓는 곳
#
#         for q, w in my_dxy : # 건너뛴 자리의 내 돌을 찾자
#             qx = x + q
#             wy = y + w
#
#             if matrix[qx][wy] and matrix[qx][wy] == player # 내 돌이 맞다면
#
#     # 그 방향의 뒤에 내 돌이 있는지를 확인해야 함
#
#     # 위 조건에 만족한다면, 돌을 두고 상대돌 자리를 BW으로 교체
#
#
#
#
#
#     for play in range(M) : # 돌을 두는 횟수
#         x, y, BW = map(int, input().split())
#









