N = int(input())
H = list(map(int, input().split()))
ans = 0
max_height = 0
for hotel in H:
    if hotel >= max_height:
        ans += 1
        max_height = hotel
    else:
        pass

print(ans)
