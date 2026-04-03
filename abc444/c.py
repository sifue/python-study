import sys
import numpy as np
import math
import bisect
from collections import deque
sys.setrecursionlimit(10**7) # 再起回数の設定
N = int(input())
A = list(map(int, input().split()))
A = sorted(A, reverse=True)
no_split_A = deque(A)
all_split_A = deque(A)
result = []

# 割れなかったものがあり
maxA = max(A)

while len(no_split_A) > 0 and no_split_A[0] == maxA:
    no_split_A.popleft() #Lを除く

if len(no_split_A) % 2 == 0:
    while len(no_split_A) >= 2 and no_split_A[0] + no_split_A[-1] == maxA:
        no_split_A.pop()
        no_split_A.popleft()
if len(no_split_A) == 0:
    result.append(maxA)

# 全て割れている
candL = all_split_A[0] + all_split_A[-1]
#print("all_split_A")
#print(all_split_A)
#print("candL")
#print(candL)
if len(all_split_A) % 2 == 0:
    while len(all_split_A) >= 2 and all_split_A[0] + all_split_A[-1] == candL:
        all_split_A.pop()
        all_split_A.popleft()
if len(all_split_A) == 0:
    result.append(candL)

print(" ".join(map(str, result)))


