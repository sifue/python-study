import numpy as np
N = int(input())
creatures = list(map(int, input().split()))
creatures.sort()

single_winner_count = 0
current_size = 0
for i in range(N - 1):
    current_size += creatures[i]
    if (creatures[i + 1] <= (current_size * 2)):
        single_winner_count += 1
    else:
        single_winner_count = 0

single_winner_count += 1 # 最大数のものは必ず生き残るので足す1

print(single_winner_count)
