N, M = map(int, input().split())

x = 1
current = 1

for i in range(1, M+1):
  current *= N
  x += current
  
if x > 10**9:
  print('inf')
else:
    print(x)
