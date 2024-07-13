S = input()

# 判定するための関数を作成する
def isAC(S):

    # Sの先頭が"A"でない場合
    if S[0] != "A":
        return False
    
    # Sの先頭の2文字と末尾の1文字を除いた"C"の個数を調べる
    if S[2:-1].count("C") != 1:
        return False
    
    # Sに含まれる大文字の個数を調べる
    if sum(map(str.isupper, S)) != 2:
        return False
    
    # 全ての条件を満たした場合
    return True

print("AC" if isAC(S) else "WA")