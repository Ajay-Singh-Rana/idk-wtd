# h3avren

from token import Token, TokenType

class Scanner:
    def __init__(self, source : str):
        self.source = source
        tokens = []

        start = 0
        current = 0
        line = 1
    
    def scanTokens(){
        while(not self.is_at_end()):
            start = current
            self.scanToken()
        self.tokens.add(Token(TokenType(EOF), "", None ,line))
        return self.tokens
    def scanToken():
        char = self.advance()
        if(char == '('):
            self.addToken(LEFT_PAREN)
        elif(char == ')'):
            self.addToken(RIGHT_PAREN)
        elif(char == '{'):
            self.addToken(LEFT_BRACE)
        elif(char == '}'):
            self.addToken(RIGHT_BRACE)
        elif(char == ','):
            self.addToken(COMMA)
        elif(char == '.'):
            self.addToken(DOT)
        elif(char == '-'):
            self.addToken(MINUS)
        elif(char == '+'):
            self.addToken(PLUS)
        elif(char == ';'):
            self.addToken(SEMICOLON)
        elif(char == '*'):
            self.addToken(STAR)
        elif(char == '!'):
            self.addToken(BANG_EQUAL if self.match('=') else BANG)
        elif(char == '='):
            self.addToken(EQUAL_EQUAL if self.match('=') else EQUAL)
        elif(char == '<'):
            self.addToken(LESS_EQUAL if self.match('=') else LESS)
        elif(char == '>'):
            self.addToken(GREATER_EQUAL if self.match('=') else GREATER)
        elif(char == '/'):
            if(self.match('/'):
                while(peek() != '\n' and not self.is_at_end()):
                    self.advance()
            else:
                self.addToken(SLASH)
        elif(char == ' ' or char == '\t' or char == '\r'):
            continue
        elif(char == '\n'):
            self.line += 1
            continue
        else:
            Lox.error(line, "Unexpected character.")

    def peek():
        if(self.is_at_end()):
            return '\0'
        return self.source[current]

    def match(expected):
        if(self.is_at_end()):
            return False
        elif(self.source[current] != expected):
            return False
        self.current += 1
        return True

    def advance():
        self.current += 1
        return self.source[self.current - 1]

    def addToken(type : TokenType, literal = None):
        text = self.source[self.start : self.current]
        self.tokens.append(Token(type, text, literal, line)

    def is_at_end():
        return self.current >= len(self.source)

