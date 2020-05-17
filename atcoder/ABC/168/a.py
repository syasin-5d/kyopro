N = int(input())

josu = ""
amari = N % 10
if amari == 3:
    josu = "bon"
elif amari == 0 or amari == 1 or amari == 6 or amari == 8:
    josu = "pon"
else:
    josu = "hon"
print(josu)
