import sys
sys.stdin = open("GNS_test_input.txt", "r")

"""
str으로 숫자를 표기함
이 표기들을 작은 수부터 차례로 정렬해야 함 
"""
T = int(input())
for tc in range(1, T+1):
    order = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]  # 목록을 저장
    test_num, n = input().split()                                                   # 갯수 불러옴
    n = int(n)                                                                      # 정수로 바꿔줌
    mix_nums = input().split()                                                      # 섞어진 리스트 받아옴

    count = {key: 0 for key in order}                                               # 문자 목록을 키로 갯수를 값으로 넣자
    print(count)
    for num in mix_nums:                                                            # 섞어진 수를 돌리며
        count[num] += 1                                                             # 갯수를 세며 밸류 카운트

    result = []                                                                     # 출력할 거
    for key in order:                                                               # 목록을 돌면서
        result += [key] * count[key]                                                # 키에 해당하는 값을 곱해서 넣어준다

    print(test_num)
    print(" ".join(result))
