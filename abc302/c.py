import sys
import numpy as np
sys.setrecursionlimit(10**7) # 再起回数の設定
N, M = map(int, input().split())
S = [input() for i in range(N)]

# 文字列が条件を満たすかどうかをチェックする関数
def check(s1, s2):
    diff = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            diff += 1
    return diff == 1

# DFSで文字列をチェックする関数
def dfs(used, prev):
    if all(used): # すべての文字列を使った場合
        return True
    for i in range(N): # すべての文字列をチェック
        if not used[i] and check(S[prev], S[i]):
            used[i] = True
            if dfs(used, i): # 条件を満たす文字列があれば、続ける
                return True
            used[i] = False
    return False # 条件を満たす文字列がない場合

# メイン処理
for i in range(N):
    used = [False] * N
    used[i] = True
    if dfs(used, i): # 全ての文字列が条件を満たす場合は "YES" を出力
        print("Yes")
        break
else: # 全ての文字列が条件を満たさない場合は "NO" を出力
    print("No")