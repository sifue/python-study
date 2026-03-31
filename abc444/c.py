import sys
import numpy as np
import math
import bisect
sys.setrecursionlimit(10**7) # 再起回数の設定
N = int(input())
A = list(map(int, input().split()))
print(N)
print(A)

# すべての組み合わせで成立するLを全パターン探す問題
