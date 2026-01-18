import sys
import numpy as np
import math
import bisect
sys.setrecursionlimit(10**7) # 再起回数の設定
x = map(int, input().split())
r = next(x)
print(r * r * 3)
