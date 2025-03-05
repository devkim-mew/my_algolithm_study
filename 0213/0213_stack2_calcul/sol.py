import sys
sys.stdin = open("input.txt", "r")

#############################################

T = 10   # test_case 개수를 받아옴

print('a')
print("b")
print("c")


for tc in range(1, T+1) :
    pass
    N = int(input())
    add_arr = input()


    def infix_to_postfix(arr) :
        stack = []                                  # +를 모아둘 스택, 사실 모여지진 않음
        post_fix = []                               # 출력을 위해 후위표기법으로 만드는 값

        for i in arr :                              # 매개변수로 받은 배열의 요소를 돌림
            if i.isnumeric() :                      # 요소가 숫자라면
                post_fix.append(i)                  # 후위표기 결과값에 바로 넣어줌

            else :
                while stack :                       # 숫자가 아니라면
                    post_fix.append(stack.pop())    # 스택에 값이 있다면, 스택의 최근 입력값을 꺼내 결과값에 넣어줌
                stack.append(i)                     # 스택에 값이 없다면, 숫자가 아닌 건 스택에 쌓아줌

        while stack :                               # 받은 문자열을 전부 돌고 스택에 값이 있다면
            post_fix.append(stack.pop())            # 스택에 있는 거 다 뽑아서 결과에 넣어줌

        return "".join(post_fix)                    # 결과를 문자열로 반환


    def postfix_to_infix(arr) :
        stack = []                                  # 피연산자를 저장할 스택
        tokens = list(arr)                          # 문자열을 받아오면 리스트로 변환, 토큰스로 저장한 건 최소단위를 뜻하기 위함


        for token in tokens :                       # 받아온 거 전부 돌고
            if token.isnumeric() :                  #
                stack.append(int(token))

            else :
                val2 = stack.pop() # 제일 최근에 저장된 숫자
                val1 = stack.pop() # 그 이전에 저장된 숫자

                if token == '+' :
                    stack.append(val1 + val2)

        return stack.pop()

    print(f"#{tc} {postfix_to_infix(infix_to_postfix(add_arr))}")








# for tc in range(1, T+1) :
#     pass
#     N = int(input())
#     add_arr = input()
#
#
#     def infix_to_postfix(arr) :
#         stack = []    # +를 모아둘 스택, 사실 모여지진 않음
#         post_fix = [] # 출력을 위해 후위표기법으로 만드는 값
#
#         for i in arr :
#             if i.isnumeric() :
#                 post_fix.append(i)
#
#             else :
#                 while stack :
#                     post_fix.append(stack.pop())
#                 stack.append(i)
#
#         while stack :
#             post_fix.append(stack.pop())
#
#         return "".join(post_fix)
#
#
#     def postfix_to_infix(arr) :
#         stack = [] # 피연산자를 저장할 스택
#         tokens = list(arr)
#
#
#         for token in tokens :
#             if token.isnumeric() :
#                 stack.append(int(token))
#
#             else :
#                 val2 = stack.pop() # 제일 최근에 저장된 숫자
#                 val1 = stack.pop() # 그 이전에 저장된 숫자
#
#                 if token == '+' :
#                     stack.append(val1 + val2)
#
#         return stack.pop()
#
#     print(f"#{tc} {postfix_to_infix(infix_to_postfix(add_arr))}")
#
#

