H, W = map(int, input().split())
S = [input() for _ in range(H)]

# (0: 下)、(1: 右)、(2: 上)、(3: 左)、(4: 右下)、(5: 右上)、(6: 左上)、(7: 左下)
"""
0 0 0
0 # 0
0 0 0

# の座標が(1, 1)の場合
"""

DX = [1, 0, -1, 0, 1, 1, -1, -1]
DY = [0, 1, 0, -1, 1, -1, -1, 1]

# 答えを表す2次元配列を用意する
# result = [[0 if v == '.' else '#' for v in row] for row in S]
result = [[0 for _ in range(W)] for _ in range(H)]
# print(result) # [[0, 0, 0, 0, 0], [0, '#', 0, '#', 0], [0, 0, 0, 0, 0]]

for i in range(H):
    for j in range(W):
        # . 以外のマスはそのままにする
        if S[i][j] != '.':

            # '.'以外のマスはresultで'#'に置き換える
            result[i][j] = '#'

            # for文から続ける
            continue

        # 周囲にある8マスの'#'の個数を数える
        for dx, dy in zip(DX, DY):
            
            # (i, j)の周囲のマスを(ni, nj)と表す
            ni, nj = i + dx, j + dy

            # (i, j)が盤面の外、すなわち縦*横の枠内に入っていない場合
            if ni < 0 or ni >= H or nj < 0 or nj >= W:
                continue

            # '#'であれば1増やす
            if S[ni][nj] == '#':
                result[i][j] += 1

for row in result:
    print(''.join(map(str, row)))