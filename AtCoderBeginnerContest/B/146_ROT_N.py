N = int(input())
S = input()

ans = ''

# Nが0の場合は文字列の変化はなし
if N == 0:
    print(S)
else:
    for s in S:
        # 文字をunicodeに変換しNを足す
        unicode = ord(s) + N

        # unicodeが'Z'よりも大きい場合
        if unicode > ord('Z'):

            # unicodeを-26すると'A'のunicodeに戻る
            unicode -= 26
        
        # 文字列を追加していく
        ans += chr(unicode)
    
    print(ans)
