N, M = 3, 23

# # A_1が良い条件は (1 <= A_1 <= M - 10(N - 1))
# A_1 = M - 10 * (N - 1)
# ans: 3
# よってA_Nは (1, 2, 3)の場合分け

# (2 <= i <= N) の条件がある。
# A_i の範囲は (A_(i - 1) + 10 <= A_i <= M - 10(N - i)) となる。

# i = 2 のとき A_2の範囲は
# A

ans = []

def dfs(v):
    sz = len(v)
    if sz == N:
        ans.append(v.copy())
        return
    # 次の要素の開始値
    start = 0
    if sz == 0:
        start = 1
    else:
        start = v[-1] + 10
    
    # 次の要素の終了値
    end = M - 10 * (N - sz - 1)

    for i in range(start, end + 1):
        v.append(i)
        dfs(v)
        v.pop()

dfs([])

for row in ans:
    print(' '.join(map(str, row)))