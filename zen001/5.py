import sys
import numpy as np
import math
import bisect
from collections import deque
sys.setrecursionlimit(10**7) # 再帰回数の設定
N = int(input())
A = list(map(int, input().split()))

if N == 2:
    print("Yes")
    sys.exit()

for i in range(N - 2):
    if A[i] * A[i+2] != A[i+1] * A[i+1]:
        print("No")
        sys.exit()

print("Yes")
