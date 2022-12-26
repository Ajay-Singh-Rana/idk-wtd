# h3avren
import sys
message = sys.argv[1]

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 .,?'

for key in range(len(SYMBOLS)):
        translated = ''
        for symbol in message:
            if(symbol in SYMBOLS):
                translation_index = SYMBOLS.find(symbol) + key
                 
                if(translation_index >= len(SYMBOLS)):
                    translation_index = translation_index - len(SYMBOLS)
                elif(translation_index < 0):
                    translation_index = translation_index + len(SYMBOLS)
                translated += SYMBOLS[translation_index]
            else:
                trasnlated = translated + symbol
        print(translated)

