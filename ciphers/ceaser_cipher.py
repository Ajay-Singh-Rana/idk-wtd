# message to be encrypted
# message = 'UvJ7uv6Jv6J62zrJ7r 7J72JorJr1p2qrqJ0v7uJprn6r5Jpv3ur5'
message = "Hi this is some text to be encoded with ceaser cipher"

# encryption key
key = 13

# whether to encrypt or to decrypt
mode = "decrypt"

# symbols
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# variable for storing/building the encrypted message
translated = ''

# encrypting/decrypting the message
for symbol in message:
    if symbol in SYMBOLS:
        symbol_index = SYMBOLS.find(symbol)

        if mode == 'encrypt':
            translated_index = symbol_index + key
        elif mode == 'decrypt':
            translated_index = symbol_index - key

        # handlind overflow of index
        if translated_index >= len(SYMBOLS):
            translated_index -= len(SYMBOLS)
        elif translated_index < 0:
            translated_index += len(SYMBOLS)

        translated = translated + SYMBOLS[translated_index]
    else:
        translated = translated + symbol

# output the encoded message
print(translated)
