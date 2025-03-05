import sys
sys.stdin = open("4866_input.txt", "r")

#############################################

T = int(input())    # test_case 개수를 받아옴

for tc in range(1, T+1) :
    pass
    str_value = input() # 문자열을 받아옴
    stack_str_value = [] # 문자열 중 괄호만의 스택을 설정
    bool_stack = 0 # 괄호의 정상 여부, False로 초기설정

    for i in str_value : # 문자열 전체 검사
        if i == '(' or i == '{' : # 여는 괄호를 스택에 쌓기
            stack_str_value.append(i)
        if i == ')' : # 닫는 괄호를 마주치면 여는 괄호 지우기
            stack_str_value.remove('(')
        elif i == '}' :
            stack_str_value.remove('{')

    if len(stack_str_value) == 0 : # 스택이 비어있다면 True로 바꿔줌
        bool_stack = 1

    print(f"#{tc} {bool_stack}")