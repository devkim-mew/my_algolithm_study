import sys
sys.stdin = open("input.txt", "r")

#############################################
"""
매일 온도가 정수로 주어짐 arr로 받자
연속적인 며칠동안의 온도의 합이 가장 큰 값을 result
총 일수는 N
더할 온도의 일수는 K

어떻게 풀까?
리스트에서 연속되는 부분을 슬라이싱으로 인덱스를 가져오고 인덱스에 따라 값들을 더하며
크다면 result를 업데이트 해보자
=> 위 방법은 시간초과가 나온다 ㅠㅠ

슬라이싱 말고 다른 방법이 있을까?
이중 for 문을 돌려보자
=> 아니 이중 for 문도 안되네? 뭐지?

그렇다면 for 문을 한번만 써보자 미리 값을 더해서 빼거나 더하는 형태로 만들면 되겠지?

"""

T = 1

for tc in range(1, T+1) :
    N, K = map(int, input().split())                # 정수를 받아오고
    temp_list = list(map(int, input().split()))     # 리스트를 받아오고
    result = 0                                      # 결과 저장
    for i in range(0, N-K+1):          # 온도 리스트의 인덱스를 순회, 슬라이싱 할거기 때문에 뒷부분 제외
        if sum(temp_list[i:i+K]) > result :         # 결과가 더 큰 수가 나오면 업데이트
            result = sum(temp_list[i:i+K])
    print(result)


####### 위 풀이방식은 시간초과가 나오니 슬라이싱으로 접근하지 말자

# N, K = map(int, input().split())
# temp = list(map(int, input().split()))
# r = 0
# for i in range(0, N-K+1):
#     mm = 0
#     for j in range(K):
#         mm += temp[i+j]
#     if mm > r:
#         r = mm
# print(r)

