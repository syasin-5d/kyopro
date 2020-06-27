import bisect

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

ans = 0

for b in B:
    n_lower_B = bisect.bisect_left(A, b)
    n_higher_B = N - bisect.bisect_right(C, b)
    ans += n_lower_B * n_higher_B

print(ans)
