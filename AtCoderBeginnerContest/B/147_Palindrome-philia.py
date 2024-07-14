S = input()

# 入力された文字列を逆順にする
palindrome_S = S[::-1]

# バグのカウント
bug_counter = 0

for i in range(len(S)):
    if S[i] != palindrome_S[i]:
        bug_counter += 1

print(int(bug_counter / 2))
