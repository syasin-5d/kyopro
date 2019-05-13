from itertools import accumulate

N = int(input())
S = input()
L = list()
for s in S:
    if s == '.':
        L.append(0)
    else:
        L.append(1)

sharp_cumsum = [0] + list(accumulate(L))
period_cumsum = ([0] + list(accumulate([x^1 for x in L[::-1]])))[::-1]

ans = 10 ** 9

for i in range(N):
    left = i
    right = i+1
    tmp_ans = sharp_cumsum[left] + period_cumsum[right]
    ans = tmp_ans if tmp_ans < ans else ans
print(ans)
