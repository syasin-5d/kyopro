import sys

N = int(input())
A = list(map(int, input().split()))

ans = 1

for a in A:
    if a == 0:
        print(0)
        sys.exit()

for a in sorted(A, reverse=True):
    ans *= a
    if 10**18 < ans:
        print(-1)
        sys.exit()


print(ans)
