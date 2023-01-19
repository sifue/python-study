import sys
sys.setrecursionlimit(10**7) # 再起回数の設定
N = int(input())
points = [list(map(int, input().split())) for i in range(N)]
result = 0

for i in points:
    for j in points:
        if (i[0] - j[0]) != 0:
            g = (i[1] - j[1]) / (i[0] - j[0])
            if g >= -1 and g <= 1:
                result += 1
print(result // 2)
