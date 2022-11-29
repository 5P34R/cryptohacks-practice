from pwn import * # pip install pwntools
import json
from Crypto.Util.number import long_to_bytes
import codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


res = []
res.append("")

while True:
    received = json_recv()


    ty = received["type"] 
    chall = received["encoded"]
    
    print("Received type: ")
    print(ty)
    print("Received encoded value: ")
    print(chall)

    if ty == "base64":
        res[0] = base64.b64decode(chall)
        print(res[0])

    
    elif ty == "hex":
        res[0] = bytes.fromhex(chall)
        print(res[0])
        
        
    elif ty == "rot13":
        res[0] = codecs.encode(str(chall), 'rot_13')
        print(res[0])
        
        
    elif ty == "bigint":
        res[0] = long_to_bytes(int(chall, 16))
        print(res[0])
        
        
    elif ty == "utf-8":
        re = ""
        for i in chall:
            re += chr(i)
        res[0] = re
        print(re)
        
    else:
        if f:
            print(f"[+] found flag {received['flag']}")
    
    to_send = {
            "decoded": str(res[0].decode("utf-8") if type(res[0]) == type('a'.encode()) else res[0])
        }
    json_send(to_send)

    

