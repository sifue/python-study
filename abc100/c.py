import numpy as np
N = int(input())
ary = list(map(int, input().split()))
nums = np.array(ary)

def count_can_divide2(num):
    count = 0
    while (num % 2 == 0):
        num = num // 2
        count += 1
    return count
count_can_divide2_v = np.vectorize(count_can_divide2)

result = np.sum(count_can_divide2_v(nums))
print(result)