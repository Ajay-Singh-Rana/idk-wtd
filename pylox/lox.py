# h3avren

# imports
import sys
import os

def run_file(path):     # this function is used to run a script
    with open(path, 'r') as file:
        text = file.read()
    run(text)

def run_prompt():   # this function launches the REPL
    while True:
        try:
            print(">", end = " ")
            line = input()
        except EOFError:
            break;
        run(line)

def run(line):  # Runs the code line by line
    for i in line:
        print(i)

if(len(sys.argv) > 2):
    print("Usage : python3 lox.py [script]")
    sys.exit(64)
elif(len(sys.argv) == 2):
    run_file(sys.argv[1])
else:
    run_prompt();


