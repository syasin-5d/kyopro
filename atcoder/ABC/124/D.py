from itertools import accumulate
N,K = map(int, input().split())
S = list(map(int, input()))

groups = list()
now = 1
cnt = 0

for s in S:
    if s == now:
        cnt += 1
    else:
        groups.append(cnt)
        now ^= 1
        cnt = 1

groups.append(cnt)

if len(groups) % 2 == 0:
    groups.append(0)

cumsum = [0] + list(accumulate(groups))

Add = 2 * K + 1

ans = 0

for i in range(0,len(groups), 2):
    left = i
    right = min(i + Add, len(groups))
    tmp = cumsum[right] - cumsum[left]

    ans = max(tmp,ans)

print(ans)
