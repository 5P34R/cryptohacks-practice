from operator import xor
import string
from pwn import xor
val = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

key = xor(bytes.fromhex(val)[:8], b"crypto{")
print(len(key))

res = xor(bytes.fromhex(val), b"myXORkey")
print(res)