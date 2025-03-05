import sys
sys.stdin = open("input.txt", "r")

"""
ATM 앞에 줄을 섰을 때 1~N까지 번호가 있음
i번 사람이 돈을 인출하는데 걸리는 시간은 pi분
모두가 돈을 인출하는데 최솟값을 구해보자
N 사람 수
pi 사람들마다 걸리는 시간
사람들마다 걸리는 시간을 모두 더해보자

어떻게 풀까?
작은 수부터 정렬하는 것이 줄의 시간이 제일 빠르다 정렬 후 해보자

"""

N = int(input())
waiting_time = list(map(int, input().split()))
waiting_time.sort()
total_time = [waiting_time[0]]

for i in range(1, N):
    total_time.append(waiting_time[i] + total_time[-1])

print(sum(total_time))




