S = input()
for i, c in enumerate(S):
    if i > 0 and S[i - 1] == "A" and c == "C":
        print("Yes")
        exit()
print("No")