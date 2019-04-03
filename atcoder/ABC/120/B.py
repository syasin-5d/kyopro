from fractions import gcd

def yakusuu(a):
    yakusuu = list()
    for i in range(1,a+1):
        if a % i == 0:
            yakusuu.append(i)
    return yakusuu

A, B, K = map(int, input().split())

ans = yakusuu(gcd(A,B))[-K]
print(ans)

