import sys
import numpy as np
import math
from bisect import bisect_left, bisect_right
sys.setrecursionlimit(10**7) # 再起回数の設定
N = int(input())

# 実装はできたが、30秒ぐらいかかる...

# エラストテネスの篩による素数のリストの作成
def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False

    for num in range(2, int(limit ** 0.5) + 1):
        if primes[num]:
            for multiple in range(num * num, limit + 1, num):
                primes[multiple] = False

    return [num for num in range(2, limit + 1) if primes[num]]

primes = sieve_of_eratosthenes(math.isqrt(math.ceil(N / 12))) # N / (2 * 2 * 3) の平方根、つまりcの最大数までの素数を列挙
# print(primes)
# print(len(primes))

count = 0
for c in primes:
    if c * c > N:
        break
    for i, a in enumerate(primes):
        if a >= c:
            break

        b = N // (a * a * c * c)

        if b >= c:
            b = c - 1 # bはc未満の数である必要があるので、許容できる最大で上書きする
        if b <= a:
            break
        b_index = bisect_right(primes, b)
        # print("[a, c, b_index]", end="=")
        # print([a, c, b_index])
        count += (b_index - i - 1)

print(count)
