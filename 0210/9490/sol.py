import sys
sys.stdin = open("input1.txt", "r")

#############################################

T = int(input())    # test_case 개수를 받아옴

for tc in range(1, T+1) :
    pass
    n, m = map(int, input().split()) # 행과 열의 줄 수를 받아옴
    matrix = [list(map(int, input().split())) for _ in range(n)] # 행의 줄 수만큼 반복하여 2중 리스트로 저장
    max_value = 0 # 구해야 할 최대값 세팅

    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 탐색 위치별 순서를 정의

    for i in range(n) : # 행을 돌리자
        for j in range(m) : # 열을 돌리자
            sum_val = matrix[i][j] # 풍선의 기준점

            for dx, dy in dxy : # 탐색 위치를 꺼내와서 돌리자
                for dist in range(1, matrix[i][j] + 1) : # 풍선 기준점의 값만큼 반복문
                    ni = i + dx * dist # 탐색하는 위치는 기준점 + 기준점의 값을 설정
                    nj = j + dy * dist

                    if 0 <= ni < n and 0 <= nj < m : # out of range 방지
                        sum_val += matrix[ni][nj] # 기준점 주변의 풍선 누적합을 구함
            max_value = max(sum_val, max_value) # 세팅한 최대값과 누접합을 계속 비교하여 더 큰 값으로 업데이트

    print(f"#{tc} {max_value}")
