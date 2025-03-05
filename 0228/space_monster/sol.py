"""
1차원 구현 매운맛 : 신뢰, 당근포장
탐욕문제가 나올 수도 있으니 조심


상하좌우로 괴물이 광선을 발사하며 상하좌우로 계속 뻗어나감
풍선팡 보너스와 비슷함
근데 벽을 부딫히면 광선이 없어짐
0은 칸
1은 벽
2는 괴물

안전한 칸 남은 0을 구하자

로직
1. 외계인을 찾자
2. 외계인의 빔이 스친곳을 체크
    빔은 끝까지 발사
    벽에 막히기도 함
3. 빔이 스치지 않은 곳을 확인 후 개수 세기
"""

import sys
sys.stdin = open("sample_in.txt", "r")

def check_beam(alien, grid):
    drc = [(-1,0), (1,0), (0,-1), (0,1)]        # 외계인 빔 스친 곳 탐색
    for x, y in drc:                            # 탐색하는데 델타값을 곱해가며 탐색을 늘려감
        for i in range(1, N):
            nr = alien[0] + x * i
            nc = alien[1] + y * i

            if 0 <= nr < N and 0 <= nc < N:     # 빔이 스치는 곳
                if grid[nr][nc] == 1:           # 만약 벽을 마주치면 중단
                    break                       # 여기는 return이 오면 안됨
                grid[nr][nc] += 28              # 빔 스친 곳 표시
    return grid                                 # 델타 탐색을 모두 마치고 수정된 공간 반환

def get_safe_area(grid):
    cnt = 0                                     # 안전공간 수를 세어야 함
    for row in range(N):
        for col in range(N):
            if grid[row][col] == 0:             # 0이라면 안전하니 체크
                cnt += 1
    return cnt                                  # 카운트 반환

T = int(input())
for tc in range(1, T+1):
    N = int(input())                                                # 먼저 사각형 길이를 받고
    grid = [list(map(int, input().split())) for _ in range(N)]      # 공간 정보 받아옴

    alien = None                                                    # 일단 외계인 위치는 킵
    for row in range(N):                                            # 공간을 돌면서
        for col in range(N):
            if grid[row][col] == 2:                                 # 외계인을 찾고
                alien = (row, col)

    # 외계인의 빔이 스친 곳 체크
    grid = check_beam(alien, grid)

    # 스치지 않은 갯수세기 함수
    result = get_safe_area(grid)

    print(f"#{tc}", result)
