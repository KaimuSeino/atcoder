N, c_1, c_2 = map(str, input().split())
N = int(N)
S = input()

result = []

for s in S:
  if s != c_1:
    result.append(c_2)
  else:
    result.append(c_1)

print(' '.join(result))
