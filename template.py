import sys
import numpy as np
import math
import bisect
from collections import deque
sys.setrecursionlimit(10**7) # 再起回数の設定
N, M, X = map(int, input().split()) # 1行
ary = [list(map(int, input().split())) for i in range(N)] #N行の配列化
books = np.array(ary)
