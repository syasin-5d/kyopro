from collections import deque

N,M = map(int, input().split())
ways = [[] for _ in range(N+1)]

for i in range(M):
    a,b = map(lambda x: int(x), input().split())
    ways[a].append(b)
    ways[b].append(a)

dq = deque([1])
sign = [None] * (N+1)
sign[0] = 0
sign[1] = 0

while(dq):
    now = dq.popleft()
    for w in ways[now]:
        if not sign[w]:
            sign[w] = now
            dq.append(w)

if None in sign:
    print("No")
else:
    print("Yes")
    for i in range(2, N+1):
        print(sign[i])
