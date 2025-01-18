Q = int(input())

snakes = []
first_snakes_index = 0
set_num = 0

for _ in range(Q):
    line = input().split()

    query = int(line[0])

    if query == 1:
        # タイプ１の場合
        l = int(line[1])
        if first_snakes_index == len(snakes):
            head = set_num
        else:
            # 最後の蛇を取得する
            last_head, last_len = snakes[-1]
            # 追加された蛇の最後の尾
            head = last_head + last_len
        
        snakes.append((head, l))
    elif query == 2:
        # タイプ２の場合
        # 先頭の蛇情報の取得
        first_head, first_len = snakes[first_snakes_index]
        first_snakes_index += 1
        # 抜けた蛇の長さ分をセットする
        set_num += first_len
    else:
        # タイプ３の場合
        k = int(line[1])
        # k番目の先頭の座標を取得
        head, _ = snakes[first_snakes_index + k -1]
        print(head - set_num)