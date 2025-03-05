import sys
sys.stdin = open("input.txt", "r")

"""
개의 행동 파악하기
1번 개는 A분 동안 공격적, B분 동안 조용히 쉼
2번 개는 C분 동안 공격적, D분 동안 조용히 쉼
두 개는 이 행동을 서로 반복함

각 세명의 사람이 도착하는 시간 P, M, N 이라면 몇마리의 개에게 공격 받는지 알아보자
하루의 시작 시간은 0
"""

T = int(input())
for tc in range(1, T + 1):
    A, B, C, D = map(int, input().split())
    P, M, N = map(int, input().split())

    p_min, m_min, n_min = P * 60, M * 60, N * 60
    p_bite, m_bite, n_bite = 0, 0, 0
    bk = 0

    day_time = 0
    dog_one, dog_two = [0, 1], [0, 1]    # 화나면 1 아니면 0

    while max(p_min, m_min, n_min) > 0:
        if p_min == 0:
            p_bite = dog_one[1] + dog_two[1]
        if m_min == 0:
            m_bite = dog_one[1] + dog_two[1]
        if n_min == 0:
            n_bite = dog_one[1] + dog_two[1]

        p_min -= 1
        m_min -= 1
        n_min -= 1
        dog_one[0] += 1
        dog_two[0] += 1


        if dog_one[0] == A:
            dog_one[1] = 1 - dog_one[1]
        elif dog_one[0] == A+B:
            dog_one[1] = 1 - dog_one[1]
            dog_one[0] = 0

        if dog_two[0] == C:
            dog_two[1] = 1 - dog_two[1]
        elif dog_two[0] == C+D:
            dog_two[1] = 1 - dog_two[1]
            dog_two[0] = 0

    print(p_bite)
    print(m_bite)
    print(n_bite)










# T = int(input())
# for tc in range(1, T + 1):
#     A, B, C, D = map(int, input().split())
#     P, M, N = map(int, input().split())
#     p_bite = 0
#     m_bite = 0
#     n_bite = 0
#     bk = 0
#
#     day_time = 0
#     dog_one = [0, 1]    # 화나면 1 아니면 0
#     dog_two = [0, 1]
#
#     while True:
#         day_time += 1
#         dog_one[0] += 1
#         dog_two[0] += 1
#
#         if dog_one[0] == A:
#             dog_one[1] = 1 - dog_one[1]
#         elif dog_one[0] == A+B:
#             dog_one[1] = 1 - dog_one[1]
#             dog_one[0] = 0
#
#         if dog_two[0] == C:
#             dog_two[1] = 1 - dog_two[1]
#         elif dog_two[0] == C+D:
#             dog_two[1] = 1 - dog_two[1]
#             dog_two[0] = 0
#
#         if day_time / 60 == P:
#             p_bite += dog_one[1] + dog_two[1]
#             bk += 1
#         if day_time / 60 == M:
#             p_bite += dog_one[1] + dog_two[1]
#             bk += 1
#         if day_time / 60 == N:
#             p_bite += dog_one[1] + dog_two[1]
#             bk += 1
#         if bk == 3:
#             break
#
#     print(p_bite)
#     print(m_bite)
#     print(n_bite)







