#!/usr/bin/env python3

def solve():
    full_binary = ""
    flag = ""

    local_58 = [int('0') for _ in range(36)]
    local_58[0] = -0x1f
    local_58[1] = -0x59
    local_58[2] = '\x1e'
    local_58[3] = -8
    local_58[4] = 'u'
    local_58[5] = '#'
    local_58[6] = '{'
    local_58[7] = 'a'
    local_58[8] = -0x47
    local_58[9] = -99
    local_58[10] = -4
    local_58[11] = 'Z'
    local_58[12] = '['
    local_58[13] = -0x21
    local_58[14] = 'i'
    local_58[15] = 0xd2
    local_58[16] = -2
    local_58[17] = '\x1b'
    local_58[18] = -0x13
    local_58[19] = -0xc
    local_58[20] = -0x13
    local_58[21] = 'g'
    local_58[22] = -0xc

    for i in range(23):
        val = local_58[i]
        if isinstance(val,str):
            angka = ord(val)
        else:
             angka = val
        angka_unsign = angka & 0xFF
        biner_str = f"{angka_unsign:08b}"
        print("Index:",i)
        print("Raw:",angka_unsign)
        print("Biner:",biner_str)
        full_binary += biner_str
    
    print(full_binary)
    for j in range(0,len(full_binary),7):
        print("Biner:",full_binary[j:j+7])
        print("Char:",chr(int(full_binary[j:j+7],2)))
        
        flag += chr(int(full_binary[j:j+7],2))
    print(flag)

if __name__ == "__main__":
    solve()