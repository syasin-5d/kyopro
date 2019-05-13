N,A,B,C = map(int,input().split())

bumboos = [int(input()) for _ in range(N)]

INF = 10 ** 9

def dfs(cur, a, b, c):
    if cur == N:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a,b,c) > 0 else INF
    ret0 = dfs(cur + 1, a, b, c)
    ret1 = dfs(cur + 1, a+bumboos[cur], b, c) + 10
    ret2 = dfs(cur + 1, a, b+bumboos[cur], c) + 10
    ret3 = dfs(cur + 1, a, b, c+bumboos[cur]) + 10
    return min(ret0, ret1, ret2, ret3)

print(dfs(0,0,0,0))


"""
1, 2, 3, 4, 5, 6  7, 8
A  A  A  A  A  A  A  A
B  B  B  B  B  B  B  B
C  C  C  C  C  C  C  C
X  X  X  X  X  X  X  X

example
5 100 90 80
98
40
30
21
80

1. dfs(0,0,0,0)
  ret0 = dfs(1,0,0,0) + 10
  ret1 = dfs(1,98,0,0) + 10 <- will be chosen
  ret2 = dfs(1,0,98,0) + 10
  ret3 = dfs(1,0,0,98) + 10

2. dfs(1,98,0,0)
  ret0 = dfs(2,98,0,0) + 10
  ret1 = dfs(2,138,0,0) + 10
  ret2 = dfs(2,98,40,0) + 10 <- will be chosen
  ret3 = dfs(2,98,0,40) + 10

3. dfs(2,98,40,0)
  ret0 = dfs(3,98,40,0) + 10
  ret1 = dfs(3,128,40,0) + 10
  ret2 = dfs(3,98,70,0) + 10 <- will be chosen
  ret3 = dfs(3,98,40,30) + 10

4. dfs(3,98,70,0)
  ret0 = dfs(4,98,70,0) + 10
  ret1 = dfs(4,119,70,0) + 10
  ret2 = dfs(4,98,91,0) + 10 <- will be chosen
  ret3 = dfs(4,98,70,21) + 10

5. dfs(4,98,91,0)
  ret0 = dfs(5,98,91,0) + 10
  ret1 = dfs(5,178,91,0) + 10
  ret2 = dfs(5,98,171,0) + 10
  ret3 = dfs(5,98,91,80) + 10 <- will be chosen

6. dfs(5,98,91,80)
  return abs(98 - 100) + abs(91 - 90) + abs(80 - 80) - 30 if min(98,91,80) > 0 else INF
equals
  return 2 + 1 + 0 - 30
equals
  return -27

then,

5. dfs(4,98,91,0)
  ret3 = -27 + 10
  it returns -17

4. dfs(3,98,70,0)
  ret2 = -17 + 10
  it returns -7

3. dfs(2,98,40,0)
  ret2 = -7 + 10
  it returns 3

2. dfs(1,98,0,0)
  ret2 = 3 + 10
  it returns 13

1. dfs(0,0,0,0)
  ret1 = 13 + 10
  it returns 23

therefore, the answer is 23.
"""
