"""
zip으로 풀면 안된다 ㅠㅠ 문자열의 길이가 중간에 짧은 게 있기 때문임



"""

import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    words = [input() for _ in range(5)]
    result = '' # 문자열은 수정 가능하므로 추가로 넣을 수 있음

    max_length = 0
    for word in words:
        # 여태까지 나온 최대 길이와 현재 문자열의 길이를 비교해서
        # 현재 문자열의 길이가 더 길어진다면, 최대 길이 갱신
        max_length = max(max_length, len(word))

    # 열을 순회! => 최대 길이만큼 순회
    for col in range(max_length):
        # 행을 순회 => 행은 무조건 5개
        for row in range(5):
            # 해당 행의 길이가 현재 열보다 작은 경우면 문자가 존재함
            # 결과에 추가
            if col < len(words[row]):
                result += words[row][col]

    print(f"#{tc}", result)
    print(words)