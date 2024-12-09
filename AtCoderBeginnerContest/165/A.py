K = int(input())
A, B = map(int, input().split())

result = False

for i in range(A, B + 1):

    if i % K == 0:
        result = True

if result:
    print("OK")
else:
    print("NG")
