N, K = map(int, input().split())
L_list = list(map(int, input().split()))

L_list.sort(reverse=True)

length = 0

for i in range(K):
    length += L_list[i]

print(length)