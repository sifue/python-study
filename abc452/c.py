import sys
import numpy as np
import math
import bisect
from collections import deque
sys.setrecursionlimit(10**7) # 再帰回数の設定
N = int(input())
AB = [list(map(int, input().split())) for i in range(N)] #N行の配列化
M = int(input())
S = [input() for i in range(M)] #N行の配列化

#print(N)
#print(AB)
#print(M)
#print(S)

for j in range(M):
    sj = S[j]
    if len(sj) != N:
        print("No")
    else:
        print("Yes") # TODO

