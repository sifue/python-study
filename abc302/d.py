import sys
import numpy as np
import bisect
sys.setrecursionlimit(10**7)
N, M, D = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

def find_maximum_pair(A, B, D):
    max_sum = -1
    for a in A:
        # aからD減算した値をBで探索して、条件を満たす最も大きいbを見つける
        search_key = a - D
        idx = bisect.bisect_left(B, search_key)
        if (0 <= idx < len(B)) and check_difference(a, B[idx], D):
            max_sum = max(max_sum, a + B[idx])

        # aとDの範囲内で最も小さいbを見つける
        search_key = a + D
        idx = bisect.bisect_right(B, search_key)
        if (0 < idx) and check_difference(a, B[idx - 1], D):
            max_sum = max(max_sum, a + B[idx - 1])
    return max_sum

# 差の絶対値がD以下であればTrue、そうでなければFalseを返す関数
def check_difference(a, b, D):
    return abs(a - b) <= D

result = find_maximum_pair(A, B, D)
print(result)