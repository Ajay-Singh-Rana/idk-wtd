import sys

key = int(sys.argv[1])
message = sys.argv[2]

matrix = []
message_length = len(message)
count = 0
temp = []
for i in range(0,len(message)):
    if(count == key):
        matrix.append(temp)
        count = 0
        temp = []
    temp.append(message[i])
    count += 1
    if(i == (len(message) - 1)):
        matrix.append(temp)

translated = ''
for i in range(key + 1):
    for j in range(len(matrix)):
        if(i < len(matrix[j])):
            translated += matrix[j][i]
        else:
            break


print(translated)
