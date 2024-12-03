N, D = map(int, input().split())
S = list(input())

for i in range(-1, -(N + 1), -1):
    if S[i] == '@':
        S[i] = '.'
        D -= 1
    
    if D == 0:
        break

print(''.join(S))