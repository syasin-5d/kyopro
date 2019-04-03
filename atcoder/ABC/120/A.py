def favorite_sound(A,B,C):
    if A*C <= B:
        return C
    else:
        return int(B / A)

A, B, C = map(int, input().split())
print(favorite_sound(A,B,C))
