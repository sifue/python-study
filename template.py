import sys
import numpy as np
import math
import bisect
sys.setrecursionlimit(10**7) # 再起回数の設定
N, M, X = map(int, input().split())
ary = [list(map(int, input().split())) for i in range(N)]
books = np.array(ary)