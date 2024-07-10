N = int(input())
num_list = list(map(int, input().split()))

ans_list = []

for i in range(N):
    ans_list.append(int(i + 1))

num_list.sort(reverse=False)

if ans_list == num_list:
    print('Yes')
else:
    print('No')