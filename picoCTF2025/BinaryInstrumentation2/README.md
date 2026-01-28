### Tag: Medium, Reverse Engineering, picoCTF 2025
### Author: Venax

### Description
I've been learning more Windows API functions to do my bidding. Hmm... I swear this program was supposed to create a file and write the flag directly to the file. Can you try and intercept the file writing function to see what went wrong?
Download the exe <a href="https://challenge-files.picoctf.net/c_verbal_sleep/4aee1b9778a8e56724d015b027431fb236853a94f53e5dcf32c5ed32aed404da/bininst2.zip">here</a>. Unzip the archive with the password picoctf

## Write-Up
Jadi disini ada file yang merupakan lanjutan dari challenge Binary Instrumentation 1 yang lebih sulit. Kenapa lebih sulit? karena disini program tiba-tiba _terminated_ dirinya sendiri tanpa mengeluarkan strings apapun di terminal karena itu kemungkinan flag ditulis ketika program berjalan. Clue dari deskripsi yaitu WinAPI sendiri ada beberapa function yang biasa digunakan untuk input output:
1. WriteFile
2. CreateFile
Kedua library tersebut ada di kernel32.dll karena itu kita bisa pasang breakpoint di beberapa function terkait.

<img width="1043" height="509" alt="image" src="https://github.com/user-attachments/assets/f4bbadd9-8def-41e8-a244-5b05baecdcf7" />

<img width="1051" height="464" alt="image" src="https://github.com/user-attachments/assets/bba55144-1e64-4912-97af-67b41100b274" />


Seperti dua contoh gambar di atas, aku melakukan breakpoint di beberapa fucntion writefile dan createfile, dari sini kita hanya perlu F9 hingga break di salah satu breakpoint. Singkat cerita aku sampai di breakpoint pertama dan yang pertama terkena ternyata adalah dari CreateFileA Function

<img width="1012" height="658" alt="image" src="https://github.com/user-attachments/assets/07dac277-b1cc-49ab-b009-4ef7ec528a97" />

Dari sini aku menemukan 2 cara untuk mendapatkan flagnya. Yang pertama adalah cara yang diharapkan challenge, yaitu menggunakan frida untuk melakukan tracing program. Yang kedua adalah menggunakan x64 debugger ini terus hingga mendapatkan file yang di hardcode. 

### Cara 1: Menggunakan Frida Script
Untuk scriptnya bisa di cek di repository ini di **hook.js**. Intinya kita sudah tau kalau ada WriteFile dan CreateFileA yang ada disini, kita hanya perlu melakukan tracing untuk mengambil argumen yang ada dan melakukan patching terhadap retrun value. Kenapa perlu patching return value? karena di logic untuk menyembunyikan flagnya, program sengaja melakukan CMP atau compare rax dengan -1 yang itu akan selalu sama dan menyebabkan program terminated. Karena itu kita hanya perlu patching value -1 agar tidak sama dengan rax namun aku belum menemukan cara untuk dapat  logic ini kecuali dengan static analyst dengan ghidra atau x64 debugger

### Cara 2: Menggunakan x64 Debugger 
Untuk cara ini kita hoki karena flag di hardcoded. Kita hanya perlu terus F8 hingga return function CreateFileA yang membawa kita kesini

<img width="1045" height="506" alt="image" src="https://github.com/user-attachments/assets/f52b1ba0-0eb3-4133-9add-5d8799dde9cd" />

Seperti yang kukatakan, logicnya adalah membandingkan rax dengan 0xffffffffffffffff yang mana itu akan selalu sama dan kondisi JNZ ke flag tidak pernah terpenuhi. Tapi disini kita gaperlu bypass atau patch loguc ini karena sudah dapat string base64 flagnya. Hasil kedua cara tetap menghasilkan hal sama

**Flag Encoded: cGljb0NURntmcjFkYV9mMHJfYjFuX2luNXRydW0zbnQ0dGlvbiFfYjIxYWVmMzl9**
**Flag Decoded: picoCTF{fr1da_f0r_b1n_in5trum3nt4tion!_b21aef39}**
