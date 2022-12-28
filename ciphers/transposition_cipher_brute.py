# h3avren

import subprocess
import sys

message = sys.argv[1]

for i in range(1,len(message) + 1):
    print(f"Trying Key: {i}")
    # trying to decode the message for different keys
    decoded_message = subprocess.check_output(["python3.9", 
                                      "transposition_cipher_decryption.py", 
                                      str(i), message])
    decoded_message = decoded_message.decode("utf-8").strip()
    
    # detecting English in the decoded message
    result = subprocess.check_output(["python3.9", "detect_english.py",
                                      decoded_message, "60", "92"])

    result = result.decode("utf-8").strip()

    # getting word and letter matches
    list_result = [i.split() for i in result.split("\n")]
    word_matches = list_result[1][-1]
    match_pct = list_result[3][-1]


    if("English Detected" in result):
        yes_no = input(f"English detected..! Word Matches: {word_matches}, "\
                       f"Match Percent: {match_pct}\n"\
                       "Press Y to show the message, Press any "\
                       "key to continue decoding: ").lower()
        
        if(yes_no == 'y' or yes_no == 'yes'):
            print(decoded_message)
            quit_perm = input("Press Q to quit or any other key "\
                              "to continue: ").lower()
            if(quit_perm == 'q' or quit_perm == 'quit'):
                break

