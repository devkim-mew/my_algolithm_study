import sys
sys.stdin = open("5099_input.txt", "r")

from collections import deque

#############################################

T = int(input())    # test_case 개수를 받아옴

for tc in range(1, T+1) :
    pass

# 화덕 N개  피자 M개
# 치즈량


# 화덕에 피자를 N개 넣고 화덕.append(피자[0])
#
# 화덕을 한바퀴 돌면서 치즈가 반으로 줄음 //2

# 치즈가 0이 되면 피자를 빼고 다음 피자를 넣음
# 가장 마지막 피자를 출력 if len(화덕) == 1 : print(화덕[0])


    N, M = map(int, input().split())
    pizza = deque(tuple(map(int, input().split())))
    fire_fit = deque()


    for _ in range(N) :
        fire_fit.append(pizza.popleft())

    # print(len(fire_fit))

    while len(fire_fit) > 1 :

        fire_fit.append(fire_fit.popleft())
        fire_fit[-1] = fire_fit[-1] // 2

        if fire_fit[-1] <= 0 :
            fire_fit.popleft()

            if len(pizza) > 0 :
                fire_fit.append(pizza.popleft())


        print(fire_fit)
