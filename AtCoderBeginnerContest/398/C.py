N = int(input())
A_list = list(map(int, input().split()))

count_dic = {}
for num in A_list:
  if num in count_dic:
    count_dic[num] += 1
  else:
    count_dic[num] = 1

max_num = 0
max_person = 0

for idx, num in enumerate(A_list):
  if count_dic[num] == 1 and num > max_num:
    max_num = num
    max_person = idx + 1

print(max_person)