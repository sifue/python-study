import sys
import numpy as np
import math
import bisect
from collections import deque
sys.setrecursionlimit(10**7) # 再帰回数の設定
N, M = map(int, input().split()) # 1行
LR = [tuple(map(int, input().split())) for i in range(M)] #N行の配列化
turrets = [0] * (N+1)

for i in range(M):
    L = LR[i][0]
    R = LR[i][1]
    L -= 1
    turrets[L] += 1
    turrets[R] -= 1

for i in range(1, N+1):
    turrets[i] += turrets[i-1]

ans = 1e9
for i in range(N):
    ans = min(ans, turrets[i])

print(ans)

