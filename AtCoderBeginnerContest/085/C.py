N, Y = 2000, 20000000
is_ok = False

# for x in range(N + 1):
#     for y in range(N + 1 - x):
#         z = N - x - y
#         total = 10000 * x + 5000 * y + 1000 * z
#         if total == Y:
#             print(f"{x} {y} {z}")
#             is_ok = True
#             break
#     if is_ok:
#         break

for x in range(N + 1):
    for y in range(N + 1 - x):
        z = N - x - y
        total = 10000 * x + 5000 * y + 1000 * z
        if total == Y:
            print(f"{x} {y} {z}")
            is_ok = True
            break
    if is_ok:
        break

if not is_ok:
    print('-1 -1 -1')
