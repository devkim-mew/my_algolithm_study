import sys
sys.stdin = open("input.txt", "r")

#############################################

T = 10    # test_case 개수를 받아옴

for tc in range(1, T+1) :
    pass
    N = int(input())
    arr = [list(input().split()) for _ in range(8)]

    # 어떻게 풀어야 할까?
    # i행을 돌면서 회문을 찾는다
    # 회문을 찾는 방법은 첫번째와 두번째가 동일한 경우, 첫번째와 마지막이 동일하고 가운데가 하나인 경우,

    # i부터 도는 것과 -i로 도는 것이 일치해야


    # 홀수인 경우


    def palindrome(A, B, C) :






    for i in arr :
        for j in i :
            if i ==