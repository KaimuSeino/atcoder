N = int(input())
A_list = list(map(int, input().split()))

# 操作回数
counter = 0

# 操作が行えなくなるまで操作を行う
while True:

    # 操作が行えるかどうかを判断すための変数
    can_do = True

    # 各要素が2で割れるかどうかを確認
    for i in range(N):

        # A_listのi番目の要素が奇数であるか確認する
        if A_list[i] % 2 == 1:

            # 奇数が見つかった場合は、これ以上操作を行えない
            can_do = False
    
    # 奇数が見つかった場合は、反復を打ち切る
    if not can_do:
        break

    # 操作を行うことができる場合は、操作を行う
    for i in range(N):

        # A_listのi番目の要素を2で割った正の整数を再び代入する
        A_list[i] //= 2
    
    # 操作回数を１増やす
    counter += 1

# 出力
print(counter)