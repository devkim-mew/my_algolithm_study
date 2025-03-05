import sys
sys.stdin = open("input.txt", "r")

#############################################

T = 10    # test_case 개수를 받아옴

for tc in range(1, T+1) :
    pass
    test_num = int(input()) # 테스트 케이스 넘버를 받아옴
    matrix = []
    for _ in range(100) :
        matrix.append(list(map(int, input().split()))) # 한줄씩 리스트 받아오는 것을 100번 반복하여



    plus_n = 0 # 대각선 합
    plus_m = 0 # 반대 대각선 합
    plus_i_max = 0 # 행의 최대 합
    plus_j_max = 0 # 열의 최대 합

    for i in range(100) :
        plus_i = 0
        plus_j = 0
        plus_n += matrix[i][i]  # 대각선 순회하며 합하기
        plus_m += matrix[i][99 - i]  # 반대 대각선 순회하며 합하기
        for j in range(100) :
            plus_i += matrix[i][j] # 행을 순회하며 합하기
            plus_j += matrix[j][i] # 열을 순회하며 합하기
        if plus_i > plus_i_max :
            plus_i_max = plus_i # 행의 합 중 가장 큰 수
        if plus_j > plus_j_max :
            plus_j_max = plus_j # 열의 합 중 가장 큰 수

    sum_max = max(plus_i_max, plus_j_max, plus_m, plus_n)

    print(f"#{tc} {sum_max}")