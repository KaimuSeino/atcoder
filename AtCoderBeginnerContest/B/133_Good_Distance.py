import math

N, D = map(int, input().split())

distance_list = [input().split() for _ in range(N)]

counter = 0

for i in range(N):
    for j in range(i + 1, N):
        distance_squared = sum((distance_list[i][k] - distance_list[j][k]) ** 2 for k in range(D))
        distance = math.sqrt(distance_squared)

        if distance.is_integer():
            counter += 1
    

print(counter)