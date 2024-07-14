O = input()
E = input()

O_len = len(O)
E_len = len(E)

ans = ''

for i in range(O_len - 1):
    O_str = O[i]
    E_str = E[i]
    
    ans += O_str + E_str

if O_len == E_len:
    ans += O[O_len - 1] + E[E_len - 1]
else:
    ans += O[O_len - 1]

print(ans)