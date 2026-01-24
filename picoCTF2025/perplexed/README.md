## perplexed
### Author: SkrubLawd
### Tag: Medium, Reverse Engineering, picoCTF 2025, browser_web_solveable

### Description
Download the binary <a href="https://challenge-files.picoctf.net/c_verbal_sleep/2326718ce11c5c89056a46fce49a5e46ab80e02d551d87744306ae43a4767e06/perplexed">here</a>.

## Write-up
Jadi disini kita diberikan sebuah binary yang jika kita jalankan akan meminta password. Disini aku langsung saja disas dan decompile pake ghidra dan nemu logic utamanya di check fucntion

```

undefined8 check(char *param_1)

{
  size_t sVar1;
  undefined8 uVar2;
  size_t sVar3;
  char local_58 [36];
  uint local_34;
  uint local_30;
  undefined4 local_2c;
  int local_28;
  uint local_24;
  int local_20;
  int local_1c;
  
  sVar1 = strlen(param_1);
  if (sVar1 == 0x1b) {
    local_58[0] = -0x1f;
    local_58[1] = -0x59;
    local_58[2] = '\x1e';
    local_58[3] = -8;
    local_58[4] = 'u';
    local_58[5] = '#';
    local_58[6] = '{';
    local_58[7] = 'a';
    local_58[8] = -0x47;
    local_58[9] = -99;
    local_58[10] = -4;
    local_58[0xb] = 'Z';
    local_58[0xc] = '[';
    local_58[0xd] = -0x21;
    local_58[0xe] = 'i';
    local_58[0xf] = 0xd2;
    local_58[0x10] = -2;
    local_58[0x11] = '\x1b';
    local_58[0x12] = -0x13;
    local_58[0x13] = -0xc;
    local_58[0x14] = -0x13;
    local_58[0x15] = 'g';
    local_58[0x16] = -0xc;
    local_1c = 0;
    local_20 = 0;
    local_2c = 0;
    for (local_24 = 0; local_24 < 0x17; local_24 = local_24 + 1) {
      for (local_28 = 0; local_28 < 8; local_28 = local_28 + 1) {
        if (local_20 == 0) {
          local_20 = 1;
        }
        local_30 = 1 << (7U - (char)local_28 & 0x1f);
        local_34 = 1 << (7U - (char)local_20 & 0x1f);
        if (0 < (int)((int)param_1[local_1c] & local_34) !=
            0 < (int)((int)local_58[(int)local_24] & local_30)) {
          return 1;
        }
        local_20 = local_20 + 1;
        if (local_20 == 8) {
          local_20 = 0;
          local_1c = local_1c + 1;
        }
        sVar3 = (size_t)local_1c;
        sVar1 = strlen(param_1);
        if (sVar3 == sVar1) {
          return 0;
        }
      }
    }
    uVar2 = 0;
  }
  else {
    uVar2 = 1;
  }
  return uVar2;
}
```
Disini intinya ada 23 byte char flag yang ter-enkripsi. Logic decryptnya cukup mudah, dibagian ini

```
    for (local_24 = 0; local_24 < 0x17; local_24 = local_24 + 1) {
      for (local_28 = 0; local_28 < 8; local_28 = local_28 + 1) {
        if (local_20 == 0) {
          local_20 = 1;
        }
```
Biner dari raw flag itu hanya 7 bit biner bukan 8. Biner paling awal akan dibuang dan akan dimulai langsung dari index ke-1. Bentuk lebih rapi sudah aku buat di logic.py untuk gambaran simple logicnya. Kerentanan disini adalah _hardcoded password with custom bit-packing_ yang ada di 23 byte array tadi yang seharusnya tidak disimpan disitu ditambah logicnya juga rentan, bukan hash, enkripsi atau encode tapi hanya bit yang di pack atau obfuscation.
<br>

Intinya kalau ingin dapat flagnya hanya perlu membuat script python dengan menggabungkan semua value dari 23 byte tadi, lalu ubah jadi biner dan gabung semua jadi 1 baris biner, ambil 7 bit biner tiap iterasi dan ubah ke char ascii untuk dapat flagnya. script solver ada di solve.py di repository ini. Hasil akhir nanti akan seperti ini

```
└─$ python3 solve.py
Index: 0
Raw: 225
Biner: 11100001
Index: 1
Raw: 167
Biner: 10100111
Index: 2
Raw: 30
Biner: 00011110
Index: 3
Raw: 248
Biner: 11111000
Index: 4
Raw: 117
Biner: 01110101
Index: 5
Raw: 35
Biner: 00100011
Index: 6
Raw: 123
Biner: 01111011
Index: 7
Raw: 97
Biner: 01100001
Index: 8
Raw: 185
Biner: 10111001
Index: 9
Raw: 157
Biner: 10011101
Index: 10
Raw: 252
Biner: 11111100
Index: 11
Raw: 90
Biner: 01011010
Index: 12
Raw: 91
Biner: 01011011
Index: 13
Raw: 223
Biner: 11011111
Index: 14
Raw: 105
Biner: 01101001
Index: 15
Raw: 210
Biner: 11010010
Index: 16
Raw: 254
Biner: 11111110
Index: 17
Raw: 27
Biner: 00011011
Index: 18
Raw: 237
Biner: 11101101
Index: 19
Raw: 244
Biner: 11110100
Index: 20
Raw: 237
Biner: 11101101
Index: 21
Raw: 103
Biner: 01100111
Index: 22
Raw: 244
Biner: 11110100
1110000110100111000111101111100001110101001000110111101101100001101110011001110111111100010110100101101111011111011010011101001011111110000110111110110111110100111011010110011111110100
Biner: 1110000
Char: p
Biner: 1101001
Char: i
Biner: 1100011
Char: c
Biner: 1101111
Char: o
Biner: 1000011
Char: C
Biner: 1010100
Char: T
Biner: 1000110
Char: F
Biner: 1111011
Char: {
Biner: 0110000
Char: 0
Biner: 1101110
Char: n
Biner: 0110011
Char: 3
Biner: 1011111
Char: _
Biner: 1100010
Char: b
Biner: 1101001
Char: i
Biner: 0110111
Char: 7
Biner: 1011111
Char: _
Biner: 0110100
Char: 4
Biner: 1110100
Char: t
Biner: 1011111
Char: _
Biner: 1100001
Char: a
Biner: 1011111
Char: _
Biner: 0110111
Char: 7
Biner: 1101001
Char: i
Biner: 1101101
Char: m
Biner: 0110011
Char: 3
Biner: 1111101
Char: }
Biner: 00
Char: 
picoCTF{0n3_bi7_4t_a_7im3}
```
Disitu terlihat kalau array of char sendiri hanya menerima 8 bit biner, jadi jika ada  7 bit biner maka akan dilakukan padding dengan mengambil biner di depannya.
<br>
**Flag:picoCTF{0n3_bi7_4t_a_7im3}**
