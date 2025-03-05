import sys
sys.stdin = open("input.txt", "r")

"""
변의 길이가 1인 정사각형 n개를 가지고 있다
이 정사각형을 이용해서 만들 수 있는 직사각형의 개수는 총 몇 개일까?

입력 : N 정사각형 갯수

어떻게 풀까?

한 줄짜리 직사각형을 만들 수 있고
그 다음은 2줄짜리 직사각형을 만들 수 있고
N줄짜리 직사각형까지 만들 수 있음

정사각형의 갯수만큼 for 문을 돌린다

"""

# N = int(input())
# square_list = []
#
# for row in range(1, N+1):
#     for col in range(1, N//2):
#         if row * col <= N:
#             if col > row:
#                 plus = [row, col]
#                 square_list.append(tuple(plus))
#             else:
#                 plus = [col, row]
#                 square_list.append(tuple(plus))
#
# result = set(square_list)
# print(len(result))

################################################

N = int(input())

count = 0
for a in range(1, N+1):
    for b in range(a, N+1):  # b는 a 이상
        if a * b <= N:
            count += 1
        else:
            # a * b가 N을 초과하면, b가 더 커질수록 계속 초과하므로
            # 이중 반복문에서 break로 빠져나와도 됨
            break

print(count)
