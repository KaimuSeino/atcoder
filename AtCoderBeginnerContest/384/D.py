N, S = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)
S %= total

A = A + A

prefix_sum = set()
prefix_sum.add(0)
p = 0
for a in A:
    p += a
    prefix_sum.add(p)

result = 'No'
for val in prefix_sum:
    if (val + S) in prefix_sum:
        result = 'Yes'
        break

print(result)
