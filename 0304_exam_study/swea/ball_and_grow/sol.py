"""
1차원 리스트에서
바닥 : ...
공 : ()
잡초 : |

초원에서 잡초가 자라 공이 가려짐
이 때 공의 최소 갯수를 출력하자

입력
T 테스트 케이스
||||||
(|..|)
.|.(|...||)|...()..

어떻게 풀까?
1. 먼저 리스트로 받고
2. 스택의 방식대로 해결해보자
    2-1. 순회를 돌며 (를 마주치면 다른 리스트에 넣고
    2-2. )를 마주치면 마저 리스트에 넣고 순회를 종료한다
    2-3. (와 ) 사이에 .이 있다면 이것도 리스트에 넣는다
3. 리스트에 들어간 값을 2로 나누어 결과로 출력한다
"""

import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    ground = input().strip()                        # 풀뗴기 받아옴
    balls = []                                      # 공을 저장할 스택
    result = 0                                      #

    for i in range(len(ground)):                    # 풀을 돌면서
        if ground[i] == "(":                        # 여는 괄호를 마주치면
            balls.append(ground[i])                 # 일단 추가

        if ground[i-1] != "." and ground[i] == "|":  # 직전이 .이 아니고 |이라면
            if len(balls) % 2 == 1:                  # 그리고 공이 반쪽이라면 추가
                balls.append(ground[i])

        if ground[i] == ")":                         # 닫는 거 만나면
            if ground[i-1] == "|":                   # 직전이 작대기라면 작대기 먼저 추가
                balls.append(ground[i-1])
            balls.append(ground[i])                  # 그리고 다는 거도 추가 후
            result += len(balls) // 2                # 공 개수를 결과에 추가
            balls = []                               # 공 비움

        if balls and len(balls) % 2 == 0:            # 공이 있고 짝수라면
            result += len(balls) // 2                # 결과에 추가하며 한 번씩 비워줌
            balls = []

    print(f"#{tc}", result)



