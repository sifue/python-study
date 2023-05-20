import sys
import numpy as np
import math
import bisect
sys.setrecursionlimit(10**7) # 再起回数の設定
a, b, c = map(int, input().split())

set = set()
set.add(a)
set.add(b)
set.add(c)
print(len(set))