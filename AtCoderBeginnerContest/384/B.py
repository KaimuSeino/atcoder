N, R = 4, 1255
D_list = [2, 1, 2, 1]
A_list = [900, 521, 600, 52]

for i in range(N):
    d = D_list[i]
    a = A_list[i]

    if d == 1:
        if 1600 <= R <= 2799:
            R += a
    else:
        if 1200 <= R <= 2399:
            R += a

print(R)