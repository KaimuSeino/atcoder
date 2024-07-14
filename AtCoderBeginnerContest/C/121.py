N, M = map(int, input().split())

drink_list = []

for _ in range(N):
    price, num = map(int, input().split())

    drink_list.append([price, num])

drink_list.sort(reverse=False)


money = 0

for price, num in drink_list:
    for _ in range(num):
        if M == 0:
            break
        else:
            money += price
            M -= 1
        

print(money)

