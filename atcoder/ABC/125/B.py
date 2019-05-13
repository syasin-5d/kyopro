N = int(input())
V = map(int, input().split())
C = map(int, input().split())

ans = 0
for v,c in zip(V,C):
    expect = v-c
    if expect > 0:
        ans += expect

print(ans)
