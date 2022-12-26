# h3avren
import sys

key = int(sys.argv[1])
message = sys.argv[2]

matrix = []
translated = ''
columns = (len(message) // key) if ((len(message) / key) / (int(len(message) / key)) == 0) else ((len(message) // key) + 1)
for i in range(key):
    #temp = []
    for j in range(columns):
        #if(((key * j) + (i + 1)) <30): # doesn't let the cell number pass beyond the message length
        #   try:
        #        temp.append(message[(i + j) + ((columns - 1) * i)])
        #   except IndexError:
        #      print((i + j) + ((columns - 1) * i))
        if(((i + j) + ((columns - 1) * i)) < len(message)):
            matrix.append(message[(i + j) + ((columns - 1) * i)])
    #matrix.append(temp)

translated = ''
for j in range(columns):
    for i in range(key):
        translated += matrix[(columns * i) + j] if (((columns*i) + j) < len(matrix)) else ''

"""
for j in range(columns):
    for i in matrix:
        translated += i[j]"""
print(matrix)
print(translated)
