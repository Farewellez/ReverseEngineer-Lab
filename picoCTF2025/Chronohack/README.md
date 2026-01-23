## Chronohack
### Author: Theoneste Byagutangaza
### Tag: Medium, Reverse Engineering, picoCTF 2025, browser_webshell_solveable

### Description
Can you guess the exact token and unlock the hidden flag?
Our school relies on tokens to authenticate students. Unfortunately, someone leaked an important <a href="https://challenge-files.picoctf.net/c_verbal_sleep/9959cfadf7887ffe477e2c16baeb90aeb7159d39db55263ae1bffcb59a0d013f/token_generator.py">file for token generation</a>. Guess the token to get the flag.

## Write-up
Langsung aja cek source code dan terlihat ada logic ini

```
def get_random(seed_time):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    random.seed(seed_time)  # seeding with current time 
    s = ""
    for i in range(20):
        s += random.choice(alphabet)
    return s
```
yang sesuai nama function, ini adalah kerentanan _insecure randomness_ yang dimana seed yang digunakan untuk generate random token itu mudah ditebak karena pemilik menggunakan time library yang mengambil latar waktu sesuai epoch time dan ini adalah data publik yang juga bisa dilihat orang lain.
<br> 

Karena sudah tertebak, maka kita haya perlu mundur beberapa milidetik atau detik atau mundur beberapa integer agar sesuai dengan waktu sistem membuat token. semisal waktu kita mengirim payloads itu 1769163590733.2578 jika diubah ke integer mungkin 1769163590733 sedangkan di server itu 1769163590740 yang mana selisih beberapa angka. hal inilah yang perlu di exploitasi. <br>

Satu lagi kerentanan yang ada yaitu _lack of rate limiting_ yang mana attacker bisa melakukan bruteforcing dan connect berkali-kali ke sistem dengan menggunakan script exploit seperti yang kubuat di repository ini **(solve.py)**.
Script itu menggunakan pwntools yang akan menghasilkan log yang kurang lebih seperti ini
```
└─$ python3 solve.py
Mulai
[+] Opening connection to verbal-sleep.picoctf.net on port 56808: Done
[*] Closed connection to verbal-sleep.picoctf.net port 56808
gagal
Mulai
[+] Opening connection to verbal-sleep.picoctf.net on port 56808: Done
[*] Closed connection to verbal-sleep.picoctf.net port 56808
gagal
Mulai
[+] Opening connection to verbal-sleep.picoctf.net on port 56808: Done
[*] Closed connection to verbal-sleep.picoctf.net port 56808
gagal
Mulai
[+] Opening connection to verbal-sleep.picoctf.net on port 56808: Done
[*] Closed connection to verbal-sleep.picoctf.net port 56808
gagal
Mulai
[+] Opening connection to verbal-sleep.picoctf.net on port 56808: Done
token:  FnecqtDznLkmxpqwxRQ5 berhasil
b'Congratulations! You found the correct token.\n'
[+] Receiving all data: Done (47B)
[*] Closed connection to verbal-sleep.picoctf.net port 56808
picoCTF{UseSecure#$_Random@j3n3r@T0rsf262cabc}
```
**Flag: picoCTF{UseSecure#$_Random@j3n3r@T0rsf262cabc}**
