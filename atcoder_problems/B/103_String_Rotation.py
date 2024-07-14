S = list(input())
T = list(input())

length = len(S)

for x in range(length + 1):
  last_str = S.pop()
  S.insert(0, last_str)
  if S == T:
    print("Yes")
    exit()

print("No")

