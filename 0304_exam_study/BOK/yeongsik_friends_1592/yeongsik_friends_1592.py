import sys
sys.stdin = open("input.txt", "r")


"""
영식이와 친구들이 원형으로모여서 시계방향으로 1 ~ N 까지 적힌 자리에 앉는다
이 상태에서 공던지기를 하는데
1번 자리의 사람이 먼저 공을 가지고 다른 사람에게 던진다 받은 사람은 또 다른 사람에게 던진다
이를 반복하다 한 사람이 공을 M번 받으면 게임 끝(당장 받는 공까지 포함)

공을 M번보다 적게 받은 사람이 공을 받은 횟수가 
홀수번이면 자기의 현재 위치에서 시계 방향으로 L번째 있는 사람에게
짝수번이면 자기 위치에서 반시계 방향으로 L번째 있는 사람에게 공을 던진다

공을 총 몇 번 던졌는지 구하자 cnt
N 사람 수
M 게임 끝나는 공 받은 수
L 공을 던지는 방향 수


어떻게 풀까?
그룹 리스트를 딕셔너리로 만들고 
1번 키에서 공을 던진다(홀수) 시계방향 => 키 값은 +L 로 변경
만약 벨류값이 짝수라면 -L로 변경 하지만 음수가 된다면 +N 해준다
그러다 밸류가 M이 되면 멈춘다
"""


T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())

    friends = {friend: 0 for friend in range(N)}

    friends[0] = 1              # 처음 공을 줌
    total_cnt = 0               # 출력할 값
    last_friend = 0             # 직전 공 받은 친구의 인덱스
    while True:
        if friends[last_friend] == M:       # 밸류 중 M이 되는 게 있으면 순회탈출
            break

        if friends[last_friend] % 2 == 0:
            if last_friend + L < N:
                friends[last_friend + L] += 1
                last_friend = last_friend + L
                total_cnt += 1
            else:
                friends[last_friend + L - N] += 1
                last_friend = last_friend + L - N
                total_cnt += 1
        else:
            if last_friend - L >= 0:
                friends[last_friend - L] += 1
                last_friend = last_friend - L
                total_cnt += 1
            else:
                friends[last_friend - L + N] += 1
                last_friend = last_friend - L + N
                total_cnt += 1

    print(total_cnt)


