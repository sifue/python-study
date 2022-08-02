import sys
sys.setrecursionlimit(10**7) # 再起回数の設定
N, M, X = map(int, input().split())
books = [list(map(int, input().split())) for i in range(N)]
minimum = 1200001
# 深さ優先探索で全探索する
def dfs(i, cost, levels):
    if (i == N):
        isOK = True
        for lv in levels:
            if (lv < X):
                isOK = False
        if (isOK):
            global minimum
            minimum = min(cost, minimum)
        return

    # その本を読まない
    dfs(i + 1, cost, levels) 

    # その本を読む
    newLevels = []
    for j in range(M):
        newLevels.append(levels[j] + books[i][j + 1]);
    dfs(i + 1, cost + books[i][0], newLevels)

dfs(0, 0, [0 for i in range(M)])
if (minimum == 1200001):
    print(-1)
else:
    print(minimum)