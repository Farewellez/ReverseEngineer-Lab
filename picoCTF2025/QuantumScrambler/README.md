## Quantum Scrambler
### Author: Michael Crotty
### Tag: Medium, Reverse Engineer, picoCTF 2025, browser_webshell_solveable 

### Description
We invented a new cypher that uses "quantum entanglement" to encode the flag. Do you have what it takes to decode it?
Additional details will be available after launching your challenge instance.

## Write-up
Jadi ketika instance dijalankan maka akan ada banyak List array yang muncul. kurang lebih seperti ini

<img width="1903" height="486" alt="image" src="https://github.com/user-attachments/assets/a2e795ba-e05f-4053-86c4-c4c1e00326a1" />

Jika dilihat juga ada source code yang bisa di download <a href="https://challenge-files.picoctf.net/c_verbal_sleep/48c0a7965daffa76fb1edeed6a6e1bd387bd11702b115ca3f4eaf960e46791e9/quantum_scrambler.py">disini</a>

Terlihat cukup memusingkan jadi coba buat script debug yang menduplikasi source code nya dan coba debug satu-persatu. kurang lebih bisa dibuat seperti ini

```
└─$ cat test.py                   
flag = open('flag.txt','r').read()
hex_flag = []

for char in flag:
    hex_flag.append([str(hex(ord(char)))])

print(flag.split())
print(hex_flag)

A:list = hex_flag
i = 2
while (i < len(A)):
    print("Awal:",A)
    print("loop dengan i=",i,"dan len =",len(A))
    print(A[i-2],"+= pop dari",A[i-1])
    A[i-2] += A.pop(i-1)
    print("setelah ditambah: ",A)
    print(A[i-1], "gabung", A[:i-2])
    A[i-1].append(A[:i-2])
    print("setelah digabung",A)
    i += 1
    print("i saat ini",i,"dan len saat ini",len(A))
print(A[-1])

candidate = ""
for i in range(len(A)-1,0-1,-1):
    if i == len(A)-1:
        print("i:",i)
        candidate += ''.join(A[i])
    elif i == len(A)-2:
        print("i:",i)
        candidate += ''.join(A[i][0])
    else:
        print("i:",i)
        candidate += ''.join(A[i][-1])
        candidate += ''.join(A[i][0])
print(candidate.split('0x'))
for char in flag:
    print(hex(ord(char)))                                                                                                                                                                                                                                            

```
pastikan flag.txt dummy sudah ada di direktori saat ini. semisal di sini kuisi hanya dengan alphabet

```
─$ cat flag.txt      
abcdefghijklmnopqrstuv  
```

jika dijalankan maka hasilnya seperti ini. fokus pada bagian akhir list

```
.... bagian ataas
['0x63', [], '0x64'], ['0x65', [['0x61', '0x62']], '0x66']], '0x6a']], '0x6e']], '0x72']]], ['0x76']]
i saat ini 12 dan len saat ini 12
['0x76']
i: 11
i: 10
i: 9
i: 8
i: 7
i: 6
i: 5
i: 4
i: 3
i: 2
i: 1
i: 0
['', '76', '75', '74', '73', '72', '71', '70', '6f', '6e', '6d', '6c', '6b', '6a', '69', '68', '67', '66', '65', '64', '63', '62', '61']
0x61
0x62
0x63
0x64
0x65
0x66
0x67
0x68
0x69
0x6a
0x6b
0x6c
0x6d
0x6e
0x6f
0x70
0x71
0x72 
0x73
0x74
0x75
0x76
```

