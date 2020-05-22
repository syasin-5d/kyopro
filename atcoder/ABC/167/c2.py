from itertools import combinations

N, M, X = map(int, input().split())

items = []
calced = []

min_cost = float('inf')

for _ in range(N):
    items.append(list(map(int, input().split())))

for i in range(N):
    for combo in combinations(items, i+1):
        cost = 0
        exp = [0] * M
        mastered = True
        for c in combo:
            cost += c[0]
            for m in range(0,M):
                exp[m] += c[m+1]
        for m in range(M):
            if exp[m] < X:
                mastered = False
        if mastered:
            min_cost = min(min_cost, cost)


if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)

