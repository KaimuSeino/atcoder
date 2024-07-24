N, T, P = map(int, input().split())
L_list = list(map(int, input().split()))

L_list.sort(reverse=True)

if T - L_list[P - 1] < 0:
    print(0)
else:
    print(T - L_list[P - 1])