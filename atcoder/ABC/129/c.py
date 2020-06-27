N, M = map(int, input().split())
A = [int(input()) for _ in range(M)]
oks = [True] * (N + 1)
dp = [0] * (N + 1)
dp[0] = 1
mod = 10**9 + 7

for a in A:
    oks[a] = False

for now in range(N + 1):
    next1 = now + 1
    next2 = now + 2
    if N < next1:
        break
    if oks[next1]:
        dp[next1] += dp[now]
        dp[next1] %= mod

    if N < next2:
        break
    if oks[next2]:
        dp[next2] += dp[now]
        dp[next2] %= mod

print(dp[N])