jika kamu cek isi dari list yang dikirim oleh server maka akan terlihat ada sebuah element tunggal diakhir list. case ini terjadi jika dan hanya jika i saat ini dan len list saat ini sama. ada case lain jika ternyata i lebih dari len list sebanyak 1 maka diakhir list tidak akan ada 1 elemnt tunggal.
<br> Apa artinya? artinya jumlah flag genap dan bukan ganjil semisal contoh disini aku ambil isi dummy flag adalah "abcdefghijklmnopqrstu" yang jumlahnya 22. Tidak perlu pusing, jika kamu teliti maka akan ada pattern yang berulang pada list yang terkirim. Apa itu? yaitu kepingan flag bisa kamu dapatkan dengan cara mengambil element list terakhir, lalu ambil elemen pertama dari list dari terakhir lalu mundur ke element list selanjutnya dengan mengambil element akhir dan awal. jika divsualisasikan seperti ini:

```
└─$ python3 test.py
['abcdefgh']
[['0x61'], ['0x62'], ['0x63'], ['0x64'], ['0x65'], ['0x66'], ['0x67'], ['0x68']] -> flag asli urut
Awal: [['0x61'], ['0x62'], ['0x63'], ['0x64'], ['0x65'], ['0x66'], ['0x67'], ['0x68']]
loop dengan i= 2 dan len = 8
['0x61'] += pop dari ['0x62']
setelah ditambah:  [['0x61', '0x62'], ['0x63'], ['0x64'], ['0x65'], ['0x66'], ['0x67'], ['0x68']]
['0x63'] gabung []
setelah digabung [['0x61', '0x62'], ['0x63', []], ['0x64'], ['0x65'], ['0x66'], ['0x67'], ['0x68']]
i saat ini 3 dan len saat ini 7

Awal: [['0x61', '0x62'], ['0x63', []], ['0x64'], ['0x65'], ['0x66'], ['0x67'], ['0x68']]
loop dengan i= 3 dan len = 7
['0x63', []] += pop dari ['0x64']
setelah ditambah:  [['0x61', '0x62'], ['0x63', [], '0x64'], ['0x65'], ['0x66'], ['0x67'], ['0x68']]
['0x65'] gabung [['0x61', '0x62']]
setelah digabung [['0x61', '0x62'], ['0x63', [], '0x64'], ['0x65', [['0x61', '0x62']]], ['0x66'], ['0x67'], ['0x68']]
i saat ini 4 dan len saat ini 6

Awal: [['0x61', '0x62'], ['0x63', [], '0x64'], ['0x65', [['0x61', '0x62']]], ['0x66'], ['0x67'], ['0x68']]
loop dengan i= 4 dan len = 6
['0x65', [['0x61', '0x62']]] += pop dari ['0x66']
setelah ditambah:  [['0x61', '0x62'], ['0x63', [], '0x64'], ['0x65', [['0x61', '0x62']], '0x66'], ['0x67'], ['0x68']]
['0x67'] gabung [['0x61', '0x62'], ['0x63', [], '0x64']]
setelah digabung [[**'0x61', '0x62'**], [**'0x63'**, [], **'0x64'**], [**'0x65'**, [['0x61', '0x62']], **'0x66'**], [**'0x67'**, [['0x61', '0x62'], ['0x63', [], '0x64']]], **['0x68']**]
i saat ini 5 dan len saat ini 5

['0x68']
```
terlihat kan jika yang ditandai dengan **flag** asteric itu adalah kepingan flag yang memiliki pola:
1. bagian flag terakhir ada di array[-1]
2. bagian flag kedua dari terakhir ada di array[-2][0]
3. sisanya hanya perlu iterasi array[i][-1] dan array[i][0] dimana i adalah -3,-4,...,i jadi berjalan mundur. script bisa di cek di directory ini **solve.py**

setelah selesai maka akan dapat flag yang berurutan dari belakang dan hanya perlu di reverse

```
└─$ python3 solve.py       
i: 16
i: 15
i: 14
i: 13
i: 12
i: 11
i: 10
i: 9
i: 8
i: 7
i: 6
i: 5
i: 4
i: 3
i: 2
i: 1
i: 0
picoCTF{python_is_weird797ef9bd} 
```
**Flag: picoCTF{python_is_weird797ef9bd}**
