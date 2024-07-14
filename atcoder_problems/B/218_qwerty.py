P_list = list(map(int, input().split()))

# 回答を保存
ans_str = ''

for p in P_list:

    # p + 96をすることで p = 1の場合は 'a' のunicodeとなる
    unicode = p + 96

    # chr関数でunicodeを文字列に変換する
    ans_str += chr(unicode)

print(ans_str)