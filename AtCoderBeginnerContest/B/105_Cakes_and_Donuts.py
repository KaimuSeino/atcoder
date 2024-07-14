N = int(input())

for i in range(0, 100 // 4):
    for j in range(0, 100 // 7):
        
        if 4 * i + 7 * j == N:
            print('Yes')
            exit()

print('No')