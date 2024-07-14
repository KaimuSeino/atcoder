S = input()

def isEvenStr(s):
    # 文字列の長さが奇数だった場合
    if len(s) % 2 != 0:
        return False
    
    # 文字列を半分ずつに分ける
    half_length = len(s) // 2
    left_str = s[:half_length]
    right_str = s[half_length:]

    # 半分に分けた文字列が一致しているかどうかを確認
    return left_str == right_str

def findEvenStr(s):
    length = len(s)
    for i in range(length - 1, 0, -1):

        # 偶文字列であるかどうかを確認する
        if isEvenStr(S[:i]):
            return i

print(findEvenStr(S))