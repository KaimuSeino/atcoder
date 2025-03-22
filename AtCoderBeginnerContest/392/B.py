N, M = map(int, input().split())
A = list(map(int, input().split()))

array = []

for i in range(1, N+1):
  if i not in A:
    array.append(i)


print(len(array))
print(" ".join(map(str, array)))