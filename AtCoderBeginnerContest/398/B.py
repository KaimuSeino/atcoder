A_list = list(map(int, input().split()))

count_list = [0] * 14

for card in A_list:
    count_list[card] += 1

is_fullhouse = False

for i in range(1, 14):
    if count_list[i] >= 3:
        for j in range(1, 14):
            if i != j and count_list[j] >= 2:
                is_fullhouse = True
                break
        if is_fullhouse:
            break

print('Yes' if is_fullhouse else 'No')