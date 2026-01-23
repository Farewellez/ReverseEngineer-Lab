import time
import random
from pwn import *

context.log_level = 'info'

def get_random(seed_time):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    random.seed(seed_time)  # seeding with current time 
    s = ""
    for i in range(20):
        s += random.choice(alphabet)
    return s

flag = False
while True:
    if flag == True:
        break
    print("Mulai")
    try:
        # conn = remote('verbal-sleep.picoctf.net', 56808) # buat langsung ke server
        conn = process('./token_generator.py') # buat test local
        conn.recvuntil(b':')
        predict = int(time.time() * 1000)
        offset = range(0,500,10)
        for i,num in enumerate(offset):
            if i >= 50:
                break

            seed = predict - num
            ftoken = get_random(seed)
            conn.sendline(ftoken.encode())
            response = conn.recvline()

            if b'Congratulations' in response or b'picoCTF' in response:
                print("token: ",ftoken,"berhasil")
                print(response)
                print(conn.recvall().decode())
                flag = True
                break
            elif b'Bye' in response:
                print("reconnent")
                break
            else:
                try:
                    conn.recvuntil(b':')
                except EOFError:
                    break
        conn.close()
        if flag == False:
            print("gagal")
        else:
            pass
    except EOFError:
        print("Koneksi")
        try:
            conn.close()
        except:
            pass
    except exception as e:
        print(e)
    time.sleep(1)