X, Y = map(int, input().split())

max_legs = 4 * X

if max_legs < Y:
    print("No")
    exit()

legs = max_legs

for i in range(X+1):
    legs = i * 2 + (X-i) * 4
    if legs == Y:
        print("Yes")
        exit()
print("No")
