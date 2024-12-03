N = 5
S = '/////'

has_single_slash = S.count('/') == 1

# 奇数である場合
if N % 2 != 0 and has_single_slash:
    pattern = S.split('/')

    # 1のstringを取得
    left = pattern[0]
    # 2のstringを取得
    right = pattern[1]

    is_length_equal = len(left) == len(right)
    is_only_1_and_2 = left.count('1') == len(left) and right.count('2') == len(right)

    if (is_length_equal & is_only_1_and_2):
        print('Yes')
    else:
        print('No')
else:
    # 奇数でない場合はNo
    print('No')