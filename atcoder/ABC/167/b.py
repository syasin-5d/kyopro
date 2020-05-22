A,B,C,K = map(int, input().split())

score = 0


if K <= A+B:
    score = min(A,K)
else:
    score = A - min(C, (K - (A+B)))


print(score)
