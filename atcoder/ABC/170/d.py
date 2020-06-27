N = int(input())
A = list(map(int, input().split()))
cnt = 0
ans = 0

factor = []
B = []
duplicated = set()

for a in sorted(A):
    for f in factor:
        if a == f:
            duplicated.add(a)
        if a % f != 0:
            continue
        else:
            break
    else:
        factor.append(a)


# for i in range(len(factor)):
#     for j in range(len(factor)):
#         if i == j:
#             continue
#         if A[i] % A[j] != 0:
#             cnt += 1
#     if cnt == N - 1:
#         ans += 1
#     cnt = 0

print(len(factor) - len(duplicated))
