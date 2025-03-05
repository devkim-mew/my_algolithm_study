import sys
sys.stdin = open("4873_input.txt", "r")

#############################################

T = int(input())    # test_case 개수를 받아옴

for tc in range(1, T+1) :
    pass
    char = list(input())
    stack_char = []

    for word in char :
        if stack_char and  word == stack_char[-1] :
            stack_char.pop()
        else:
            stack_char.append(word)

    print(f"#{tc} {len(stack_char)}")