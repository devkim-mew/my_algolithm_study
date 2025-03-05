import sys
sys.stdin = open("s_input.txt", "r")

#############################################
# 문제 이해
# 버스는 1~5000개가 있음
# 버스 노선은 N개인데 i번째 버스의 노선은 Ai이상이고 Bi 이하인 모든 정류장만을 다니는 버스 노선이다 Ai <= i <= Bi
# P개의 버스 정류장은 각 정류장마다 노선이 몇개인지 구하자
# 노선에 해당하는 정류장을 구하자

# N = 2 , 버스노선이 2개
# 1 <= 1노선 <= 3  /  1 ~ 3
# 2 <= 2노선 <= 5  /  2 ~ 5
# P는 정류장 개수
# c1 = 1
# c2 = 2
# c3 = 3
# c4 = 4
# c5 = 5

# 구할 것 : P개의 정류장마다 다니는 버스노선 수를 각각 구해야


T = int(input())  # test_case 개수를 받아옴

for tc in range(1, T + 1):
    N = int(input())                                                # 노선 수
    bus_line = [list(map(int, input().split())) for _ in range(N)]  # 버스 노선
    print(bus_line)
    P = int(input())                                                # 버스 정류장 수
    C = [int(input()) for _ in range(P)]                            # 기준이 되는 버스 정류장 세팅
    total = [0] * P                                                 # 출력할 값, 지나치는 버스 정류장들

    for line1, line2 in bus_line :                                  # 버스 노선들이 정류장과 일치한 지 확인해보자
        for bus_stop in range(P):                                   # 지나치는 버스정류장들을 순회하면서
            if C[bus_stop] in range(line1, line2 + 1):              # range에 두개를 적는다? 이해가 안되는 부분
                total[bus_stop] += 1

    print(f"#{tc}", *total)

