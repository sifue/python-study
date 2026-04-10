import sys
import numpy as np
import math
import bisect
from collections import deque
sys.setrecursionlimit(10**7) # 再帰回数の設定
M, D = map(int, input().split()) # 1行
sekku_set = {(1,7), (3,3), (5,5), (7,7), (9,9)}

if (M,D) in sekku_set:
    print("Yes")
else:
    print("No")

