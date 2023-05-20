# WIP

import sys
sys.setrecursionlimit(10**7)  # 再起回数の設定
H, W, N, h, w = map(int, input().split()) # H, W: グリッドの大きさ, N: 塗りつぶす回数, h, w: 塗りつぶすグリッドの大きさ
A = [list(map(int, input().split())) for i in range(H)]

# 累積和(v[0:i][0:k]リストの作成 [i][j] でアクセス (i,j) はそれぞれ0始まりに変更、計算をシンプルにしたいので一つ外側まで埋めておく
cumulative_sum = [[ {} for _ in range(W+1)] for _ in range(H+1)]

base = {i: 0 for i in range(1, N+1)}
for i in range(H+1):
    for j in range(W+1):
        if(i == 0 and j == 0):
            cumulative_sum[i][j] = base.copy()
            for k, v in cumulative_sum[i][j].items():
                cumulative_sum[i][j][k] = v + (A[i][j] == k)

        elif(i == H or j == W): # はみ出し分は、左の累積和と上の累積和と足して、左上を引いておくだけ
            cumulative_sum[i][j] = cumulative_sum[i][j-1].copy()
            for k, v in cumulative_sum[i-1][j].items():
                cumulative_sum[i][j][k] = cumulative_sum[i][j].get(k, 0) + v
            for k, v in cumulative_sum[i-1][j-i].items():
                cumulative_sum[i][j][k] = cumulative_sum[i][j].get(k, 0) - v

        elif(i == 0): # 1行目の場合、左の累積和をコピーして、その行の累積和を計算する
            cumulative_sum[i][j] = cumulative_sum[i][j-1].copy()
            for k, v in cumulative_sum[i][j].items():
                cumulative_sum[i][j][k] = v + (A[i][j] == k)
        
        elif(j == 0): # 1列目の場合、上の累積和をコピーして、その列の累積和を計算する
            cumulative_sum[i][j] = cumulative_sum[i-1][j].copy()
            for k, v in cumulative_sum[i][j].items():
                cumulative_sum[i][j][k] = v + (A[i][j] == k)

        else: # それ以外の場合、左の累積和と上の累積和と足して、左上をひいて、その行列の累積和を計算する
            cumulative_sum[i][j] = cumulative_sum[i][j-1].copy()
            for k, v in cumulative_sum[i-1][j].items():
                cumulative_sum[i][j][k] = cumulative_sum[i][j].get(k, 0) + v
            for k, v in cumulative_sum[i-1][j-i].items():
                cumulative_sum[i][j][k] = cumulative_sum[i][j].get(k, 0) - v
            for k, v in cumulative_sum[i][j].items():
                cumulative_sum[i][j][k] = v + (A[i][j] == k)

print(cumulative_sum)

# # H, W全体で、k, l, h, wで塗りつぶされていない場所における値の種類数を求める
# def calc_num_types(k, l): # k, l は左上の座標、h, w はグリッドの大きさ
#     num_types = 0
#     for i, v in cumulative_sum[H-1][W-1].items(): # 特定のi(N)について、グリッドの値の出現回数を計算
#         num = v - cumulative_sum[k+h][l+w].get(i, 0) \
#                 + cumulative_sum[k][l+w].get(i, 0) \
#                 + cumulative_sum[k+h][l].get(i, 0) \
#                 - cumulative_sum[k][l].get(i, 0)

#         if num > 0:
#             num_types += 1
#     return num_types

# # 各部分グリッドの値の出現回数を計算し、値の種類数を求める。(k, j) はそれぞれ0始まりになるので注意
# for k in range(H - h + 1):
#     for l in range(W - w + 1):
#         num_types = calc_num_types(k, l)
#         print(num_types, end=" ")
#     print()