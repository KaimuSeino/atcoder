N = int(input())

result = []

if N % 2 == 0:
  mid1 = (N // 2) - 1
  mid2 = (N // 2)
  
  result = ['-'] * N
  result[mid1] = '='
  result[mid2] = '='
else:
  mid = N // 2
  result = ['-'] * N
  result[mid] = '='

print(''.join(result))
