class Parser:
    def parse(self, input_string):
        self.input_string = input_string
        self.index = 0
        self.current_token = None
        self.next_token()
        return self.expr()

    def next_token(self):
        if self.index < len(self.input_string):
            self.current_token = self.input_string[self.index]
            self.index += 1
        else:
            self.current_token = None

    def match(self, token):
        if self.current_token == token:
            self.next_token()
        else:
            raise SyntaxError(f"Expected {token}, found {self.current_token}")

    def expr(self):
        if self.current_token.isdigit():
            num = self.current_token
            self.match(num)
            return int(num)
        elif self.current_token == '(':
            self.match('(')
            result = self.expr()
            self.match(')')
            return result
        else:
            raise SyntaxError("Invalid expression")

# Example usage:
parser = Parser()

input_string = "(1)"
result = parser.parse(input_string)
print("Result:", result)
