s = input()
t = input()

s_list = list(s)
t_list = list(t)

s_list.sort(reverse=False)
t_list.sort(reverse=True)

s = ''.join(s_list)
t = ''.join(t_list)

ans_list = []

ans_list.append(s)
ans_list.append(t)

ans_list.sort()

if ans_list[0] == s and ans_list[0] != ans_list[1]:
    print('Yes')
else:
    print('No')