import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N-K):
            if not 0 in puzzle[i][j:j+K]:
                cnt += 1

    for i in range(N-K):
        for j in range(N):
            if not 0 in puzzle[i:i+K][j]:
                cnt += 1

    print(cnt)

