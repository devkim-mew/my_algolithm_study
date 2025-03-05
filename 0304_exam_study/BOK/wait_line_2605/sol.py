import sys
sys.stdin = open("input.txt", "r")

"""
점심 줄을 서는데
첫번째 학생은 0번
두번째 학생은 0또는 1을 뽑고 0이면 그 자리, 1이면 한명을 제침
세번째 학생은 0,1,2 중 뽑고 뽑은 수 만큼 제친다

각자 뽑는 수는 인덱스와 같음

N 학생 수
select = 선택한 카드
line = 학생들의 번호를 줄대로 출력

for 문으로 N만큼 돌면서
셀렉트의 인덱스 번호가 0이면 그대로 추가
1이상이면 -인덱스로 뒤로 추가
카운트를 하면서 학생의 번호를 늘려간다

"""

N = int(input())
select = list(map(int, input().split()))
line = []
line_cnt = 1
for i in select:
    line.append(line_cnt)
    if i > 0:
        line.insert(-i, line.pop())
    line_cnt += 1

print(*line)


