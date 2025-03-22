N = 4
P = [4, 3, 2, 1]
Q = [2, 3, 1, 4]

init_array = [0] * (N + 1)
for i in range(N):
    init_array[Q[i]] = i

result = []

for i in range(1, N + 1):
    j = init_array[i]

    result.append(Q[P[j] - 1])

print(" ".join(map(str, result)))