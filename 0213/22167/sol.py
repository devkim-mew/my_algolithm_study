import sys
sys.stdin = open("input.txt", "r")

#############################################

T = int(input())    # test_case 개수를 받아옴

for tc in range(1, T+1) :
    pass
    char = list(input())                # 입력 문자열을 받아옴
    result = ""                         # 출력값

    def reverse(char, result) :          # 리버스 함수에 매개변수로 문자열과 출력값을 넣음
        cnt = 0                         # 도는 횟수 카운트
        if len(char) == cnt :           # 문자열 길이 만큼 돌면 최종 반환
            return str(result)
        else:
            result += char[-1]          # 출력값에 문자열의 끝을 추가
            char.pop()                  # 문자열의 끝을 지움
            cnt += 1
            return reverse(char, result) # 다시 함수를 재귀

    print(reverse(char, result))



############################## 
# 강사님 코딩

def rec(idx) :
    if idx == 0 :
        return string[idx]
    else:
        return string[idx] + rec(idx-5)

N= int(input())
for tc in range(1, N + 1) :
    string = input()

    print(rec(len(string)-1))





