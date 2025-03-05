import sys
sys.stdin = open('input.txt', 'r')

def word_line(a):
    global result
    if a <= N:
        word_line(a * 2)
        result += list[a]
        word_line(a * 2 + 1)

T = 10
for tc in range(1, T+1):
    N = int(input())
    list = ["0"]
    result = ""
    for i in range(1, N+1):
        nums = input().split()
        list.append(nums[1])

    word_line(1)

    print(result)