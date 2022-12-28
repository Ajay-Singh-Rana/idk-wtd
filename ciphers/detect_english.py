# h3avren

import sys 

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz \t\n'

message = sys.argv[1]
minimum_word_percentage = int(sys.argv[2]) if (len(sys.argv) > 2) else 45
minimum_letter_percentage = int(sys.argv[3]) if (len(sys.argv) > 3) else 85

letters_only_message = ''
for i in message:
    if i in SYMBOLS:
        letters_only_message += i

letters = len(letters_only_message)

matches = 0
dictionary = {}

with open('wordlist.txt','r') as file:
    content = file.read()
    content = content.split()
    for word in content:
        dictionary[word] = 1

letters_only_message = letters_only_message.split()
for word in letters_only_message:
    if(word.lower() in dictionary):
        matches += 1

letters_percentage = (letters/len(message)*100)
words_percentage = (matches/len(letters_only_message)*100) 

if(letters_percentage > minimum_letter_percentage and 
   words_percentage > minimum_word_percentage):
    print("English Detected..!")
else:
    print("English not Detected..!")

print("Matches: ", matches)
print("Letter's: ", letters)
print("Percentage of word matches: ", words_percentage)
print("Letter's only percentage: ", letters_percentage)

