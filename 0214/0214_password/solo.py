import sys
sys.stdin = open("input.txt", "r")

from collections import deque
#############################################

T = 10    # test_case 개수를 받아옴

for tc in range(1, T+1) :
    pass
    N = int(input())
    put_pw = deque(map(int, input().split()))

    while put_pw[-1] > 0 :

        for i in range(1, 6) :
            put_pw[0] -= i                      # 첫번째 인덱스의 값을 -i(1~5) 후 맨 뒤로 보낸다
            put_pw.append(put_pw.popleft())     # 맨 뒤로 보낸다

            if put_pw[-1] <= 0 :                # 만약, 끝자리가 0 이하가 되면
                put_pw[-1] = 0                  # 0이든 아니든 0으로 바꿔버리고
                break                           # 더이상의 -i를 하지 않는다


    print(f"#{tc}", *put_pw)                    # deque 언패킹하여 출력


