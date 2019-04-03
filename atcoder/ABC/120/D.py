def root(par: list, x: int) -> int:
    if par[x] < 0:
        return x # root
    else:
        par[x] = root(par, par[x])
        return par[x]


def same(par:list, x: int, y: int) -> bool:
    return root(par, x) == root(par, y)


def unite(par:list, x: int, y: int):
    x = root(par, x)
    y = root(par, y)
    # do nothing because already connected
    if x == y:
        return

    # want to connect y(smaller) to x(bigger)
    if size(par, x) < size(par, y):
        x,y = y,x

    # update size of x
    par[x] += par[y]
    # change parent of y to x
    par[y] = x

def size(par:list, x:int) -> int:
    return -par[root(par, x)]

N,M = map(int, input().split())
# store the parent number if not it's parent, else -(size of the union).
par = [-1 for _ in range(N)]

ans = [0] * M
ans[M-1] = N*(N-1) / 2

distructions = list(tuple())

for _ in range(M):
    distructions.append(tuple(map(lambda x: int(x) - 1, input().split())))

for i in range(M-1, 0, -1):
    x,y = distructions[i]

    if not same(par,x,y):
        ans[i-1] = ans[i] - size(par, x) * size(par, y)
        unite(par,x,y)
    else:
        ans[i-1] = ans[i]

for i in range(M):
    print(int(ans[i]))
