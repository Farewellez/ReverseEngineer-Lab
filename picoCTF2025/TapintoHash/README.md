## Tap into Hash
### Author: NGIRIMANA Schadrack
### Tag: Medium, Reverse Engineering, picoCTF 2025, browser_webshell_solveable

### Description
Can you make sense of this source code file and write a function that will decode the given encrypted file content?
Find the encrypted file <a href="https://challenge-files.picoctf.net/c_verbal_sleep/5b201977bdbb074a214aa9f5c06cb77187cfc02a2ba5b7ca9fc8dfe697d1e549/enc_flag">here</a>. 
It might be good to analyze <a href="https://challenge-files.picoctf.net/c_verbal_sleep/5b201977bdbb074a214aa9f5c06cb77187cfc02a2ba5b7ca9fc8dfe697d1e549/block_chain.py">source file</a> to get the flag.

## Write-up
Simple saja, fokus di logic enkripsi di program ini. Karena inti dari program ini memang membuat beberapa blockchain yang melalui serangkaian encoding base64, enkripsi dengan xor dan key yang di hash dengan sha256. Tapi jika di lihat lebih teliti dibagian ini

```
    all_blocks = get_all_blocks(blockchain)

    blockchain_string = blockchain_to_string(all_blocks)
    encrypted_blockchain = encrypt(blockchain_string, token, key)
```
Semua block tadi di dimpan di satu variable dan input kita baru dipakai di method encrypted blockchain. Artinya di method inilah kemungkinan flagnya disembunyikan. Dibagian ini

```
    midpoint = len(plaintext) // 2

    first_part = plaintext[:midpoint]
    second_part = plaintext[midpoint:]
    modified_plaintext = first_part + inner_txt + second_part
    block_size = 16
```
Kelihatan kalau inner_txt atau input kita di argumen atau bisa dibilang flagnya itu disisipkan di antara first part dan juga second part. Plaintext yang dimodifikasi ini kemudian di padding dan diXOR dengan key yang sudah dihash dan di padding yang ada di logic ini

```
    plaintext = pad(modified_plaintext, block_size)
    key_hash = hashlib.sha256(key).digest()

    ciphertext = b''

    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]
        cipher_block = xor_bytes(block, key_hash)
        ciphertext += cipher_block
```
Karena ini hanya XOR biasa dan bukan AES, ditambah kita sudah ada keynya, jadi aku buat script solve.py di repository ini untuk melakukan XOR langsung ke ciphernya karena sifat XOR yang inversible yang mana jika A XOR B = C maka hanya perlu melakukan C XOR B untuk mendapatkan A. Hasil akhir dari script solver akan seperti ini

```
Raw cipher: b'5410603d236160940efdcaf26beca4ddfaf5327aaf41b730645f77d4ccfdded5-00118a79e0fbdbba6bfc52384735078d69073d211d4efbc15b35ce5a168ad59a-00f7f88f01862b79cff1f05cc3e3dc12picoCTF{block_3SRhViRbT1qcX_XUjM0r49cH_qCzmJZzBK_41c10331}1123443252a07cca666af8e7ace2495f-000f669f06d71a4263f0353d23bc3968d6ba3e3a123ff8a4581d730ddb5cedde-009df6f0bf347f93ff88a7ff8b381550eeb65f198479a008635eeb691cf34f2c\x02\x02' 384
b'12picoCTF{block_3SRhViRbT1qcX_XUjM0r49cH_qCzmJZzBK_41c10331}1123443252a07cca666af8e7ace2495f-000f669f06d71a4263f0353d23bc3968d6ba3e3a123ff8a4581d730ddb5cedde-009df6f0bf347f93ff88a7ff8b381550eeb65f198479a008635eeb691cf34f2c\x02\x02'
```
**Flag: picoCTF{block_3SRhViRbT1qcX_XUjM0r49cH_qCzmJZzBK_41c10331}**
