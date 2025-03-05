import sys
sys.stdin = open("4831_input.txt", "r")

"""
전기버스는 한번 충전으로 이동하는 정류장 수가 정해짐
정류장 일부에 충전기 설치

종점 : N
충전 1회에 이동거리 : K
충전기가 설치된 정류장 개수 : M
충전기가 설치된 정류장 목록 : charge_stop

충전기 설치가 잘못되어 종점에 못 가면 0출력
잘 가면 충전 횟수 출력

"""
T = int(input())    # test_case 개수를 받아옴
for tc in range(1, T+1) :
    K, N, M = map(int, input().split())
    charge_points = list(map(int, input().split()))
    now_stop = 0
    cant_go = 0
    result = 0

    while now_stop < N and cant_go == 0:
        for go in range(K, 0, -1):
            if (now_stop + go) in charge_points:
                now_stop += go
                result += 1
                break

            elif (now_stop + go) == N:
                now_stop += go
                break

            elif go == 1:
                cant_go = 1
                break

    if cant_go == 1:
        print(f"#{tc}", 0)
    else:
        print(f"#{tc}", result)


# T = int(input()) # test case 개수를 받아오는 코드
# for tc in range(1, T+1):
#     K, N, M = map(int, input().split())
#     charge_station_list = list(map(int, input().split()))
#     cnt = 0                                                 # 충전 횟수
#     this_stop = 0                                           # 현재 정류장
#     error_sig = 0                                           # 갈 수 없을 때를 구분하고 브레이킹으로 활용
#
#     while this_stop < N and error_sig == 0:                 # 현재 정류장이 N보다 클 수 없음,
#         for i in range(K, 0, -1):                           # 가능한 거리 부터 1까지 순회
#                                                             # 최대 운용 가능 정류장부터 현재 정류장까지 역순으로 충전 정류장이 있는지 탐색
#             if ((this_stop + i) in charge_station_list):    # 충전 정류장 목록에 현재 정류장이 해당된다면
#                 cnt += 1                                    # 있으면 카운트 값 1증가, 및 그 정류장으로 현재정류장 갱신
#                 this_stop += i
#                 break
#             elif (this_stop + i) == N:                      #최대 정류장 도달 시 종료
#                 this_stop += i
#                 break
#
#             if i == 1:                                      # 최대 운용 가능 정류장부터 현재 정류장까지 탐색했으나 충전 정류장이 없다면
#                 error_sig = 1                               # while 반복 종료
#                 break
#
#     if error_sig == 1:                                       # 설치가 잘못못어 있므면 0출력 아니면 충전 카운트 값 출력
#         print(f'#{tc} {0}')
#     else:
#         print(f'#{tc} {cnt}')


#########
"""
전기버스 충전을 몇회해야 하는가?
정류장 수  N
충전 1회당 이동가능 정류장 K
충전기가 설치된 정류장 수 M
충전기가 설치된 정류장들 charge_point


"""



