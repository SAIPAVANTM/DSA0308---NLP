class FOPCParser:
    def __init__(self, expression):
        self.expression = expression
        self.pos = 0

    def parse(self):
        tokens = self.tokenize()
        return self.parse_expression(tokens)

    def tokenize(self):
        # Tokenize the expression into a list of tokens
        tokens = []
        while self.pos < len(self.expression):
            if self.expression[self.pos] == '(' or self.expression[self.pos] == ')':
                tokens.append(self.expression[self.pos])
                self.pos += 1
            elif self.expression[self.pos].isalpha():
                identifier = ''
                while self.pos < len(self.expression) and (self.expression[self.pos].isalnum() or self.expression[self.pos] == '_'):
                    identifier += self.expression[self.pos]
                    self.pos += 1
                tokens.append(identifier)
            else:
                self.pos += 1
        return tokens

    def parse_expression(self, tokens):
        if not tokens:
            return None
        token = tokens.pop(0)
        if token == '(':
            # Parse a compound expression
            operator = tokens.pop(0)
            if operator == 'not':
                return ('not', self.parse_expression(tokens))
            else:
                left_expr = self.parse_expression(tokens)
                right_expr = self.parse_expression(tokens)
                return (operator, left_expr, right_expr)
        elif token == ')':
            return None  # End of compound expression
        else:
            # Parse a simple expression
            return token


# Example usage
if __name__ == "__main__":
    expression = "(and (or A B) (not C))"
    parser = FOPCParser(expression)
    parsed_expression = parser.parse()
    print(parsed_expression)
