import sys
import numpy as np
import math
import bisect
sys.setrecursionlimit(10**7) # 再起回数の設定
N = int(input())
temps = [list(map(float, input().split())) for i in range(N)]
temps = np.array(temps)

print(np.count_nonzero(temps[:, 0] >= 35), end=" ")
print(np.count_nonzero((temps[:, 0] >= 30) & (temps[:, 0] < 35 )), end=" ")
print(np.count_nonzero((temps[:, 0] >= 25) & (temps[:, 0] < 30)) , end=" ")
print(np.count_nonzero(temps[:, 1] >= 25), end=" ")
print(np.count_nonzero((temps[:, 1] < 0) & (temps[:, 0] >= 0)), end=" ")
print(np.count_nonzero(temps[:, 0] < 0))