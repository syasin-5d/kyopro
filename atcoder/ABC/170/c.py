X, N = map(int, input().split())

if N > 0:
    p = set(map(int, input().split()))
else:
    print(X)
    exit()

if X not in p:
    print(X)
    exit()

i = 0

while True:
    if X-i not in p:
        print(X-i)
        exit()
    elif X+i not in p:
        print(X+i)
        exit()
    i += 1

