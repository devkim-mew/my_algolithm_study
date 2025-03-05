import sys
sys.stdin = open("input.txt", "r")

"""
N이 주어지면
N 중에 하나를 고르고
그 다음 수들은 앞자리에서 뒷자리를 빼며 이어감
음수가 출력되면 멈춤
이 때 가장 긴 길이를 출력

어떻게 풀까?
먼저 최적의 두번째 수를 찾기 위해 다 돌아야 하니까 N을 모두 순회하면서 고르고
while로 마이너스를 반복
배열에 수들을 저장해둠

"""

N = int(input().strip())
result = []
for i in range(N, 0, -1):
    num = [N, i]
    bk = 0
    while bk == 0:
        num.append(num[-2] - num[-1])
        if num[-1] < 0:
            num.pop()
            bk = 1
            break
    if len(num) > len(result):
        result = num
print(len(result))
print(*result)
