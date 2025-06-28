from pwn import *
from hashlib import sha256
import string

HOST = 'localhost' # Change to the actual server address 
PORT = 1337 # Change to the actual server port 
FLAG_LEN = 40
CHARSET = string.printable

def get_hash_from_server(payload):
    try:
        io = remote(HOST, PORT, level='error')
        
        # 1. Choose "Sign a message"
        io.sendlineafter(b'> ', b'1')
        
        # 2. Send our crafted message
        io.sendlineafter(b'Enter your message: ', payload)
        
        # 3. Receive and parse the hash list
        io.recvuntil(b"Hash list:\n")
        hash_list = eval(io.recvline().strip().decode())
        
        io.close()
        return hash_list[0]
    except Exception as e:
        log.failure(f"Error communicating with server: {e}")
        return None

def solve():
  
    known_flag = ""

    while len(known_flag) < FLAG_LEN:

        padding_len = FLAG_LEN - 1 - len(known_flag)
        padding = b'A' * padding_len
        
        target_hash = get_hash_from_server(padding)
        if not target_hash:
            return

        found_char = False
        for char in CHARSET:
            test_block = padding + known_flag.encode() + char.encode()
            
            our_hash = sha256(test_block).digest().hex()

            if our_hash == target_hash:
                known_flag += char
                print(f"Found character: {char} Current flag: {known_flag}")
                found_char = True
                break 
        
        if not found_char:
            return
    print(f"Flag found: {known_flag}")

if __name__ == "__main__":
    solve() 