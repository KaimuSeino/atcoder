# 入力の読み込み
N = int(input())
A = list(map(int, input().split()))

# 全体の合計の10分の1を計算
total_sum = sum(A)

# もし全体の合計を10で割ったあまりが0以外だった場合
if total_sum % 10 != 0:

    # Noを出力
    print("No")

    # 実行を終了する
    exit()

# total_sumを10で割った整数値を変数に代入
target = total_sum // 10

# ケーキは円形なので、配列を2倍にして連続部分和をチェック
A = A * 2
"""
例えば
[1, 9, 1, 9]の配列を2倍すると[1, 9, 1, 9, 1, 9, 1, 9]
"""

# しゃくとり法を用いて連続部分和をチェック
# しゃくとり法の参考動画：https://www.youtube.com/watch?v=aqncsLxYt8s
current_sum = 0
left = 0

"""
ピン    インデックス
left = 0
right = 0
[1, 9, 1, 9, 1, 9, 1, 9]

"""
# ケーキをrightが２周するという意味
for right in range(2 * N):

    # ケーキの大きさを代入
    current_sum += A[right]
    
    # 現在のケーキの大きさがケーキ全体の10分の1より大きい場合
    while current_sum > target and left <= right:

        # 現在のケーキの大きさからleftの位置のケーキの大きさを引く
        current_sum -= A[left]

        # leftの位置を一つプラスする
        left += 1
    
    # ケーキの大きさが全体の10分の1と一緒になった場合
    if current_sum == target:

        # Yesを出力
        print("Yes")

        # プログラムを終了する
        exit()

print("No")

