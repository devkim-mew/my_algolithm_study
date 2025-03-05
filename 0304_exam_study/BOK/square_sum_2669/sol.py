arr = [[0]*100 for _ in range(100)]
N = 4
result = 0

for n in range(N):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(x1, x2):       # 2~4
        for j in range(y1, y2):   # 1~4
            arr[i][j] = 1

for idx in arr:
    result += idx.count(1)

print(result)