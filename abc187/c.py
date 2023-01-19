import sys
sys.setrecursionlimit(10**7) # 再起回数の設定
N = int(input())
strs = [input() for i in range(N)]

withExcSet = set()

for s in strs:
    if s[0] != "!":
        withExcSet.add("!" + s)
    elif s in withExcSet:
        print(s[1:])
        exit()

for s in reversed(strs):
    if s in withExcSet:
        print(s[1:])
        exit()

print("satisfiable")