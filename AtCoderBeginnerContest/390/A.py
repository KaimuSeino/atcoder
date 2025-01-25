A_list = list(map(int, input().split()))

def one_sort_check(A_list):
  
  sorted_A = [1, 2, 3, 4, 5]
  
  if A_list == sorted_A:
    return False
  
  for i in range(len(A_list) - 1):
    A_list_copy = A_list[:]
    A_list_copy[i], A_list_copy[i+1] = A_list_copy[i+1],  A_list_copy[i]
    if A_list_copy == sorted_A:
      return True

  return False  

if one_sort_check(A_list):
  print("Yes")
else:
  print("No")

