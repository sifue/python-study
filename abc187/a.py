import sys
sys.setrecursionlimit(10**7) # 再起回数の設定
A, B = map(int, input().split())

def sumDigits(n):
    sum = 0
    while (n > 0):
        sum += n % 10
        n //= 10
    return sum
print(max(sumDigits(A), sumDigits(B)))