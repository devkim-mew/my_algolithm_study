import sys
sys.stdin = open("input.txt", "r")

"""
주어진 수를 나머지가 생길 때까지 11로 나누고

나머지가 생기면 나눈 횟수와 몫을 저장하고

그 몫을 다음 나머지가 생길 때까지 7로 나누고

5로 나누고 3으로 나누고 2로 나누기를 반복한다
"""

from collections import deque

T = int(input())

for tc in range(1, T+1) :
    num = int(input())                                # 나눌 수
    nums = [(11, 0), (7, 0), (5, 0), (3, 0), (2, 0)]  # 나눌 수와 나눈 횟수를 튜플로 저장
    result = deque()                                  # 결과값에 반대로 넣기 위해 디큐 사용

    for i in range(len(nums)):
        cnt = 0
        while True:
            if num % nums[i][0] == 0:             # 첫 수로 잘 나누어진다면
                num = num / nums[i][0]            # 나누어서 값을 업데이트하고
                cnt += 1                          # 나눈 횟수를 추가한다
            elif num % nums[i][0] > 0:            # 나누어 지지 않으면 다음 수로 나눈다
                break
        nums[i] = (nums[i][0], nums[i][1] + cnt)  # 나눌 수 있는 최대 횟수가 끝나면 나눈 횟수를 튜플에 업데이트 해준다
        result.appendleft(nums[i][1])             # 그리고 출력값에 순서를 바꿔 넣어준다

    print(f"#{tc}", *result)



    # for i in nums:
    #     while True:
    #         if num % i == 0:        # 11로 잘 나누어지면
    #             num = num / i       # 11로 나누어서 몫을 업데이트하고
    #             num_cnt[i] += 1     #
    #             print(nums[i])
    #             print(num)
    #         else:
    #             break

