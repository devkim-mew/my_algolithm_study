import sys
sys.stdin = open("4843_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()                             # 정렬먼저 해주고
    result = []
    for i in range(5):                      # 10개까지만이니 5번만 순회
        result.append(nums[-i-1])           # 가장 뒷자리가 젤 크니 먼저
        result.append(nums[i])              # 그 다음 가장 앞자리
    print(f'#{test_case}', *result)