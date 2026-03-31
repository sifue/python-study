import sys
import numpy as np
import math
import bisect
sys.setrecursionlimit(10**7) # 再起回数の設定
N, K = map(int, input().split())

count = 0
for i in range(N + 1):
    digits = list(str(i))
    result = 0
    for s in digits:
        result += int(s)
    if result == K:
        count += 1
print(count)
