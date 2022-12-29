# h3avren

import sys

key = int(sys.argv[1])
key_2 = int(sys.argv[2])
message = sys.argv[3]

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"\
          "abcdefghijklmnopqrstuvwxyz1234567890"\
          "%$#@,^+-_='\".;:()*&"

set_size = len(SYMBOLS)
# multiplicatively_translated = ''
affine_translated = ''

# function to find greatest common divisor 
def gcd(num_1,num_2):
    if(num_1 == 0):
        return num_2
    elif(num_2 == 0):
        return num_1
    else:
        return gcd(num_2,num_1 % num_2)

# checks for keys
if(gcd(set_size,key) != 1):
    sys.exit(f"Wrong multiplicative key passed..!\nCan't encrypt with {key} as it is"\
             f"not coprime with {set_size}.\nTry with another another key..!"\
             f"The multiplicative key should be coprime with {set_size}")

if(key < 2 or key_2 > (set_size - 1) or key_2 < 1):
    sys.exit("Multiplicative key should not be less than or equal to 1\n"\
             f"Second key should be between 1 and {set_size}")

# decryption
for i in message:
    # replacement = SYMBOLS[((SYMBOLS.find(i) * key) % set_size)]
    if i in SYMBOLS:
        index = (((SYMBOLS.find(i) * key) + key_2) % set_size)
        # translated_index = index if (index < set_size) else (set_size - index)
        # multiplicatively_translated += replacement
        affine_translated += SYMBOLS[index]
    else:
        affine_translated += i

"""
for i in multiplicatively_translated:
    index = (SYMBOLS.find(i) + key_2)
    translated_index = index if index < set_size else (set_size - index)
    replacement = SYMBOLS[translated_index]
    affine_translated += replacement

print(multiplicatively_translated)"""

print(affine_translated)
