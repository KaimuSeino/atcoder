N, M = map(int, input().split())

# 市の情報を格納するための変数を定義
cities = []

# 入力から市の情報を変数に代入する
for _ in range(M):

    # lineから県と市ができた年数を取得
    pref, year = map(int, input().split())

    # 配列に県と市ができた年数を追加する
    cities.append((pref, year))

# 市の情報を誕生年でソート
# sortedとsortの違いを理解している？
sorted_cities = sorted(cities, key=lambda x: x[1])

# 県ごとのカウンターを記録する辞書を作成
pref_counter = {}

# 市の情報が入った配列から県と設立年を取得
for pref, year in cities:

    # pref_counterの辞書に県の番号が登録されていない場合
    if pref not in pref_counter:

        # pref_counterを登録する
        pref_counter[pref] = 0

# 識別番号を生成する
city_id_map = {}

# ソートされた市の情報から識別番号を生成する
for pref, year in sorted_cities:

    # 県ごとのカウンターを1増やす
    pref_counter[pref] += 1

    # 識別番号を生成
    # 上6桁は県番号、下6桁は県内での誕生順
    city_id = f'{pref:06}{pref_counter[pref]:06}'

    # 識別番号を辞書に保存
    city_id_map[(pref, year)] = city_id

# 各市の元の順序に従って識別番号を出力
for pref, year in cities:

    # 保存された識別番号を出力
    print(city_id_map[((pref, year))])