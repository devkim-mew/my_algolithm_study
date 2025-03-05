import sys
input = sys.stdin.readline

# 테스트 케이스는 총 10개가 주어진다.
T = 10
for tc in range(1, T + 1):
    # 첫 줄에 테이블의 한 변의 길이가 주어지는데, 문제 조건에선 항상 100이다.
    n = int(input().strip())

    # 100x100 테이블 입력받기
    # 각 셀의 값은 0, 1, 2로 주어지며,
    # 1은 N극 성질(보통 위쪽에서 아래쪽으로 움직임), 2는 S극 성질(보통 아래쪽에서 위쪽으로 움직임)을 의미한다.
    table = [list(map(int, input().split())) for _ in range(n)]

    deadlock_count = 0  # 교착 상태의 총 개수를 저장할 변수

    # 각 열에 대해 독립적으로 교착 상태 개수를 계산
    for j in range(n):
        # flag는 현재 열에서 아직 충돌하지 않은 N극(1)이 있는지를 나타낸다.
        flag = False
        for i in range(n):
            # N극(1)을 만나면 flag를 켠다.
            if table[i][j] == 1:
                flag = True
            # S극(2)을 만났을 때, 이전에 N극이 있었다면 (flag가 켜져 있다면)
            # 그 즉시 교착 상태가 발생한 것으로 카운트하고 flag를 초기화한다.
            elif table[i][j] == 2:
                if flag:
                    deadlock_count += 1
                    flag = False

    # 각 테스트 케이스 결과를 "#테스트번호 결과" 형식으로 출력
    sys.stdout.write(f"#{tc} {deadlock_count}\n")

