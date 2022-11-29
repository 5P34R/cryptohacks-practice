from pwn import xor
import string
char = string.digits

val = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

for i in char:
    res = xor(bytes.fromhex(val), )
    if "crypto" in res.decode('utf-8'):
        print(res.decode('utf-8'))
    print(res.decode('utf-8'))
