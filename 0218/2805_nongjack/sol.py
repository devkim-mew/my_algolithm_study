"""
N * N 크기의 농장이 있음

수확은 마름모 형태로만 가능함

N은 항상 홀수

수학물들을 구해보자

"""


import sys
sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    center = N//2
    hab = 0

    for row in range(N-1):
        if row <= center:
            for l in range(center-row, center+row+1):
                hab += farm[row][l]
        else:
            for j in range(center-1, -1, -1):
                for m in range(center-j, center+j+1):
                    hab += farm[row][m]

    print(f"#{tc}", hab)
