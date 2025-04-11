from math import isqrt, log2

N = int(input())

def countSquares(x):
    s = isqrt(x)
    return (s + 1) // 2

maxVal = int(log2(N))
ans = 0

for v in range(1, maxVal + 1):
    L = (N // (2 ** (v + 1))) + 1
    R = N // (2 ** v)

    cnt = countSquares(R) - countSquares(L - 1)
    ans += v * cnt


print(ans)
