import sys
import numpy as np
import math
import bisect
from collections import deque
sys.setrecursionlimit(10**7) # 再帰回数の設定
X, Y = map(int, input().split()) # 1行
print(X * (2 ** Y))

