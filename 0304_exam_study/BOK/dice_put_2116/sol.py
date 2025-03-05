import sys
sys.stdin = open("input.txt", "r")

"""
1번 주사위부터 순서대로 쌓는다
쌓을 때 주사위의 윗면과 아랫면이 같아야 한다
또, 주사위 기둥의 4면 중 한면의 숫자 합이 최대가 되도록 쌓아야 한다
주사위의 짝은 AF BD CE 로 이루어져 있다
인덱스의 짝이 0,5 / 1,3 / 2,4

어떻게 풀까?
밑면 하나가 정해지면 나머지 주사위 값들은 모두 정해진다
이 특징을 이용하면 밑면 하나를 기준으로 순회를 돌리고
옆면들 중 가장 큰 수들만 더해보자


"""

N = int(input())
dice_list = [list(map(int, input().split())) for _ in range(N)]

# 인덱스와 값을 매칭해줌
top_bottom = [5, 3, 4, 1, 2, 0]
result = 0

for bottom_idx in range(6):
    bottom = dice_list[0][bottom_idx]
    top = dice_list[0][top_bottom[bottom_idx]]
    now_total = 0

    for j in range(N):
        if j > 0:                                       # 두번째 주사위부터는 아랫값을 이전의 윗값으로 바꿔줌
            bottom = top
            bottom_idx = dice_list[j].index(bottom)
            top = dice_list[j][top_bottom[bottom_idx]]

        side_values = [dice_list[j][k] for k in range(6) if k not in (bottom_idx, top_bottom[bottom_idx])]  # 아래 위 제외한 4면의 값들 모으기
        now_total += max(side_values)                   # 4면중 가장 큰 값 더해줌

    result = max(result, now_total)
print(result)


























#
# N = int(input())
# dice_list = [list(map(int, input().split())) for _ in range(N)]
#
# result = 0
# for i in range(6):
#     up_face = i
#     drrr = 0
#     for j in range(N):
#         if up_face == 0 :
#             up_face = 5
#             drrr += max(dice_list[j][1], dice_list[j][2], dice_list[j][3], dice_list[j][4])
#         elif up_face == 1:
#             up_face = 3
#             drrr += max(dice_list[j][0], dice_list[j][2], dice_list[j][4], dice_list[j][5])
#         elif up_face == 2:
#             up_face = 4
#             drrr += max(dice_list[j][0], dice_list[j][1], dice_list[j][3], dice_list[j][5])
#         elif up_face == 3:
#             up_face = 1
#             drrr += max(dice_list[j][0], dice_list[j][2], dice_list[j][4], dice_list[j][5])
#         elif up_face == 4:
#             up_face = 2
#             drrr += max(dice_list[j][0], dice_list[j][1], dice_list[j][3], dice_list[j][5])
#         elif up_face == 5:
#             up_face = 0
#             drrr += max(dice_list[j][1], dice_list[j][2], dice_list[j][3], dice_list[j][4])
#     result = max(result, drrr)
# print(result)
