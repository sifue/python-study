import sys
import numpy as np
import math
import bisect
sys.setrecursionlimit(10**7) # 再起回数の設定
N = int(input())
A = list(map(int, input().split()))

maxA = max(A)
candL = set()
candL.add(maxA)
for ai in A:
    for aj in A:
        candL.add(ai + aj)
candL = sorted(list(candL))

#print("candL")
#print(candL)

result = []
for l in candL:
    #print("l")
    #print(l)
    check_list = list(A)
    is_found = True # 調査フラグ、未調査時はTrueでスタート
    for i, a in enumerate(A):
        if not check_list[i]: # すでに利用済みならパス
            continue
        #print("i")
        #print(i)
        check_list[i] = False
        if a == l:
            #print("continue")
            continue
        else:
            is_found = False # 調査開始とともにFalseに
            for j, ap in enumerate(A):
                if check_list[j] and a + ap == l:
                    check_list[j] = False
                    is_found = True # ペア発見
                    break
            #print("is_found")
            #print(is_found)
            if not is_found:
                break
    if check_list.count(False) == N and is_found:
        result.append(l)
print(" ".join(map(str, result)))


