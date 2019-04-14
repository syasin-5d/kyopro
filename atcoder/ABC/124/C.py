S = input()

len_S = len(S)
first = ("01" * (len_S//2+1))[:len_S]
second = ("10" * (len_S//2+1))[:len_S]

ans = min(bin(int(S,2) ^ int(first,2)).count('1'), bin(int(S,2) ^ int(second,2)).count('1'))
print(ans)
