from fractions import gcd
from itertools import combinations
from functools import reduce

N = int(input())
A = map(int, input().split())
ans = 0
for a in combinations(A,N-1):
    tmp = reduce(gcd,a)
    ans = tmp if ans < tmp else ans

print(ans)
