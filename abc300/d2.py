def enumerate_primes(n):
    if n <= 1:
        return []
    A = [1, 7, 11, 13, 17, 19, 23, 29]
    thres = (n + 29) // 30
    sieve = [255] * (thres + int(n ** 0.5) + 10)
    ntoi = lambda i: (i >> 2) + (not (~i & 19))
 
    sieve[0] ^= 1
    i = 0
    flg = 1
    while flg:
        if sieve[i] != 0:
            for j in range(8):
                if sieve[i] >> j & 1:
                    p = i * 30 + A[j]
                    if (p * p > n):
                        flg = 0
                        continue
                    q = [0] * 8
                    r = [0] * 8
                    s = 0
                    for k in range(8):
                        x = p * (i * 30 + A[k])
                        q[k] = x // 30
                        r[k] = ntoi(x - 30 * q[k])
                    while q[0] + s < thres:
                        sieve[q[0] + s] &= ~(1 << r[0])
                        sieve[q[1] + s] &= ~(1 << r[1])
                        sieve[q[2] + s] &= ~(1 << r[2])
                        sieve[q[3] + s] &= ~(1 << r[3])
                        sieve[q[4] + s] &= ~(1 << r[4])
                        sieve[q[5] + s] &= ~(1 << r[5])
                        sieve[q[6] + s] &= ~(1 << r[6])
                        sieve[q[7] + s] &= ~(1 << r[7])
                        s += p
 
        i += 1
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for i in range(1, thres):
        for j in range(8):
            if sieve[i] >> j & 1:
                primes.append(i * 30 + A[j])
    while primes[-1] > n:
        primes.pop()
    return primes
 
 
from bisect import bisect_left, bisect_right
 
n = int(input())
P = enumerate_primes(1000000)
ans = 0
for c in P:
    if c * c > n:
        break
    for i, a in enumerate(P):
        if a >= c:
            break
        b = n // (a * a * c * c)
        if b >= c:
            b = c - 1
        if b <= a:
            break
        ans += bisect_right(P, b) - i - 1
 
print(ans)