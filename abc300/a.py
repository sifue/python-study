import sys
import numpy as np
sys.setrecursionlimit(10**7) # 再起回数の設定
N, A, B = map(int, input().split())
C = list(map(int, input().split()))
ans = A + B

for i in range(N):
    if C[i] == ans:
        print(i + 1);
        exit()

print(-1)
exit()