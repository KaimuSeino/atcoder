N, M = 10, 5
A_i = 60, 83, 76, 45, 70, 91, 37, 58, 94, 22
B_j = 70, 39, 52, 33, 18

# 定数の定義
K = 200

# 配列idを初期化
id = [-1] * K
r = K

# 前処理: 各a_iに対してid[r]を設定
for i in range(N):
    # a = 60
    a = A_i[i]
    # 100 > 60
    while r > a:
        # r = 99
        r -= 1
        # 99 < 100
        if r < K:

            id[r] = i + 1 # インデックスは1-based
        else:
            break

for b in B_j:
    print(id[b])