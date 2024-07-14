N = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        # 入力値と一致する掛け算の組み合わせをさがず
        if i * j == N:
            print('Yes')
            exit()

print('No')