import sys

S = input()
T = input()

for i, s in enumerate(S):
    if (s != T[i]):
        print("No")
        sys.exit()

if (len(S) + 1 != len(T)):
    print(len(S))
    print(len(T) + 1)
    print("No")
    sys.exit()

print("Yes")