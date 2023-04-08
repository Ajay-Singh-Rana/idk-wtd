# h3avren

# imports
import sys
import os
from scanner import Scanner

class Lox:
    def __init__(self):
        self.had_error = False
    
    def run_file(self,path):     # this function is used to run a script
        with open(path, 'r') as file:
            text = file.read()
        run(text)

    def run_prompt(self):   # this function launches the REPL
        while True:
            try:
                print(">", end = " ")
                line = input()
            except EOFError:
                break;
            self.run(line)

    def report(self,line_num, where, message):
        print(f"[line {line_num} ] Error {where} : {message}")
        self.had_error = True;

    def error(self,line_num, message):
        self.report(line_num, "", message)

    def run(self,line):  # Runs the code line by line
        scanner_obj = Scanner(line, self)
        tokens = scanner_obj.scan_tokens()
        for i in tokens:
            print(i)

interpreter = Lox()
if(len(sys.argv) > 2):
    print("Usage : python3 lox.py [script]")
    sys.exit(64)
elif(len(sys.argv) == 2):
    interpreter.run_file(sys.argv[1])
else:
    interpreter.run_prompt();


