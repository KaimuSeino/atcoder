# pythonでは回答不可

from itertools import combinations

N, P, Q = map(int, input().split())
A_list = list(map(int, input().split()))

counter = 0

for comb in combinations(A_list, 5):
    sum = 1
    for num in comb:
        sum *= num

    if sum % P == Q:
        counter += 1

print(counter)
