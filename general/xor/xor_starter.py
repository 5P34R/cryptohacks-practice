#manual

string : str = "label"
res = ""
for i in string:
    res += chr(ord(i) ^ 13)
print("crypto{"+res+"}")

# pwntools
from pwn import xor
print(xor("label".encode('utf-8'), 13))