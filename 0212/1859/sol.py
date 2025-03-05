import sys
sys.stdin = open("input.txt", "r")

# 미리 가격을 알고 사재기를 한다
# 다만 개수는 제한되어있다
# 사재기의 조건 : 연속된 N일동안 물건 매매가를 예측하여 앎, 하루에 1개만 구입 가능, 판매는 얼마든지 가능

# N일 동안 1씩 모으다가 가장 비싼 날에 팔자

# 리스트에서 가장 비싼 날을 찾고 그 날의 인덱스(판매 당일은 안 사니까)를 판매 개수로 구하자

# 다시 구하자 가장 비싼 날 다음에도 차익거래가 가능한 날들이 있다
# 리스트에서 가장 비싼 날을 찾고 그 날의 인덱스(판매 당일은 안 사니까)를 구매 개수로 하고
# 지금까지 구매한 값들 모두 더하고 sum
# 가장 비싼 가격 * 일자 - 구매에 사용한 비용으로 구한다
# 그리고 리스트에서 가장 비싼 날의 인덱스 부터 가장 비싼 값을 찾는다를 모든 인덱스를 돌 때까지 반복한다




T = int(input())    # test_case 개수를 받아옴

for tc in range(1, T+1) :
    pass
    N = int(input())
    arr = list(map(int, input().split()))




    for i in range() :


    print(f"#{tc} {total}")







    T = int(input())  # test_case 개수를 받아옴

    for tc in range(1, T + 1):
        pass
        N = int(input())
        arr = list(map(int, input().split()))
        start_arr = 0
        total_buy = 0
        max_arr = []
        total = 0

        for i in range(5):
            buy = 0
            day = 0
            for j in range(start_arr, max(arr[start_arr:-1])):
                buy += arr[j]
                start_arr = j
                total_buy += buy
                day += 1
            total += max_arr[i] * day - buy

        print(f"#{tc} {total}")






