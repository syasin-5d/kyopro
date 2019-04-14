X,Y,Z,K = map(int, input().split())
cakes = [list(map(int, input().split())) for _ in range(3)]
 
cakes = list(map(lambda x : sorted(x, reverse=True), cakes))
ans = list()
for i in range(X):
    for j in range(Y):
        for k in range(Z):
            if (i+1)*(j+1)*(k+1)>K:
                break
            ans.append(cakes[0][i] + cakes[1][j] + cakes[2][k])
ans.sort(reverse=True)
print("\n".join(map(str, ans[:K])))
