N, K = map(int, input().split())

h_list = []

for _ in range(N):
    h = int(input())
    h_list.append(h)

h_list.sort(reverse=True)

h_min_list = []

for i in range(N - K + 1):
    h_min = h_list[i] - h_list[i + K - 1]

    h_min_list.append(h_min)

print(min(h_min_list))