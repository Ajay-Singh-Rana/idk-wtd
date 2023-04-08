# h3avren

from token import Token, TokenType as tt

class Scanner:
    def __init__(self, source : str):
        self.source = source
        self.tokens = []

        self.start = 0
        self.current = 0
        self.line = 1
    
    def scan_tokens(self):
        while(not self.is_at_end()):
            self.start = self.current
            self.scan_token()
        self.tokens.append(Token(tt.EOF, "", None , self.line))
        return self.tokens
    
    def scan_token(self):
        char = self.advance()
        if(char == '('):
            self.addToken(tt.LEFT_PAREN)
        elif(char == ')'):
            self.addToken(tt.RIGHT_PAREN)
        elif(char == '{'):
            self.addToken(tt.LEFT_BRACE)
        elif(char == '}'):
            self.addToken(tt.RIGHT_BRACE)
        elif(char == ','):
            self.addToken(tt.COMMA)
        elif(char == '.'):
            self.addToken(tt.DOT)
        elif(char == '-'):
            self.addToken(tt.MINUS)
        elif(char == '+'):
            self.addToken(tt.PLUS)
        elif(char == ';'):
            self.addToken(tt.SEMICOLON)
        elif(char == '*'):
            self.addToken(tt.STAR)
        elif(char == '!'):
            self.addToken(tt.BANG_EQUAL if self.match('=') else tt.BANG)
        elif(char == '='):
            self.addToken(tt.EQUAL_EQUAL if self.match('=') else tt.EQUAL)
        elif(char == '<'):
            self.addToken(tt.LESS_EQUAL if self.match('=') else tt.LESS)
        elif(char == '>'):
            self.addToken(tt.GREATER_EQUAL if self.match('=') else tt.GREATER)
        elif(char == '/'):
            if(self.match('/')):
                while(peek() != '\n' and not self.is_at_end()):
                    self.advance()
            else:
                self.addToken(tt.SLASH)
        elif(char == ' ' or char == '\t' or char == '\r'):
            pass
        elif(char == '\n'):
            self.line += 1
        elif(char == '"'):
            self.string()
        else:
            if(self.isdigit(char)):
                self.number()
            else:
                print("Unexpected character at line ", self.line)
                # Lox.error(self.line, "Unexpected character.")
    
    def isdigit(self, char):
        return char >= '0' and char <= '9'
    
    def number(self):
        while(self.isdigit(self.peek())):
            self.advance()

        # Look for a fractional part.
        if(self.peek() == '.' and self.isdigit(self.peek_next())):
            self.advance()  # consume the "."
            while(self.isdigit(self.peek())):
                self.advance()
        self.addToken(tt.NUMBER, float(self.source[self.start, self.current]))
    
    def peek_next():
        if(self.current + 1 >= len(self.source)):
            return '\0'
        return self.source[self.current + 1]

    def string(self):
        while(not self.peek() == '"' and not self.is_at_end()):
            if(self.peek() == '\n'):
                self.line += 1
            self.advance()
        if(self.is_at_end()):
            print("Unterminating string at line ", self.line)
            # Lox.error(self.line,"Unterminating string..!")
            return
        self.advance()  # the closing ".
        string = self.source[self.start + 1 : self.current - 1]
        self.addToken(tt.STRING, string)


    def peek(self):
        if(self.is_at_end()):
            return '\0'
        return self.source[self.current]

    def match(self, expected):
        if(self.is_at_end()):
            return False
        elif(self.source[self.current] != expected):
            return False
        self.current += 1
        return True

    def advance(self):
        self.current += 1
        print(len(self.source))
        print(self.current)
        return self.source[(self.current - 1)]

    def addToken(self, type : tt, literal = None):
        text = self.source[self.start : self.current]
        self.tokens.append(Token(type, text, literal, self.line))

    def is_at_end(self):
        return self.current >= len(self.source)

