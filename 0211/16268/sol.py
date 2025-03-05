import sys
sys.stdin = open("input1.txt", "r")

#############################################

T = int(input())    # test_case 개수를 받아옴

for tc in range(1, T+1) :
    pass
    N, M = map(int, input().split()) # 행과 열의 줄 수를 가져옴
    matrix = [list(map(int, input().split())) for _ in range(N)] # 행의 수만큼 반복하여 열을 돌리고 매트릭스를 만듦
    max_value = 0 # 최종 구할 최대값 세팅

    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 탐색 좌표 및 순서

    for i in range(N) : # 행 돌림
        for j in range(M) : # 열 돌림
            sum_bloon = matrix[i][j] # 풍선 기준점

            for dx, dy in dxy : # 좌표 돌리기
                ni = i + dx # 기준점 + 탐색값
                nj = j + dy

                if 0 <= ni < N and 0 <= nj < M : # 아웃방지
                    sum_bloon += matrix[ni][nj] # 기준점 값에 탐색값들 모두 더함

            max_value = max(max_value, sum_bloon) # 최대값을 구하기 위해 더 큰 값 생기면 업데이트

    print(f"#{tc} {max_value}")
