import sys
sys.setrecursionlimit(500*500)
H,W = map(int, input().split())

maze = [input() for _ in range(H)]
reached = [[False]*W for _ in range(H)]

S = None
G = None

for x in range(W):
    for y in range(H):
        if maze[y][x] == 's':
            S = (x,y)
        if maze[y][x] == 'g':
            G = (x,y)
        if S and G:
            break
    if S and G:
        break

def dfs(x,y):
    if(x < 0 or W <= x or y < 0 or H <= y or maze[y][x] == '#'):
        return False
    if reached[y][x]:
        return False
    if (x,y) == G:
        return True
    reached[y][x] = True

    return dfs(x+1,y) or dfs(x-1,y) or dfs(x,y+1) or dfs(x,y-1)

if dfs(*S):
    print("Yes")
else:
    print("No")
