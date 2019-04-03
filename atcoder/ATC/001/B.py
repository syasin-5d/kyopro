def root(par: list, x: int) -> int:
    if par[x] == x:
        return x # root
    else:
        par[x] = root(par, par[x])
        return par[x]


def same(x: int, y: int) -> bool:
    return root(par, x) == root(par, y)


def unite(par:list, x: int, y: int):
    x = root(par, x)
    y = root(par, y)
    if x == y:
        return
    par[x] = y


N,Q = map(int, input().split())
par = [_ for _ in range(N)]
for _ in range(Q):
    P,A,B = map(int, input().split())
    if P == 0:
        unite(par, A, B)
    elif P == 1:
        if same(A, B):
            print("Yes")
        else:
            print("No")
