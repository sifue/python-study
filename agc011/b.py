import numpy as np
N = int, input()
creatures = list(map(int, input().split()))
single_winner_count = 0

# その生き物が最後まで吸収し切れるかチェックしていく
for i, creature in enumerate(creatures):
    current_size = creature
    target_creatures = np.array(creatures)
    target_creatures = np.delete(target_creatures, i) # 自分を削除
    target_creatures = np.sort(target_creatures) # 小さいやつから吸収していく

    while (np.size(target_creatures) > 0):
        target = target_creatures[0]
        if (target <= (current_size * 2)): # もし吸収できるなら
            current_size += target
            target_creatures = np.delete(target_creatures, 0)
        else:
            break # これ以上吸収できないなら終了

    if (np.size(target_creatures) == 0): # 対象を全部吸収できていたら
        single_winner_count += 1 #色をカウント

print(single_winner_count)
