import sys
import numpy as np
sys.setrecursionlimit(10**7) # 再起回数の設定
H, W = map(int, input().split())
A = [list(input()) for i in range(H)]
A = np.array(A)
B = [list(input()) for i in range(H)]
B = np.array(B)

for i in range(H):
    h_rolled = np.roll(A, i, axis=0)
    for j in range(W):
        hw_rolled = np.roll(h_rolled, j, axis=1)
        if np.array_equal(B, hw_rolled):
            print("Yes")
            exit()
print("No")