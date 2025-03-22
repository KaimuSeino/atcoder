s1, s2 = map(str, input().split())

# 1の場合
if (s1 == "sick" and s2 == 'sick'):
  print(1)

# 2の場合
if (s1 == "sick" and s2 == 'fine'):
  print(2)

# 3の場合
if (s1 == "fine" and s2 == 'sick'):
  print(3)

# 4の場合
if (s1 == "fine" and s2 == 'fine'):
  print(4)