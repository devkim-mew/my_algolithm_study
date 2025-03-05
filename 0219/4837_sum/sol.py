import sys
sys.stdin = open("4837_input.txt", "r")

"""
1부터 12까지 무작위 집합  A

목표
집합 A의 부분 집합 중 N개의 원소를 갖고 있고
원소의 합이 K인 부분집합의 개수를 출력

어떻게 구해야 할까?

A에서 N개를 꺼내서 더했을 때 K가 나와야 한다
"""


def sum_subset(idx, num_sum):
    global result
    # 인덱스가 arr의 길이(12)만큼 돌았으면 (모든 요소를 다 확인했으면)
    if idx == len(arr):
        # 부분집합의 원소 개수가 n개이고, 그 합이 k이면 결과 카운트 증가
        if len(selected) == n and num_sum == k:
            result += 1
        return

    # idx에 해당하는 값을 선택한다 (부분집합에 포함)
    selected.append(arr[idx])
    sum_subset(idx + 1, num_sum + arr[idx])

    # idx에 해당하는 값을 선택하지 않는다 (부분집합에 미포함)
    selected.pop()
    sum_subset(idx + 1, num_sum)


T = int(input())  # 테스트케이스 개수
for tc in range(1, T + 1):
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n, k = map(int, input().split())  # n: 부분집합 원소 개수, k: 부분집합의 합
    result = 0
    selected = []  # 선택한 원소를 담을 리스트 (부분집합 저장용)
    sum_subset(0, 0)
    print(f"#{tc} {result}")