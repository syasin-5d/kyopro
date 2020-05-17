from scipy.sparse.csgraph import shortest_path
from scipy.sparse import csr_matrix
import sys

def get_path(start, goal, pred):
    return get_path_row(start, goal, pred[start])

def get_path_row(start, goal, pred_row):
    path = []
    i = goal
    while i != start and i >= 0:
        path.append(i)
        i = pred_row[i]
    if i < 0:
        return []
    path.append(i)
    return path[::-1]

N, M = map(int, input().split())
A = []
B = []
neighbor = [[0 for x in range(N)] for y in range(N)]
for i in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    neighbor[a][b] = 1
    neighbor[b][a] = 1

neighbor = csr_matrix(neighbor)

ans = []
d, p = shortest_path(neighbor, return_predecessors=True, indices=0)

for i in range(1,N):
    if p[i]<0:
        print("No")
        sys.exit(0)
    else:
        ans.append(p[i]+1)
print("Yes")
for i in range(N-1):
    print(ans[i])
