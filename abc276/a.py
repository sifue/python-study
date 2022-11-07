# 英小文字からなる文字列 S が与えられます。
# S に a が現れるならば最後に現れるのが何文字目かを出力し、現れないならば −1 を出力してください。
# 制約
# S は英小文字からなる長さ 1 以上 100 以下の文字列
import sys
sys.setrecursionlimit(10**7) # 再起回数の設定
S = input()
for i in range(len(S) - 1, -1, -1):
    if (S[i] == 'a'):
        print(i + 1)
        exit()
print(-1)