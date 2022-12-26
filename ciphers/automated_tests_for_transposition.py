# h3avren

import subprocess
import random

message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
random_number = random.randint(0,100)
count = 0
for i in range(random_number):
    test_message = ''
    key = random.randint(1,len(message) + 1)
    for j in range(random.randint(1,len(message) + 1)):
        test_message += message[random.randint(0,len(message)-1)]
    
    result = subprocess.check_output(['python3.9', 
                                      'transposition_cipher.py',
                                      f'{key}', 
                                      f'{test_message}']).decode('utf-8')
    result = result.strip()
    decoded_result = subprocess.check_output(['python3.9',
                                              'transposition_cipher_'\
                                              'decryption.py',f'{key}',
                                              f'{result}']).decode('utf-8')
    decoded_result = decoded_result.strip()
    if(test_message == decoded_result):
        status = 'Passed..!'        
    else:
        count += 1
        status = 'Failed..!'

    print(f'\nTest {i}:\nMessage: {test_message}\n'\
           f'Encoded Message: {result}\n'\
           f'Decode Message: {decoded_result}\n'\
           f'Test Status: {status}')

print(f'\n\nTotal Tests: {random_number}\n'\
       f'Tests Passed: {random_number - count}\n'\
       f'Tests Failed: {count}')

