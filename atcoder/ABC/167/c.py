from pprint import pprint

N, M, X = map(int, input().split())

items = []
best_m_item = {}
sum_costs = 0
exp = [0] * M
mastered = [False] * M
bought = 0

for i in range(N):
    items.append([i] + list(map(int, input().split())))

for m in range(M):
    best_m_item[m] = sorted(items, key=lambda x: (x[m+2], x[1]), reverse=True)


used = set()

while bought < N:
    if all(mastered):
        break
    for m in range(M):
        if mastered[m]:
            continue
        i, cost, *books = best_m_item[m].pop(m)
        bought += 1
        if i in used:
            continue
        used.add(i)
        sum_costs += cost
        for l in range(M):
            exp[l] += books[l]
            if exp[l] >= X:
                mastered[l] = True
        print(sum_costs)
        pprint(used)
        print(exp)
        if all(mastered):
            break
        


if all(mastered):
    print(sum_costs)
else:
    print(exp)
    print(-1)
