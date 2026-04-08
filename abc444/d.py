import sys
import numpy as np
import math
import bisect
from collections import deque
sys.setrecursionlimit(10**7) # 再起回数の設定
N = int(input())
A = sorted(map(int, input().split()))

res = []
carry = 0
alive = N
prev = 0
i = 0

while i < N:
    x = A[i]

    # prev+1 桁目 ～ x 桁目までは alive 本が寄与
    for _ in range(x - prev):
        carry += alive
        res.append(str(carry % 10))
        carry //= 10

    # 長さ x のものをまとめて消す
    while i < N and A[i] == x:
        alive -= 1
        i += 1

    prev = x

# 残った carry を出力
while carry > 0:
    res.append(str(carry % 10))
    carry //= 10

print(''.join(reversed(res)))
