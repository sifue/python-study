import sys
import numpy as np
sys.setrecursionlimit(10**7) # 再起回数の設定
N, M = map(int, input().split())
condABs = [list(map(int, input().split())) for i in range(M)]
K = int(input())
condCDs = [list(map(int, input().split())) for i in range(K)]

false_array = [False for _ in range(N+1)] # インデックスと番号の整合性のため0番目は使わない
maximum = 0

def dfs(i, used):
    if (i == K):
        # print(used)
        count = 0
        for condAB in condABs:
            if (used[condAB[0]] and used[condAB[1]]):
                count += 1
        global maximum
        maximum = max(count, maximum)
        return

    # 一つ目の皿にボールを置く
    fst_used = used.copy()
    fst_used[condCDs[i][0]] = True
    dfs(i + 1, fst_used)

    # 二つ目の皿にボールを置く
    snd_used = used.copy()
    snd_used[condCDs[i][1]] = True
    dfs(i + 1, snd_used)

dfs(0, false_array)
print(maximum)
