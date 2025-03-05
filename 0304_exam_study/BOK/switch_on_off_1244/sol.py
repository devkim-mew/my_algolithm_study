import sys
sys.stdin = open("input.txt", "r")

"""
N개의 스위치가 0, 1로 무작위로 있음
학생이 스위치를 바꿀 수 있는데
남자 1은 받은 수의 배수를 바꾸고
여자 2는 받은 수를 중심으로 좌우가 같은 가장 넓은 구간을 모두 바꾼다
바뀐 값을 출력해보자

어떻게 풀까?
먼저 사람 수 만큼 순회를 돌리고 for i in range(people_num)
성별에 따라 if people[0] == 1
주어진 스위치 번호 people[1]-1를 switch_list에서 찾는다

남학생 탐색
스위치 번호로 나누어 떨어지는 인덱스는 모두 바꾼다

여학생 탐색
스위치 번호 자리의 양 옆이 같은지를 틀릴때까지 비교한다 switch_list[num-i] == switch_list[num+i] while
틀리는 구간이 나오면 직전 구간을 전부 바꿔준다

"""

N = int(input())                                                            # 스위치 수
switch_list = list(map(int, input().split()))                               # 스위치의 리스트
people_num = int(input())                                                   # 학생 수
people = [tuple(map(int, input().split())) for _ in range(people_num)]      # 학생 정보

for p in people:                                                            # 학생들을 돌린다
    switch_point = p[1] - 1                                                 # 학생이 받은 수를 인덱스 고려해서 -1
    if p[0] == 1:                                                           # 남자면
        for i in range(switch_point, N, switch_point + 1):                  # 받은 수부터 끝까지 받은 수만큼 건너뛰며 스위칭
            switch_list[i] = 1 - switch_list[i]

    elif p[0] == 2:                                                         # 여자면
        j = 1                                                               # 양옆 이동값
        while switch_point - j >= 0 and switch_point + j < N:               # 인덱스를 벗어나면 순회탈출
            if switch_list[switch_point - j] != switch_list[switch_point + j]:      # 양옆의 값이 다르면 탈출
                break
            j += 1                                                          # 양옆을 늘려가며 탐색

        for k in range(switch_point - (j - 1), switch_point + (j - 1) + 1): # 양옆이 같은 값까지의 모든 구간을 바꿈
            switch_list[k] = 1 - switch_list[k]

for l in range(0, N, 20):
    for i in switch_list[l:l+20]:
        print(i, end = " ")
    print()
































# N = int(input())
# switch_list = list(map(int, input().split()))
# people_num = int(input())
# people = [tuple(map(int, input().split())) for _ in range(people_num)]
#
# for p in people:
#     switch_point = p[1]
#     if p[0] == 1:
#         for i in range(N):
#             if (i+1) % switch_point == 0:
#                 if switch_list[i] == 1:
#                     switch_list[i] = 0
#                 else:
#                     switch_list[i] = 1
#
#     elif p[0] == 2:
#         length = min(switch_point, len(switch_list)-switch_point+1)
#         for j in range(1, length):
#             minu = switch_point - 1 - j
#             plus = switch_point - 1 + j
#             if minu == 0 or plus+1 == len(switch_list):
#                 for k in range(minu, plus+1):
#                     if switch_list[k] == 1:
#                         switch_list[k] = 0
#                     else:
#                         switch_list[k] = 1
#             if switch_list[minu] != switch_list[plus]:
#                 for k in range(minu+1, plus):
#                     if switch_list[k] == 1:
#                         switch_list[k] = 0
#                     else:
#                         switch_list[k] = 1
#
# print(*switch_list)


