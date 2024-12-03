N, D = map(int, input().split())
S = list(input())


for i in range(N):
    if S[i] == '@':
        S[i] = '.'
        D -= 1
    
    if D == 0:
        break

print(S.count('.'))
