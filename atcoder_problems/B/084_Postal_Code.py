A, B = map(int, input().split())
S = input()

# 郵便番号の形式かどうかを確認するための関数
def isPostalCode(S, A, B):

    # SのA番目の要素が-でない場合
    if S[A] != "-":
        return False
    
    # 郵便番号の長さが条件に当てはまっているか
    if len(S) != A + B + 1:
        return False
    
    # Aが全て0~9までの数字 かつ Bが全て0~9までの数字
    return all(map(str.isdigit, S[:A])) and all(map(str.isdigit, S[A+1:]))

# 出力
print('Yes' if isPostalCode(S, A, B) else 'No')