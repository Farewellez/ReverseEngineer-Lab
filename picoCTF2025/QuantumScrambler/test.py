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