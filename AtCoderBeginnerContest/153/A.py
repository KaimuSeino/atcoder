H, A = map(int, input().split())

counter = 0
while H > 0:
    H -= A
    counter += 1

print(counter)