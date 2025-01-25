H, W = map(int, input().split())

board = [list(input()) for _ in range(H)]

a = H # `#`の左上端
b = -1 # `#`の右上端
c = W #　`#`の左下端
d = -1 # `#`の右下端

white_set = set()

question_count = 0

for i in range(H):
  for j in range(W):
    if board[i][j] == "#":
        a = min(a, i)
        b = max(b, i)
        c = min(c, j)
        d = max(d, j)
    elif board[i][j] == ".":
        white_set.add((i, j))
    else:
        question_count += 1

for white_i, white_j in white_set:
    if a <= white_i <= b and c <= white_j <= d:
        print("No")
        exit()

print("Yes")
