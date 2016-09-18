INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def __str__(self):
        return 'Token({type}, {value})'.format(
            type = self.type,
            value = self.value
        )
    
    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.currant_token = None
    
    def error(self):
        raise Exception('Error parsing input')
    
    def get_next_token(self):
        text = self.text
        
        if self.pos > len(text) - 1:
            return Token(EOF, None)
        
        currant_char = text[self.pos]
        
        if currant_char.isdigit():
            currant_token = Token(INTEGER, int(currant_char))
            self.pos += 1
            return currant_token
        
        if currant_char == '+':
            currant_token = Token(PLUS, currant_char)
            self.pos += 1
            return currant_token
        
        self.error()

    def eat(self, token_type):
        if self.currant_token.type == token_type:
            self.currant_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.currant_token = self.get_next_token()

        left = self.currant_token
        self.eat(INTEGER)

        mid = self.currant_token
        self.eat(PLUS)

        right = self.currant_token
        self.eat(INTEGER)

        result = left.value + right.value

        return result

def main():
    while True:
        try:
            try:
                text = raw_input('calc> ')
            except NameError:
                text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()
            