import re

S = input()
ans = re.split(r'[^ATGC]', S)

maxlen = -1
maxarg = 0
for a in ans:
    maxlen = len(a) if len(a) > maxlen else maxlen

print(maxlen)

