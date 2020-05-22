N, K = map(int, input().split())

A = list(map(int,input().split()))

moved = {}
now_city = 1
next_city = A[0]
i=0

while i < N:
    moved[now_city] = i
    if next_city in moved:
        break
    now_city = next_city
    next_city = A[now_city-1]
    i += 1

# i 回目の試行で、now_city から next_city に移ろうとしている

mod = i - moved[next_city]

moved_list = [x for x in moved.keys()]

loop_list = moved_list[moved[next_city]:i+1]
loop = len(loop_list)

if K < moved[next_city]:
    print(moved_list[K])
else:
    print(loop_list[(K-moved[next_city])%loop])


# print(f"{next_city=} {i=}")
# print(f"{loop_list=}")
# print(f"{moved_list=}")
# print(f"{K-moved[next_city]=}")
# print(f"{loop=}")

# ans = 5
# 6 10
# 2 3 4 5 4 6
