a_1, a_2, a_3 = map(int, input().split())

if a_1 == a_2 * a_3 or a_2 == a_1 * a_3 or a_3 == a_1 * a_2:
  print("Yes")
else:
  print("No")