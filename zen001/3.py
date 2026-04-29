import sys
import numpy as np
import math
import bisect
from collections import deque
sys.setrecursionlimit(10**7) # 再帰回数の設定
X = int(input())
sum = 0
for i in range(9):
    for j in range(9):
        target = (i + 1) * (j + 1)
        if target != X:
            sum += target
print(sum)

