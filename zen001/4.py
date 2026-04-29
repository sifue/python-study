import sys
import numpy as np
import math
import bisect
from collections import deque
sys.setrecursionlimit(10**7) # 再帰回数の設定
N, K = map(int, input().split()) # 1行

year = 0
eaten = 0
while eaten < K:
    eaten += year + N
    year += 1
print(year - 1)

