import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    pass

    N, M = map(int, input().split())        # 배열의 길이와 옮길 횟수를 받아오고
    arr = deque(map(int, input().split()))  # 돌려버릴 배열을 받아온다

    for _ in range(M):                      # 앞 자리를 M번만큼 뒤로 보낸다
        arr.append(arr.popleft())

    print(f"#{test_case}", arr[0])


