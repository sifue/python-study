import sys
args = input().split()
A = int(args[0])
B = int(args[1])
C = int(args[2])
K = int(args[3])

if (A >= K):
    print(K)
    sys.exit()

if (A + B >= K):
    print(A)
    sys.exit()

print(A - (K - (A + B)))