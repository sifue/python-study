import sys
import numpy as np
sys.setrecursionlimit(10**7) # 再起回数の設定
H, W = map(int, input().split())
C = [list(input()) for i in range(H)]
N = min(H, W)
result = [0 for i in range(N)]

for i in range(H):
    for j in range(W):
        if C[i][j] == "#": # 伸ばせるかどうか
            max_size = min(H - i - 1, W - j - 1, i, j) # 伸ばせる最大サイズ

            # print("[i, j, max_size]:")
            # print([i, j, max_size])

            if (max_size > 0):
                current_size = 0
                for k in range(1, max_size + 1):
                    if C[i+k][j+k] == "#" and C[i+k][j-k] == "#" and C[i-k][j+k] == "#" and C[i-k][j-k] == "#":
                        current_size += 1
                    else:
                        break

                if (current_size > 0):
                    result[current_size - 1] += 1

print(" ".join(map(str, result)))