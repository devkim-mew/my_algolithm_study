import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())    # test_case 개수를 받아옴

for tc in range(1, T+1) :
    N = int(input())                                    # 수를 받아오고
    result = []                                         # 결과값 세팅
    input_nums = [input().strip() for _ in range(N)]    # 10개로 쪼개진 이진수를 모두 받아온다
    nums = []                                           # 10개로 쪼개진 수를 하나의 리스트로 합쳐주기 위한 리스트
    seven_nums = []
    for i in range(N):
        for j in input_nums[i]:                         # 10개로 묶인 이진수 리스트를 하나씩 풀어서 nums에 넣는다
            nums.append(j)

    imsi = []
    for g in nums:                                      # 전부 쪼갠 수를 7개씩 묶어서 다시 저장
        if len(imsi) == 7:
            seven_nums.append(imsi)
            imsi = []
            imsi.append(g)
        else:
            imsi.append(g)
    seven_nums.append(imsi)                             # 남은 거 짬처리

    for j in range(len(seven_nums)):                    # 1이라면 해당 인덱스만큼 제곱하여 수를 더하고 0이라면 패스
        sibzinsu = 0
        zegob = 6
        for k in seven_nums[j]:
            if int(k) == 1:
                sibzinsu += 2**zegob
                zegob -= 1
            else:
                zegob -= 1
        result.append(sibzinsu)

    print(f"#{tc}", *result)



