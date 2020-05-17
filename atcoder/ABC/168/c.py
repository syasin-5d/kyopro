import math

A, B, H, M = map(int, input().split())


dH = 360 / 720 # per minutes
dM = 360 / 60 # per minutes

delta = 60 * H + M # elapsed minutes

theta = delta * dH - M * dM

if theta < 0:
    theta = M * dM - delta * dH
if 180 < theta:
    theta = 360 - theta

C = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(math.radians(theta)))

print(C)
