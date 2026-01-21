## Flag Hunters
### Author: syreal
### Tags: Easy, Reverse Engineering, picoCTF 2025, browser_webshell_solveable
### Description
Lyrics jump from verses to the refrain kind of like a subroutine call. There's a hidden refrain this program doesn't print by default. Can you get it to print it? There might be something in it for you. <br>
The program's source code can be downloaded <a href="https://challenge-files.picoctf.net/c_verbal_sleep/63cac71f63ab95d9f131aa1b1177665a5e70f9a734ca46a68fe8b0eb3b02f052/lyric-reader.py">here</a>. <br>
Additional details will be available after launching your challenge instance. <br>

## Write-up
Jadi ketika selesai download filenya maka akan diberikan sebuah python script yang bisa di cek sendiri dalamnya. intinya dia akan menjalankan sebuah lirik lagu yang akan berulang sampai max line itu terpenuhi. vulnerabilitnya dimulai dari bagian ini

```
      elif re.match(r"CROWD.*", line):
        crowd = input('Crowd: ')
        song_lines[lip] = 'Crowd: ' + crowd
        lip += 1
```
bagian ini adalah satu-satunya payloads atau input buffer yang bisa diinject. sayangnya ada _Lack of Input Sanitization_ yang mana tidak ada filtering terhadap input user. alhasil berdampak pada bagian ini

```
for line in song_lines[lip].split(';'):
      if line == '' and song_lines[lip] != '':
        continue
```
injection kita bisa berdampak disini dengan teknik _delimiter injection_ karena tiap baris lagu akan selalu di split tiap ada ';' maka apapun baris yang ada tanda itu akan masuk ke split dan dibaca sebagai lirik yang valid. sayangnya bagian input tadi di bagian ini

```
 song_lines[lip] = 'Crowd: ' + crowd
```
dia membuat line baru sesuai input user, contoh dua input ini yang telah di tambahkan debug code di script debug

#### normal input

```
13
['CROWD (Singalong here!)', '']
Crowd: aaa
...
12
['We’re chasing that victory, and we’ll never quit.']
We’re chasing that victory, and we’ll never quit.
13
['Crowd: aaa']
Crowd: aaa
14
['RETURN 34']
```
maka di lirik akan ada baris baru yaitu ['Crowd: aaa'], tapi bagaimana jika input ini ditambahkan ';' maka hasilnya seperti ini

#### poison input

```
12
['We’re chasing that victory, and we’ll never quit.']
We’re chasing that victory, and we’ll never quit.
13
['CROWD (Singalong here!)', '']
Crowd: ;RETURN 3
14
['RETURN 25']
14
['RETURN 25']
25
['']
...
13
['Crowd: ', 'RETURN 3']
Crowd: 
14
['RETURN 34']
3
['With unity and skill, flags we deliver,']
With unity and skill, flags we deliver,
4
['The ether’s ours to conquer, FLAG{FAKE}']
The ether’s ours to conquer, FLAG{FAKE}
```
alih-alih hanya string "crowd: <input kita>" dia malah menambahkan element baru di array karena delimiter injection dengan char ';' tadi alhasil terjadi _Control Flow Hijacking_ yang mengarah ke bagian ini

```
      elif re.match(r"RETURN [0-9]+", line):
        lip = int(line.split()[1])
```
karena di baris lirik sekarang, mengandung kata RETURN yang sudah kita inject tadi maka lip akan berubah menjadi element index ke-1 dari line yaitu [RETURN, 3] yang mana 3 akan menjadi lip dan lirik baris ketiga yang berisi secret intro akan ter-trigger dan memuncukkan flag. jika dicoba langsung di instance, lognya seperti ini

#### Result
```
$ nc verbal-sleep.picoctf.net 56178
Command line wizards, we’re starting it right,
Spawning shells in the terminal, hacking all night.
Scripts and searches, grep through the void,
Every keystroke, we're a cypher's envoy.
Brute force the lock or craft that regex,
Flag on the horizon, what challenge is next?

We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
Crowd: ;RETURN 3

Echoes in memory, packets in trace,
Digging through the remnants to uncover with haste.
Hex and headers, carving out clues,
Resurrect the hidden, it's forensics we choose.
Disk dumps and packet dumps, follow the trail,
Buried deep in the noise, but we will prevail.

We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
Crowd: 
The ether’s ours to conquer, picoCTF{70637h3r_f0r3v3r_0099cf61}


[REFRAIN]
We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
Crowd: 
The ether’s ours to conquer, picoCTF{70637h3r_f0r3v3r_0099cf61}


[REFRAIN]
We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
Crowd: 
The ether’s ours to conquer, picoCTF{70637h3r_f0r3v3r_0099cf61}


[REFRAIN]
We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
Crowd: 
The ether’s ours to conquer, picoCTF{70637h3r_f0r3v3r_0099cf61}


[REFRAIN]
We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
Crowd: 
The ether’s ours to conquer, picoCTF{70637h3r_f0r3v3r_0099cf61}


[REFRAIN]
We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
Crowd: 
The ether’s ours to conquer, picoCTF{70637h3r_f0r3v3r_0099cf61}


[REFRAIN]
We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
Crowd: 
The ether’s ours to conquer, picoCTF{70637h3r_f0r3v3r_0099cf61}


[REFRAIN]
We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
Crowd: 
The ether’s ours to conquer, picoCTF{70637h3r_f0r3v3r_0099cf61}


[REFRAIN]
We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
Crowd: 
```

**FLAG PAWNED: picoCTF{70637h3r_f0r3v3r_0099cf61}**
