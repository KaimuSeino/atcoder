N = int(input())
A_list = list(map(int, input().split()))

a_0 = A_list[0]
a_1 = A_list[1]

r = a_1 / a_0

def is_geometric_progression(A_list, r):
  for i in range(1, len(A_list)):
    if A_list[i] != A_list[i-1] * r:
      return False
  return True

if is_geometric_progression(A_list, r):
  print("Yes")
else:
  print("No")
