import sys
import numpy as np
import math
import bisect
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
for i, a in enumerate(primes):
    for j in range(i + 1, len(primes)):
        c = primes[j]
        if a * a * c * c > N:
            continue
        b_index = bisect.bisect_right(primes[i:j], N / (a * a * c * c))
        # print("[a, b, b_index]", end="=")
        # print([a, c, b_index])
        if b_index > 1:
            count += (b_index - 1)
print(count)
