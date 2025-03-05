import sys
sys.stdin = open("input.txt", "r")




from itertools import permutations

# 숫자가 1씩 증가하는 지 확인
def is_run(target):
    # target의 길이는 3으로 상정 함수를 작성
    # baby gin에서 카드를 판단할 때는 무조건 세장을 가지고 판단하기 때문에
    return (target[0] + 1 == target[1]) and (target[1] + 1 == target[2])
    # 단축평가여서 값이 리넡 될 것 같지만,
    # 비교연산이기 때문에 값은 T/F로 나옴

def is_triplet(target):
    # 방법 1
    # cnt = 0
    # for card in target:
    #     if target[0] == card :
    #         cnt += 1
    # return cnt == 3  # 비교 연산으로 T/F로 출력

    # 방법 2 : 세트의 특성을 사용
    return len(set(target)) == 1

def is_babygin(target):
    num1 = target[:3]
    num2 = target[3:]

    # 런이나 트리플릿이면 result는 0이 아니고 1이 들어가게 됨
    result1 = is_run(num1) + is_triplet(num1)   # 앞 숫자에 대한 런/트리플릿 확인, 0이 아니라면 result에 뭐가 들어갈 것
    result2 = is_run(num2) + is_triplet(num2)   # 뒷 숫자에 대한 런/트리플릿 확인

    return (result1 + result2) == 2             # result1, result2 둘 다 런/트리플릿이라면 결과는 2가 나옴


T = int(input())

for tc in range(1, T+1) :
    card_list = list(map(int, input().strip()))

    result = "false"
    for target in permutations(card_list) :
        if is_babygin(target):
            result = "true"
            break

    print(f"#{tc}", result)























