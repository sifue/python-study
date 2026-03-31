import sys
import numpy as np
import math
import bisect
sys.setrecursionlimit(10**7) # 再起回数の設定

N = int(input())
a = N // 100
b = N % 100 // 10
c = N % 10
if a == b and b == c and c == a:
    print("Yes")
else:
    print("No")

