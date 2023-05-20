import sys
import numpy as np
import math
import bisect
sys.setrecursionlimit(10**7) # 再起回数の設定
N = int(input())

if N % 2 == 0:
    print(N)
else:
    print(2 * N)
