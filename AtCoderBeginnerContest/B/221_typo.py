S = input()
T = input()

s_length = len(S)

# 最初から一致している場合
if S == T:
    print("Yes")
    exit()

for i in range(s_length - 1):
    s_list = list(S)
    s_list[i], s_list[i + 1] = s_list[i + 1] + s_list[i]
    s_swapped = ''.join(s_list)

    if s_swapped == T:
        print("Yes")
        exit()

print("No")