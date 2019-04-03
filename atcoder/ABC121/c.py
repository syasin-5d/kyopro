N,M = map(int, input().split())
shop = list()
price = 0
item = 0
for i in range(N):
    shop.append(list(map(int, input().split())))
shop.sort()

for i in range(N):
    for _ in range(shop[i][1]):
        if(item >= M):
            break
        price += shop[i][0]
        item += 1

print(price)
