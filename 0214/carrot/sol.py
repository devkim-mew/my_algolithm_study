import sys
sys.stdin = open("sample_in.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))
    carrots.sort()
    result = []

    for i in range(1, N - 1):  # i의 범위는 1 ~ N-2까지
        for j in range(i + 1, N):  # j의 범위는 i ~ N-1까지

            s_box = carrots[:i]
            m_box = carrots[i:j]
            l_box = carrots[j:]

            if len(s_box) > N // 2 or len(m_box) > N // 2 or len(l_box) > N // 2:  # 하나의 박스가 만약 N의 반 보다 큰 경우
                continue  # 밑 코드는 안 돌리고 다시 돌아가

            if s_box[-1] != m_box[0] and m_box[-1] != l_box[0]:  # 숫자가 같은 곳에 있어야 하니 같지 않을 경우
                box_length = [len(s_box), len(m_box), len(l_box)]
                result.append(max(box_length) - min(box_length))
                continue

    if len(result) != 0 :
        print(f"#{test_case}", min(result))
    else:
        print(f"#{test_case}", -1)