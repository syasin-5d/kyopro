import math

A,B = map(int, input().split())
ans = 0

a = math.ceil(math.log2(A))
b = math.floor(math.log2(B))


if A >= 4:
    for i in range(A,2**a):
        ans ^= i
else:
    for i in range(A,4):
        ans ^= i

for i in range(2**b, B+1):
    ans ^= i

print(ans)
