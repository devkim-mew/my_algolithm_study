def sum_subset(idx, num_sum):
    """
    부분집합의 합이 0이 되는 경우가 있는지 찾는 재귀 함수

    :param idx: 현재 탐색 중인 인덱스
    :param num_sum: 현재까지의 부분집합 원소 합
    """
    global result  # 전역 변수 사용 (부분집합의 합이 0이 되는 경우가 있으면 1로 변경)

    if idx == 10:  # 숫자 리스트의 마지막까지 탐색 완료했을 때
        if num_sum == 0:  # 부분집합의 합이 0이면
            result = 1  # 결과값을 1로 설정 (존재함)
        return  # 종료

    # 현재 숫자를 포함하는 경우
    sum_subset(idx + 1, num_sum + number[idx])

    # 현재 숫자를 포함하지 않는 경우
    sum_subset(idx + 1, num_sum)


# 테스트 케이스 개수 입력
T = int(input())

for tc in range(1, T + 1):
    number = list(map(int, input().strip().split()))  # 숫자 목록을 입력받음
    N, result = 0, 0  # N(사용되지 않음), result(부분집합의 합이 0이 되는 경우가 있으면 1)

    sum_subset(1, number[0])  # 부분집합 탐색 시작 (첫 번째 숫자를 포함한 상태로 시작)

    # 결과 출력
    print(f"#{tc} {result}")
