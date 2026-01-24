#!/usr/bin/env python3
def check(param1):
    
    local_58 = [int('0') for _ in range(36)]

    local_1c: int
    local_20: int
    local_2c = '' # undefined4

    local_28: int = 0
    local_24: int = 0 # uint

    local_30: int # uint
    local_34: int # uint

    # print(len(local_58))
    sVar1 = len(param1)
    if sVar1 == 27: # 0x1b 
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

        local_1c = 0
        local_20 = 0
        local_2c = 0
        for local_24 in range(23):
            for local_28 in range(8):
                if local_20 == 0:
                    local_20 = 1
                local_30 = 1 << (7 - local_28 & 31) # 0x1f cuma pengaman agar pergeseran decompiler tidak terlalu jauh
                local_34 = 1 << (7 - local_20 & 31) # 0x1f cuma pengaman agar pergeseran decompiler tidak terlalu jauh  
                print("local_30:",bin(local_30))
                print("local_34:",bin(local_34))

                print("test 1:",int(int(param1[local_1c]) & local_34))
                print("tets 2:", int(int(local_58[int(local_24)]) & local_30))
                if 0 < int(int(param1[local_1c]) & local_34) != 0 < int(int(local_58[int(local_24)]) & local_30):
                    print("Return 1")
                    return 1
                local_20 = local_20 + 1

input_buffer = b'A'*27 # 0x1b
check(input_buffer)