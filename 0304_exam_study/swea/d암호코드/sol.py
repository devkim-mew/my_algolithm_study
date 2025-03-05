def solve():
    import sys
    input = sys.stdin.readline

    # 미리 7비트 암호에 따른 숫자 매핑 딕셔너리 정의
    # 각 7비트 문자열이 어떤 숫자에 대응되는지 나타냄
    code_map = {
        "0001101": 0,
        "0011001": 1,
        "0010011": 2,
        "0111101": 3,
        "0100011": 4,
        "0110001": 5,
        "0101111": 6,
        "0111011": 7,
        "0001011": 8,
        "0011101": 9
    }

    # 테스트 케이스의 수 입력받기
    T = int(input().strip())

    for tc in range(1, T + 1):
        # 배열의 세로 크기 N, 가로 크기 M 입력받기
        N, M = map(int, input().split())

        # N줄에 걸쳐서 2차원 배열(문자열 형태) 입력받기
        # 각 줄은 '0'과 '1'로 이루어진 문자열
        grid = [input().strip() for _ in range(N)]

        # 암호코드가 포함된 줄을 찾기 위한 변수 초기화
        code_line = ""

        # 보통 암호코드는 여러 줄에 중복되어 나타날 수 있음.
        # 가장 아래쪽 줄에 실제 암호코드 정보가 들어있으므로,
        # 아래에서부터 탐색하여 '1'이 포함된 첫 번째 줄을 찾는다.
        for row in reversed(grid):
            if '1' in row:
                code_line = row
                break

        # 오른쪽 끝의 '1'의 인덱스를 찾음 (암호코드의 끝 부분)
        end_idx = code_line.rfind('1')
        # 암호코드의 길이는 56이므로, 시작 인덱스는 end_idx - 55
        start_idx = end_idx - 55
        # 56비트의 암호코드를 추출 (문자열 슬라이싱)
        code_str = code_line[start_idx:end_idx + 1]

        # 56비트를 7비트씩 8개의 부분으로 나눠서 숫자 8개로 디코딩
        decoded_digits = []
        for i in range(0, 56, 7):
            # 7비트씩 추출
            segment = code_str[i:i + 7]
            # 매핑 딕셔너리를 이용해 해당 비트 패턴이 나타내는 숫자를 구함
            digit = code_map.get(segment, -1)
            # 만약 매핑되지 않는 패턴이 있으면, 잘못된 암호코드로 처리할 수 있지만
            # 문제에서는 올바른 암호코드가 주어진다고 보장하므로 생략 가능
            decoded_digits.append(digit)

        # 유효성 검증을 위한 계산
        # 문제에서는 "홀수 자리의 합 x 3 + 짝수 자리의 합"이 10의 배수여야 함.
        # 여기서 자리수는 1번째, 3번째, 5번째, 7번째 숫자(인덱스 0,2,4,6)를 홀수자리로,
        # 2번째, 4번째, 6번째, 8번째 숫자(인덱스 1,3,5,7)를 짝수자리로 간주한다.
        odd_sum = decoded_digits[0] + decoded_digits[2] + decoded_digits[4] + decoded_digits[6]
        even_sum = decoded_digits[1] + decoded_digits[3] + decoded_digits[5] + decoded_digits[7]
        checksum = odd_sum * 3 + even_sum

        # 유효한 암호코드이면, 8자리 숫자의 총합을 결과로, 그렇지 않으면 0을 결과로 함
        if checksum % 10 == 0:
            result = sum(decoded_digits)
        else:
            result = 0

        # 출력 형식에 맞게 결과 출력 (예: "#1 38")
        sys.stdout.write(f"#{tc} {result}\n")


# 아래 코드는 로컬 테스트를 위한 실행 코드입니다.
# 실제 평가 환경에서는 제거하거나 주석 처리하면 됩니다.
if __name__ == "__main__":
    solve()
