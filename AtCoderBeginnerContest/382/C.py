N, M = map(int, input().split())
A_i = list(map(int, input().split()))
B_j = list(map(int, input().split()))

def find_first(min_A_i, B):
    low = 0
    high = len(min_A_i) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if min_A_i[mid] <= B:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

min_A_i = []
current_min = 2 ** 30 
for a in A_i:
    current_min = min(current_min, a)
    min_A_i.append(current_min)

result = []
for B in B_j:
    index = find_first(min_A_i, B)
    if index == -1:
        result.append(-1)
    else:
        result.append(index + 1)

for num in result:
    print(num)