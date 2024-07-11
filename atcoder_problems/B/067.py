N, K = map(int, input().split())
L_list = list(map(int, input().split()))

# 大きい順に並べる
L_list.sort(reverse=True)

# 長さを保存する
length = 0

# 長い順の棒を三つ足す
for i in range(K):
    length += L_list[i]

print(length)