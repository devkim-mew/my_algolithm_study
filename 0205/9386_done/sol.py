import sys
sys.stdin = open("input1.txt", "r")

#############################################

T = int(input())    # test_case 개수를 받아옴

for tc in range(1, T+1) :
    N = int(input())
    arr = list(map(int, input()))

    # N으로 수열의 길이를 받아오고
    # arr으로 수열을 리스트로 받아옴
    # arr 리스트에서 연속된 1의 숫자를 뽑아야 하는데
    # arr[i]가 1인경우 count 리스트의 0번째에 + 1을 반복
    # 만약 arr[i]가 1이 아닌 경우 count 리스트 +1로 넘어가서 arr[i]가 1인경우 + 1을 반복
    # count 리스트에서 제일 큰 수를 출력

    count = [0] * N
    ct = 0

    for i in range(len(arr)) :
        if arr[i] == 1 :
            count[ct] += 1
        else :
            ct += 1

    result = count[0]

    for j in range(len(count)) :
        if result < count[j] :
            result = count[j]


    print(f"#{tc} {result}")


