import sys
sys.stdin = open("input.txt", "r")

#############################################

T = 10   # test_case 개수를 받아옴

for tc in range(1, T+1) :
    pass

    test_case = int(input()) # 테스트 케이스 넘버를 받아옴
    N, M = map(int, input().split()) # 정수와 제곱근 수를 각각 받아옴

    def mixmix(N, M) : # 제곱근 재귀함수 만들기
        if M == 0 : # 제곱을 완료하였을 때 재귀를 빠져나가기 위한 세팅
            return 1
        else:
            return N * mixmix(N, M-1) # M번 만큼 N을 연속하여 곱하는 재귀

    print(f"#{test_case} {mixmix(N, M)}")