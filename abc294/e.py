import sys
import numpy as np
import math
import bisect
sys.setrecursionlimit(10**7) # 再起回数の設定
L, N1, N2 = map(int, input().split())
VL1 = [tuple(map(int, input().split())) for i in range(N1)]
VL2 = [tuple(map(int, input().split())) for i in range(N2)]

pos1, pos2 = 0, 0
ans = 0
while pos1 < N1 and pos2 < N2:
    v1, l1 = VL1[pos1]
    v2, l2 = VL2[pos2]

    if v1 == v2:  # 共通の整数がある場合
        min_len = min(l1, l2)
        ans += min_len

    if l1 > l2: # l2が短い場合
        VL1[pos1] = (v1, l1 - l2) # l1をl2を引いて更新
        pos2 += 1
    elif l1 < l2: # l1が短い場合
        VL2[pos2] = (v2, l2 - l1) # l2をl1を引いて更新
        pos1 += 1
    else:
        pos1 += 1
        pos2 += 1

print(ans)
