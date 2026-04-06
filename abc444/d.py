import sys
import numpy as np
import math
import bisect
from collections import deque
sys.setrecursionlimit(10**7) # 再起回数の設定
N = int(input())
A = sorted(list(map(int, input().split())))
#print(N)
#print(A)
result = []
counter = 0
adder = N
pre_ai = 0
for i in range(N):
    ai = A[i]
    if i == N-1:
        for step in range(ai-pre_ai):
            result.append(str(adder))
        break
    else:
        next_ai = A[i+1]
        if ai == next_ai:
            continue
        step_length = next_ai - ai
        for step in range(step_length):
            counter += adder
            digit = counter % 10
            result.append(str(digit))
            counter = counter // 10
        pre_ai = ai
    adder -= 1
print("".join(reversed(result)))

