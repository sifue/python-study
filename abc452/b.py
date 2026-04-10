import sys
import numpy as np
import math
import bisect
from collections import deque
sys.setrecursionlimit(10**7) # 再帰回数の設定
H, W = map(int, input().split()) # 1行

for i in range(H):
    for j in range(W):
        if i == 0 or j == 0 or i == H - 1 or j == W - 1:
            print("#", end="")
        else:
            print(".", end="")
    print()
