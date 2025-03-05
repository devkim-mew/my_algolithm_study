
"""
1~N까지의 수로 이루어진 조합들을 출력하자

"""


# 순열을 수를 먼저 고르고 다 다음 옵션을 고르는 방식으로 찾아야 함

def numbering(selected, remine):
    if not remine:
        print(*selected)
    else:
        for i in range(len(remine)):                 # 선택 전을 순회
            selected_i = remine[i]
            remine_list = remine[:i] + remine[i+1:]  # 선택한 거 제명
            numbering(selected + [selected_i], remine_list)

N = 3
remine = []
for i in range(1, N+1):
    remine.append(i)
numbering([], remine)


# # selected: 선택된 값 목록
# # remain: 선택되지 않고 남은 값 목록
# def perm(selected, remain):
#     if not remain:                                    # 남은 값이 없다면?
#         print(selected)                               # 내가 선택한 순열을 출력
#     else:
#         for i in range(len(remain)):                  # 남은 애들 길이만 돌림
#             select_i = remain[i]                      # 내가 고른 애
#             remain_list = remain[:i] + remain[i+1:]   # 내가 선택한 애, i를 제외하고 남은 애들
#             perm(selected + [select_i], remain_list)  # 내가 고른애, 남은 애들 목록을 재귀
#
# perm([], [1, 2, 3])