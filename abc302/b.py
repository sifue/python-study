import sys
sys.setrecursionlimit(10**7) # 再起回数の設定
H, W = map(int, input().split())
S = [input() for i in range(H)]

# 二次元配列内で指定されたインデックスが範囲内かどうかを判断するメソッド 
def is_valid_index(array, row, col):
    num_rows = len(array)
    num_cols = len(array[0])
    
    if 0 <= row < num_rows and 0 <= col < num_cols:
        return True
    else:
        return False

# 8方向の移動を定義 一つ目の要素がx、二つ目の要素がy
directions = [(1, 1), (0, 1), (-1, 1), (1, 0), (-1, 0), (1, -1), (0, -1), (-1, -1)]

# 8方向を操作してあったら出力する
for d in directions:
    for i in range(H):
        for j in range(W):
            if S[i][j] == 's' and is_valid_index(S, i + (d[0] * 4), j + (d[1] * 4)):
                if S[i + (d[0] * 1)][j + (d[1] * 1)] == 'n' and \
                      S[i + (d[0] * 2)][j + (d[1] * 2)] == 'u' and \
                        S[i + (d[0] * 3)][j + (d[1] * 3)] == 'k' and \
                              S[i + (d[0] * 4)][j + (d[1] * 4)] == 'e':
                    for k in range(5):
                        print(f"{i+1+(d[0] * k)} {j+1+(d[1] * k)}")
                    exit()