A,B,C = map(int, input().split())

if A <= C <= B or B <= C <= A:
    print("Yes")
else:
    print("No")
