"""
당근 크기 선별기를 이용해 수확하는 대로 당근의 크기를 기록함
이 선별기는 연속적으로 당근의 크기가 커지는 경우 그 갯수를 알려줌
당근의 크기는 수확한 순서로 주어짐 (당근이 다섯개라면 크기는 1~5까지)
이떄 연속적으로 커지는 제일 큰 수를 구해보자

어떻게 구할까?
1. N 당근의 갯수, carrots 당근의 수확 리스트
2. 순회를 돌며 당근의 값을 저장해두고 그 다음 순회하는 당근과 비교하여 큰지 작은지를 판단
3. 만약 크다면 카운팅하고 작다면 카운팅을 초기화
4. 마지막에 카운팅 출력
"""

import sys
sys.stdin = open("carrot_sample_in.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))
    eve_carrot = carrots[0]
    cnt = 1
    cnt_list = []

    for i in range(1, len(carrots)):
        if carrots[i] > eve_carrot:
            cnt += 1
            cnt_list.append(cnt)
        else:
            cnt = 1
            cnt_list.append(cnt)
        eve_carrot = carrots[i]

    result = max(cnt_list)

    print(f"#{tc}", result)