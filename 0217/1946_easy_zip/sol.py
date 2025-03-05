"""
원본 문서는 너비가 10인 여러줄의 문자열로 이루어짐
문자열은 마지막 줄을 제외하고 빈 공간 없이 문자로 채워짐
문자열과 수가 주어지면 원본 문서를 만드는 작업을 하자

입력
N 문자열의 종류


어떻게 풀까?
1. 원본 문서를 만들기 위한 빈 리스트를 만들고
2. 문자열을 받아와서 빈 리스트에 해당 문자열을 수 만큼 순회하며 집어 넣고
3. 다른 문자열들도 반복한다
4. 출력할 때 10줄 씩 문자열을 붙여서 출력하자
"""

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    result = []
    for _ in range(N):
        word, num = input().split()
        for i in range(int(num)):
            result.append(word)

    print(f"#{test_case}")
    for p in range(len(result)):
        if p % 10 == 0 and p != 0:
            print()
        print(result[p], end="")
    print()




