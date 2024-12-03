S = 'zzzzzz'

if len(S) % 2 == 0:
    # Sは偶数である

    # 2つずつのペアの文字列の配列を作成
    pairs = []
    for i in range(0, len(S), 2):
        pairs.append(S[i:i+2])
    
    is_valid = True

    # ペアの2つの文字列が一致しているか？
    for pair in pairs:
        if pair[0] != pair[1]:
            is_valid = False
            break
    
    if not is_valid:
        print('No')
    else:
        # ペアの回数を確認する
        for i in range(len(pairs)):
            count = 0
            for j in range(len(pairs)):
                if pairs[i] == pairs[j]:
                    count += 1
            # i == jを無視する
            if count > 1:
                is_valid = False
                break

        if is_valid:
            print('Yes')
        else:
            print('No')
else:
    # Sは奇数である
    print('No')