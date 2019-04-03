N = int(input())

ans = 4 ** N - (4 ** (N-3) * (N-2)*3 + 4 ** (N-3)*2 - (N-2)*3)

print(ans)
