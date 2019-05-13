def third_select(S):
    left = 0
    right = N - 1
    change = 0
    sharp_appeared = False
    for i, s in enumerate(S[::-1]):
        if s == '#':
            sharp_appeared = True
        elif sharp_appeared:
            right = N - i
            break
        else:
            change += 1
    print(change)
    for s in S[:right]:
        if s == '#':
            change += 1
    print(change)
    for i,s in enumerate(S):
        if s == '#':
            left = i
            break
    return min(change, S[left:].count('.'))

N = int(input())
S = input()

ALL_period = S.count('#')
ALL_sharp = N - ALL_period



print(min(ALL_period, ALL_sharp, third_select(S)))
