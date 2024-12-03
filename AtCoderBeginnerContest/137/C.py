from collections import defaultdict

N = int(input())

s = [input() for _ in range(N)]


s_num_list = []
for i in range(N):
    num = defaultdict(int)
    for j in s[i]:
        num[j] += 1
    s_num_list.append(tuple(sorted(num.items())))

freq_s_num = defaultdict(int)
for s in s_num_list:
    freq_s_num[s] += 1

count = 0
for num in freq_s_num.values():
    count += (num * (num - 1)) // 2

print(count)