import sys
sys.stdin = open("4834_input.txt", "r")

#############################################

T = int(input())    # test_case 개수를 받아옴

# 카드목록을 순회해서 카드의 개수들을 리스트로 만들어줌
# 가장


for tc in range(1, T+1) :
    N = int(input())
    cards = list(map(int, input()))

    big_card = cards[0]
    for i in range(len(cards)) :
        if big_card < cards[i] :
            big_card = cards[i]

    count_card = [0] * (big_card + 1)

    for num in cards :
        count_card[num] += 1

    count_many_card = 0






print(f"#{tc}  {cards}")







