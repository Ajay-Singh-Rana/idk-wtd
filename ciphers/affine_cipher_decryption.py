# h3avren

import sys

# funciton to find gcd
def gcd(a,b):
    if(a == 0):
        return b
    elif(b == 0):
        return a
    else:
        return gcd(b,a%b)

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'\
          "%$#@,^+-_='\".;:()*&"

set_size = len(SYMBOLS)
key = int(sys.argv[1])
key_2 = int(sys.argv[2])

message = sys.argv[3]
translated = ''

# calculating multiplicative modulo inverse
def modulo_inverse(key,set_size):
    if(gcd(key,set_size) == 1):
        i = 1
        while True:
            if(((key * i) % set_size) == 1):
                return i
            i += 1
    else:
        sys.exit("Key and set_size aren't co-primes"\
                 " and hence modulo inverse doesn't exist.")

mod_inverse = modulo_inverse(key,set_size)

for i in message:
    if i in SYMBOLS:
        print(i,1)
        index = (((SYMBOLS.find(i) - key_2) * mod_inverse) % set_size)
        translated += SYMBOLS[index]
    else:
        print(i,2)
        translated += i

print(translated)
