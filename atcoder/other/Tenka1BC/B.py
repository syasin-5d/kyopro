N = int(input())
S = input()
K = int(input())


print(''.join(list(map(lambda x : x if x == S[K-1] else '*', S))))
