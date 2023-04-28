import sys
import numpy as np
H, W = map(int, input().split())
ary = [list(map(int, input().split())) for i in range(H)]
blocks = np.array(ary)
minimum = np.min(blocks)
print(np.sum(blocks - minimum))