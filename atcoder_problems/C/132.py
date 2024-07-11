N = int(input()) # Nは偶数
d_list = list(map(int, input().split()))

# リストを小さい順にする
d_list.sort(reverse=False)

# リストを半分に分割した時の N / 2と N / 2 - 1の値が同じである場合
if d_list[int(N / 2)] == d_list[int(N / 2 - 1)]:
    print(0)
else:
    print(d_list[int(N / 2)] - d_list[int(N / 2 - 1)])