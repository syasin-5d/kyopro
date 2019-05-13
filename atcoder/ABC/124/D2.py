from itertools import accumulate

N,K = map(int, input().split())
S = list(map(int,input()))

cnt = 0
now = 1

nums = list()

for s in S:
    if s == now:
        cnt += 1
    else:
        nums.append(cnt)
        cnt = 1
        now = 1 - now

nums.append(cnt)

if len(nums) % 2 == 0:
    nums.append(0)

cumsum = accumulate(nums)

Add = 2 * K + 1

ans = 0

for i in range(0,len(nums),2):
    left = i
    right = i + Add
    ans = max(ans, cumsum[right] - cumsum[left])

print(ans)
