import sys
sys.stdin = open("input.txt", "r")

T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    result = []
    for i in range(1, N+1):
        if ('3' in str(i//10) or '6' in str(i//10) or '9' in str(i//10)) and ('3' in str(i%10) or '6' in str(i%10) or '9' in str(i%10)):
            result.append('--')
        elif '3' in str(i) or '6' in str(i) or '9' in str(i):
            result.append('-')
        else:
            result.append(i)
    print(*result)



    # for i in range(1, N+1):
    #     if len(str(i)) == 2 and (i//10) % 3 == 0 and (i % 10) % 3 == 0:
    #         result.append('--')
    #     elif len(str(i)) == 2 and i//10 % 3 == 0:
    #         result.append('-')
    #     elif i % 3 == 0:
    #         result.append('-')
    #     else:
    #         result.append(i)
    # print(*result)

