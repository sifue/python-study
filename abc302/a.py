import sys
import numpy as np
import math
import bisect
sys.setrecursionlimit(10**7) # 再起回数の設定
A, B = map(int, input().split())

if A % B == 0:
    print(A // B)
else:
    print(A // B + 1)

