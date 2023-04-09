# h3avren

from token import Token, TokenType as tt

class Scanner:
    def __init__(self, source : str, interpreter):
        self.source = source
        self.tokens = []
        self.interpreter = interpreter

        self.start = 0
        self.current = 0
        self.line = 1
        self.keywords = {"and" : tt.AND,
                         "class" : tt.CLASS,
                         "else" : tt.ELSE,
                         "false" : tt.FALSE,
                         "for" : tt.FOR,
                         "fun" : tt.FUN,
                         "if" : tt.IF,
                         "nil" : tt.NIL,
                         "or" : tt.OR,
                         "print" : tt.PRINT,
                         "return" : tt.RETURN,
                         "super" : tt.SUPER,
                         "this" : tt.THIS,
                         "true" : tt.TRUE,
                         "var" : tt.VAR,
                         "while" : tt.WHILE}
    
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
            elif(self.isalpha(char)):
                self.identifier()
            else:
                self.interpreter.error(self.line, "Unexpected character.")
    
    def isalpha(self, char):
        return (char >= 'a' and char <= 'z') or (char >='A' and char <= 'Z') or (char == '_')

    def identifier(self):
        while(self.isalphanumeric(self.peek())):
            self.advance()
        text = self.source[self.start : self.current]
        type_ = self.keywords.get(text)
        if(type_ == None):
            type_ = tt.IDENTIFIER
        self.addToken(type_)
    
    def isalphanumeric(self, char):
        return self.isalpha(char) or self.isdigit(char)

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
            self.interpreter.error(self.line,"Unterminating string..!")
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
        return self.source[(self.current - 1)]

    def addToken(self, type : tt, literal = None):
        text = self.source[self.start : self.current]
        self.tokens.append(Token(type, text, literal, self.line))

    def is_at_end(self):
        return self.current >= len(self.source)

