import sys
import numpy as np
import math
import bisect
sys.setrecursionlimit(10**7) # 再起回数の設定
S = input()

for i in range(1, len(S)):
    if S[i] == S[i - 1]:
        print("Bad")
        sys.exit()

print("Good")