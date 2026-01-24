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
Karena ini hanya XOR biasa dan bukan AES, ditambah kita sudah ada keynya, jadi aku buat script solve.py di repository ini untuk melakukan XOR langsung ke ciphernya karena sifat XOR yang 
