N,M,C = map(int, input().split())
A = list()
B = list(map(int, input().split()))
cnt = 0

for n in range(N):
    A.append(list())
    A[n] = list(map(int, input().split()))

for n in range(N):
    ans = 0
    for i in range(len(A[n])):
        ans += A[n][i] * B[i]
    ans += C
    if ans > 0:
        cnt += 1
print(cnt)
