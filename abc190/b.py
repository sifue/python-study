import sys
N, S, D = map(int, input().split())
magics = [list(map(int, input().split())) for i in range(N)]
for magic in magics:
    if (magic[0] < S and magic[1] > D):
        print("Yes")
        exit()
print("No")
