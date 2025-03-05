"""
양을 셀 것임

N의 배수인 양만 셀 것

N을 셀 떄
N의 자리수의 각 숫자들이 0~9까지의 수들로 이루어지는 경우 끝남

입력
T와
N 배수가 될 수
출력
N의 배수를 돌렸을 때 0~9까지 나오면 마지막 수를 출력

어떻게 풀까?
1. N을 받고, 비교할 0~9까지의 리스트를 만들고, N을 순회하는 횟수를 세어줄 cnt를 만들자
2. N을 문자열로 만들고 순회를 하며 0~9가 존재한다면 체크리스트에 그 숫자를 담자
3. 담았다면 N을 다시 숫자로 만들고 카운팅을 곱하여 다시 문자열을 만드는 것을 반복한다
4. 체크리스트에 0~9까지 모두 있다면 중단 후 N을 숫자로 만든 후 출력한다
"""
import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    N = int(input())                                # 일단 정수로 받고
    now_N = N
    cnt = 1
    check = []
    break_point = 0

    while break_point == 0:
        now_N = str(N * cnt)                        # 정수의 배수를 스트링으로 바꿔 쪼갠다
        for num in now_N:                           # 그리고 그 쪼갠 리스트를 돌리고
            if num in nums and num not in check:    # 1~9까지 해당하고 그게 추가가 안됐다면
                check.append(num)                   # 추가하고
                check.sort()                        # 정렬한다

        cnt += 1                                    # 배수 카운팅하고

        if check == nums:                           # 1~9를 다 찾았다면 종료
            break_point = 1
            break

    print(f"#{tc}", now_N)
