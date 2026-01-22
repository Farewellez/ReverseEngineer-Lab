import sys

def exit():
  sys.exit(0)

def scramble(L):
  A = L
  i = 2
  while (i < len(A)):
    A[i-2] += A.pop(i-1)
    A[i-1].append(A[:i-2])
    print(A,i,len(A))
    i += 1
    
  return L

def get_flag():
  flag = open('flag.txt', 'r').read()
  flag = flag.strip()
  print(flag)
  hex_flag = []
  for c in flag:
    print(c[0],c[-1])
    hex_flag.append([str(hex(ord(c)))])

  return hex_flag

def main():
  flag = get_flag()
  print(flag)
  cypher = scramble(flag)
  print(cypher)

if __name__ == '__main__':
  main()
