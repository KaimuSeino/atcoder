N, M = map(int, input().split())

counter = 0

uv_dic = {}

for _ in range(M):
  u, v = map(int, input().split())
  
  # uとvが同じなら削除する
  if u == v:
    counter += 1
  else:
    a, b = min(u, v), max(u, v)
    
    if (a, b) in uv_dic:
      uv_dic[(a, b)] += 1
    else:
      uv_dic[(a, b)] = 1

for count in uv_dic.values():
  if count > 1:
    counter += (count - 1)

print(counter)