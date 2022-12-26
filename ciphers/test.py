# h3avren 

# imports
import sys
import math

# cli arguments
key = int(sys.argv[1])
message = sys.argv[2]

# calculating number of columns in the matrix
columns =  math.ceil(len(message)/key)

translated = ''

matrix = []
count = 0 # to keep a track of the string index

for i in range(key):
    temp = []
    for j in range(columns): 
        """
        (i + (j * key)) is the cell number calculated in a transposed
        way and hence it should be always less than the message length
        (optionally the count value shouldn't go above the message length 
        either). Therefore a check has to be in place for the cell number.
        A check could also be placed for the count variable going out of bounds.
        Tough it won't serve any special purpose until and unless the cell logic 
        is perfect.
        """
        if((i + (j * key)) < len(message)): # and count < len(message)):
            temp.append(message[count])
            count += 1
    
    matrix.append(temp)

for j in range(columns):
    for i in range(key):
        if(j < len(matrix[i])):
            translated += matrix[i][j]

print(translated)
