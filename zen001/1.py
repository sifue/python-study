import sys
import numpy as np
import math
import bisect
from collections import deque
sys.setrecursionlimit(10**7) # 再帰回数の設定
S = input()
if S[0] == S[-1]:
    print("Yes")
else:
    print("No")

