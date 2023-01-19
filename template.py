import sys
sys.setrecursionlimit(10**7) # 再起回数の設定
N, M, X = map(int, input().split())
books = [list(map(int, input().split())) for i in range(N)]